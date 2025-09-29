import numpy as np

# Intento de importar CuPy para cálculos en GPU
try:
    import cupy as cp
    # Verificar que CuPy puede crear arrays y ejecutar operaciones básicas
    test_array = cp.array([1, 2, 3])
    _ = test_array + 1  # Test de operación básica
    _ = cp.ones(3)      # Test de creación de arrays
    GPU_AVAILABLE = True
    print("✅ CuPy disponible: se pueden usar cálculos en GPU")
except ImportError:
    cp = None
    GPU_AVAILABLE = False
    print("❌ CuPy no instalado: solo cálculos en CPU")
    print("💡 Instale CuPy con: pip install cupy-cuda12x")
except Exception as e:
    cp = None
    GPU_AVAILABLE = False
    error_msg = str(e)
    if "libnvrtc" in error_msg:
        print("❌ CuPy instalado pero faltan librerías CUDA")
        print("💡 Instale CUDA Toolkit completo o use modo CPU")
        print("💡 Alternativa: ejecute en Google Colab o entorno con CUDA completo")
    else:
        print(f"❌ CuPy instalado pero no funcional: {error_msg}")
    print("🔄 Usando solo cálculos en CPU")

def crear_matriz_probabilidad(n, p):
    """
    Crea una matriz de probabilidad para una cadena de Markov donde:
    - n: número de estados
    - Estados intermedios: probabilidad p de ir al siguiente, 1-p de volver al anterior
    - Estado inicial: probabilidad p de avanzar, 1-p de quedarse
    - Estado final: probabilidad p de quedarse, 1-p de retroceder

    Returns:
        numpy.ndarray: Matriz de probabilidad n x n
    """
    if not 0 <= p <= 1:
        raise ValueError("p debe estar entre 0 y 1")
    if n <= 0:
        raise ValueError("n debe ser mayor que 0")

    # Crear matriz de ceros
    matriz = np.zeros((n, n))

    # Para estados intermedios (1 a n-2):
    # - Probabilidad p de ir al siguiente estado
    # - Probabilidad 1-p de volver al estado anterior
    for i in range(1, n-1):
        matriz[i, i+1] = p      # siguiente estado
        matriz[i, i-1] = 1-p    # estado anterior

    # Estado inicial (0): probabilidad p de avanzar, 1-p de quedarse
    if n > 1:
        matriz[0, 0] = 1-p      # quedarse en el estado inicial
        matriz[0, 1] = p        # avanzar al siguiente estado

    # Estado final (n-1): probabilidad p de quedarse, 1-p de retroceder
    if n > 1:
        matriz[n-1, n-1] = p        # quedarse en el estado final
        matriz[n-1, n-2] = 1-p      # retroceder al estado anterior

    return matriz

def calcular_distribucion_metodo_autovalores(matriz):
    """
    Calcula la distribución estacionaria usando vectores propios (Método 1).
    
    Resuelve πP = π, donde π es la distribución estacionaria.
    Para esto, calculamos el vector propio izquierdo de P asociado al valor propio 1,
    que es equivalente al vector propio derecho de P^T.
    
    Args:
        matriz: numpy.ndarray - Matriz de transición P
    
    Returns:
        numpy.ndarray: Distribución estacionaria π normalizada
    """
    # Para πP = π, necesitamos el vector propio izquierdo de P
    # Esto equivale al vector propio derecho de P^T
    valores_propios, vectores_propios = np.linalg.eig(matriz.T)
    
    # Buscar el valor propio más cercano a 1
    indice_1 = np.argmin(np.abs(valores_propios - 1.0))
    
    # Obtener el vector propio correspondiente
    pi = vectores_propios[:, indice_1]
    
    # Tomar valores reales (ignorar parte imaginaria por errores numéricos)
    pi = np.real(pi)
    
    # Normalizar para que sume 1 y sea positivo
    pi = np.abs(pi)
    pi = pi / np.sum(pi)
    
    return pi

def calcular_distribucion_metodo_tiempo_retorno(matriz):
    """
    Calcula la distribución estacionaria usando tiempos medios de retorno (Método 2).

    Utiliza el teorema fundamental: πᵢ = 1/E[Tᵢ], donde E[Tᵢ] es el tiempo
    esperado de retorno al estado i.

    Para calcular E[Tᵢ], resolvemos el sistema:
    - mᵢⱼ = 1 + Σₖ≠ᵢ pⱼₖ * mᵢₖ para j ≠ i
    - mᵢᵢ = 1

    Args:
        matriz: numpy.ndarray - Matriz de transición P

    Returns:
        numpy.ndarray: Distribución estacionaria π calculada con tiempos de retorno
    """
    n = matriz.shape[0]
    tiempos_retorno = np.zeros(n)

    # Para cada estado i, calcular el tiempo medio de retorno E[Tᵢ]
    for i in range(n):
        # Construir el sistema para calcular los tiempos medios de primera pasada
        # mᵢⱼ = tiempo esperado para llegar a i desde j
        A = np.eye(n) - matriz.copy()

        # Para el estado destino i: mᵢᵢ = 0 (ya estamos ahí)
        A[i, :] = 0
        A[i, i] = 1

        # Vector b: 1 para todos los estados excepto el destino
        b = np.ones(n)
        b[i] = 0

        # Resolver el sistema Am = b
        m = np.linalg.solve(A, b)

        # El tiempo medio de retorno desde i es 1 + mᵢⱼ * pᵢⱼ sumado sobre j≠i
        # Pero por la estructura del problema, E[Tᵢ] = 1 + Σⱼ≠ᵢ pᵢⱼ * mⱼ
        tiempo_retorno = 1.0
        for j in range(n):
            if j != i:
                tiempo_retorno += matriz[i, j] * m[j]

        tiempos_retorno[i] = tiempo_retorno

    # Calcular la distribución estacionaria: πᵢ = 1/E[Tᵢ]
    pi = 1.0 / tiempos_retorno

    # Normalizar para que sume 1
    pi = pi / np.sum(pi)

    return pi

def calcular_distribucion_metodo_autovalores_gpu(matriz):
    """
    Versión GPU del Método 1: Vectores propios usando CuPy + iteración de potencias.

    Args:
        matriz: numpy.ndarray - Matriz de transición P

    Returns:
        numpy.ndarray: Distribución estacionaria π (devuelta a CPU)
    """
    if not GPU_AVAILABLE:
        raise RuntimeError("CuPy no está disponible. Use la versión CPU.")

    # Nota: CuPy no tiene cp.linalg.eig, solo eigh para matrices simétricas
    # Usamos el método de potencias para encontrar el vector propio dominante

    # Transferir matriz a GPU
    P = cp.array(matriz)
    n = P.shape[0]

    # Vector inicial aleatorio
    pi = cp.ones(n, dtype=cp.float64) / n

    # Método de potencias: π = π * P^T
    # Como πP = π, entonces π * P^T = π
    PT = P.T

    # Iterar hasta convergencia
    for _ in range(1000):  # máximo 1000 iteraciones
        pi_nuevo = pi @ PT
        pi_nuevo = pi_nuevo / cp.sum(pi_nuevo)

        # Verificar convergencia
        if cp.max(cp.abs(pi_nuevo - pi)) < 1e-12:
            break

        pi = pi_nuevo

    # Asegurar que todos los valores sean positivos
    pi = cp.abs(pi)
    pi = pi / cp.sum(pi)

    # Devolver resultado a CPU
    return cp.asnumpy(pi)

def calcular_distribucion_metodo_tiempo_retorno_gpu(matriz):
    """
    Versión GPU del Método 2: Tiempo medio de retorno usando CuPy.

    Args:
        matriz: numpy.ndarray - Matriz de transición P

    Returns:
        numpy.ndarray: Distribución estacionaria π (devuelta a CPU)
    """
    if not GPU_AVAILABLE:
        raise RuntimeError("CuPy no está disponible. Use la versión CPU.")

    # Transferir matriz a GPU
    matriz_gpu = cp.array(matriz)
    n = matriz_gpu.shape[0]
    tiempos_retorno = cp.zeros(n)

    # Para cada estado i, calcular el tiempo medio de retorno E[Tᵢ]
    for i in range(n):
        # Construir el sistema en GPU
        A = cp.eye(n) - matriz_gpu.copy()
        A[i, :] = 0
        A[i, i] = 1

        b = cp.ones(n)
        b[i] = 0

        # Resolver sistema lineal en GPU
        m = cp.linalg.solve(A, b)

        # Calcular tiempo de retorno
        tiempo_retorno = 1.0
        for j in range(n):
            if j != i:
                tiempo_retorno += matriz_gpu[i, j] * m[j]

        tiempos_retorno[i] = tiempo_retorno

    # Calcular distribución estacionaria
    pi = 1.0 / tiempos_retorno
    pi = pi / cp.sum(pi)

    # Devolver resultado a CPU
    return cp.asnumpy(pi)

def crear_matriz_probabilidad_gpu(n, p):
    """
    Versión GPU de crear_matriz_probabilidad usando CuPy.

    Args:
        n: número de estados
        p: probabilidad de avance

    Returns:
        cupy.ndarray: Matriz de probabilidad en GPU
    """
    if not GPU_AVAILABLE:
        raise RuntimeError("CuPy no está disponible. Use la versión CPU.")

    # Crear matriz de ceros en GPU
    matriz = cp.zeros((n, n))

    # Estados intermedios
    for i in range(1, n-1):
        matriz[i, i+1] = p
        matriz[i, i-1] = 1-p

    # Estado inicial
    if n > 1:
        matriz[0, 0] = 1-p
        matriz[0, 1] = p

    # Estado final
    if n > 1:
        matriz[n-1, n-1] = p
        matriz[n-1, n-2] = 1-p

    return matriz
