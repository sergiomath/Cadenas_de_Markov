import numpy as np

# Configuración y detección optimizada de CuPy
def _initialize_gpu():
    """Inicializar y configurar GPU si está disponible"""
    try:
        import cupy as cp

        # Verificar funcionalidad básica de CuPy
        test_array = cp.array([1, 2, 3])
        _ = test_array + 1
        _ = cp.ones(3)
        _ = cp.linalg.norm(cp.random.random((10, 10)))  # Test álgebra lineal

        # Configurar memoria pool para mejor rendimiento
        mempool = cp.get_default_memory_pool()
        pinned_mempool = cp.get_default_pinned_memory_pool()

        # Información de GPU
        device_id = cp.cuda.Device().id
        device_name = cp.cuda.runtime.getDeviceProperties(device_id)['name'].decode()
        total_mem = cp.cuda.runtime.getDeviceProperties(device_id)['totalGlobalMem']

        print(f"✅ CuPy disponible: {device_name} ({total_mem // 1024**2} MB)")
        return cp, True

    except ImportError:
        print("❌ CuPy no instalado")
        print("💡 Instale: pip install cupy-cuda13x (para CUDA 13.x)")
        return None, False

    except Exception as e:
        error_msg = str(e)
        if "libnvrtc" in error_msg:
            print("❌ CuPy instalado pero faltan librerías CUDA")
            print("💡 Configurar: export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH")
        else:
            print(f"❌ Error GPU: {error_msg}")
        print("🔄 Usando solo CPU")
        return None, False

# Inicializar GPU
cp, GPU_AVAILABLE = _initialize_gpu()

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
    Versión GPU optimizada del Método 1: Resuelve sistema (P^T - I)π = 0.

    Args:
        matriz: numpy.ndarray - Matriz de transición P

    Returns:
        numpy.ndarray: Distribución estacionaria π (devuelta a CPU)
    """
    if not GPU_AVAILABLE:
        raise RuntimeError("CuPy no está disponible. Use la versión CPU.")

    # Transferir matriz a GPU usando memoria optimizada
    P = cp.asarray(matriz, dtype=cp.float64)
    n = P.shape[0]

    try:
        # Método optimizado: Resolver (P^T - I)π = 0 con restricción Σπᵢ = 1
        # Construir sistema aumentado más eficientemente
        A = P.T - cp.eye(n, dtype=cp.float64)

        # Reemplazar última fila con restricción de normalización
        A[-1, :] = 1.0

        # Vector lado derecho
        b = cp.zeros(n, dtype=cp.float64)
        b[-1] = 1.0

        # Resolver usando descomposición LU (más estable que iteración de potencias)
        pi = cp.linalg.solve(A, b)

        # Asegurar positividad y normalización
        pi = cp.abs(pi)
        pi = pi / cp.sum(pi)

        return cp.asnumpy(pi)

    except cp.linalg.LinAlgError:
        # Si falla el método directo, usar método de potencias como respaldo
        return _metodo_potencias_gpu(P)

def _metodo_potencias_gpu(P):
    """Método de potencias optimizado como respaldo"""
    n = P.shape[0]

    # Vector inicial con componentes ligeramente diferentes para mejor convergencia
    pi = cp.random.random(n, dtype=cp.float64)
    pi = pi / cp.sum(pi)

    PT = P.T
    tol = 1e-12
    max_iter = min(1000, n * 10)  # Ajustar iteraciones según tamaño

    for i in range(max_iter):
        pi_nuevo = pi @ PT
        pi_nuevo = pi_nuevo / cp.sum(pi_nuevo)

        # Verificar convergencia con criterio optimizado
        if cp.linalg.norm(pi_nuevo - pi) < tol:
            break

        pi = pi_nuevo

    return cp.asnumpy(pi)

def calcular_distribucion_metodo_tiempo_retorno_gpu(matriz):
    """
    Versión GPU optimizada del Método 2: Tiempo medio de retorno vectorizado.

    Args:
        matriz: numpy.ndarray - Matriz de transición P

    Returns:
        numpy.ndarray: Distribución estacionaria π (devuelta a CPU)
    """
    if not GPU_AVAILABLE:
        raise RuntimeError("CuPy no está disponible. Use la versión CPU.")

    # Para matrices grandes, el Método 2 es inherentemente secuencial
    # y no se beneficia mucho de GPU. Usar CPU para mejor rendimiento.
    if matriz.shape[0] > 100:
        return calcular_distribucion_metodo_tiempo_retorno(matriz)

    # Transferir matriz a GPU con tipo optimizado
    P = cp.asarray(matriz, dtype=cp.float64)
    n = P.shape[0]

    try:
        # Método vectorizado para matrices pequeñas/medianas
        # Construir todas las matrices del sistema simultáneamente
        I = cp.eye(n, dtype=cp.float64)
        A_base = I - P

        # Preparar matrices para todos los estados
        tiempos_retorno = cp.zeros(n, dtype=cp.float64)

        # Procesar en lotes para mejor uso de memoria
        batch_size = min(32, n)
        for start_i in range(0, n, batch_size):
            end_i = min(start_i + batch_size, n)
            batch_size_actual = end_i - start_i

            # Crear lote de matrices A
            A_batch = cp.tile(A_base[None, :, :], (batch_size_actual, 1, 1))
            b_batch = cp.ones((batch_size_actual, n), dtype=cp.float64)

            # Modificar cada matriz del lote
            for idx, i in enumerate(range(start_i, end_i)):
                A_batch[idx, i, :] = 0.0
                A_batch[idx, i, i] = 1.0
                b_batch[idx, i] = 0.0

            # Resolver sistemas en lote
            m_batch = cp.linalg.solve(A_batch, b_batch)

            # Calcular tiempos de retorno para este lote
            for idx, i in enumerate(range(start_i, end_i)):
                # Vectorizar el cálculo del tiempo de retorno
                mask = cp.ones(n, dtype=bool)
                mask[i] = False
                tiempo_retorno = 1.0 + cp.sum(P[i, mask] * m_batch[idx, mask])
                tiempos_retorno[i] = tiempo_retorno

        # Calcular distribución estacionaria
        pi = 1.0 / tiempos_retorno
        pi = pi / cp.sum(pi)

        return cp.asnumpy(pi)

    except (cp.linalg.LinAlgError, cp.cuda.memory.MemoryError):
        # Si falla GPU, usar CPU como respaldo
        return calcular_distribucion_metodo_tiempo_retorno(matriz)

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

# ===== UTILIDADES GPU =====

def get_gpu_info():
    """Obtener información detallada de la GPU"""
    if not GPU_AVAILABLE:
        return {"available": False, "message": "GPU no disponible"}

    try:
        device = cp.cuda.Device()
        props = cp.cuda.runtime.getDeviceProperties(device.id)
        mempool = cp.get_default_memory_pool()

        return {
            "available": True,
            "device_id": device.id,
            "name": props['name'].decode(),
            "compute_capability": f"{props['major']}.{props['minor']}",
            "total_memory_mb": props['totalGlobalMem'] // 1024**2,
            "free_memory_mb": mempool.free_bytes() // 1024**2,
            "used_memory_mb": mempool.used_bytes() // 1024**2,
            "cuda_version": cp.cuda.runtime.runtimeGetVersion()
        }
    except Exception as e:
        return {"available": False, "error": str(e)}

def clear_gpu_memory():
    """Limpiar memoria GPU para evitar fragmentación"""
    if GPU_AVAILABLE:
        try:
            cp.get_default_memory_pool().free_all_blocks()
            cp.get_default_pinned_memory_pool().free_all_blocks()
            return True
        except Exception:
            return False
    return False

def optimal_gpu_method(n):
    """
    Determinar el método óptimo (CPU vs GPU) basado en el tamaño de matriz

    Args:
        n: tamaño de la matriz (número de estados)

    Returns:
        dict: Recomendaciones de método
    """
    if not GPU_AVAILABLE:
        return {
            "metodo1": "CPU",
            "metodo2": "CPU",
            "razon": "GPU no disponible"
        }

    if n <= 50:
        return {
            "metodo1": "CPU",
            "metodo2": "CPU",
            "razon": "Matrices pequeñas: overhead GPU > beneficio"
        }
    elif n <= 200:
        return {
            "metodo1": "GPU",
            "metodo2": "CPU",
            "razon": "Método 1 se beneficia de paralelización GPU"
        }
    else:
        return {
            "metodo1": "GPU",
            "metodo2": "CPU",
            "razon": "Método 1: GPU excelente, Método 2: inherentemente secuencial"
        }

def benchmark_gpu_vs_cpu(matriz, repeticiones=3):
    """
    Comparar rendimiento GPU vs CPU para una matriz específica

    Args:
        matriz: numpy.ndarray - Matriz de transición
        repeticiones: int - Número de repeticiones para promediar

    Returns:
        dict: Resultados del benchmark
    """
    import time

    n = matriz.shape[0]
    resultados = {
        "matriz_size": n,
        "repeticiones": repeticiones,
        "gpu_available": GPU_AVAILABLE
    }

    # Benchmark CPU
    tiempos_cpu = []
    for _ in range(repeticiones):
        start = time.time()
        pi_cpu = calcular_distribucion_metodo_autovalores(matriz)
        tiempos_cpu.append(time.time() - start)

    resultados["cpu_tiempo"] = np.mean(tiempos_cpu)
    resultados["cpu_std"] = np.std(tiempos_cpu)

    if GPU_AVAILABLE:
        # Benchmark GPU
        tiempos_gpu = []
        for _ in range(repeticiones):
            start = time.time()
            pi_gpu = calcular_distribucion_metodo_autovalores_gpu(matriz)
            tiempos_gpu.append(time.time() - start)

        resultados["gpu_tiempo"] = np.mean(tiempos_gpu)
        resultados["gpu_std"] = np.std(tiempos_gpu)
        resultados["speedup"] = resultados["cpu_tiempo"] / resultados["gpu_tiempo"]
        resultados["precision_error"] = np.max(np.abs(pi_cpu - pi_gpu))

        # Recomendación
        if resultados["speedup"] > 1.2:
            resultados["recomendacion"] = "GPU"
        elif resultados["speedup"] < 0.8:
            resultados["recomendacion"] = "CPU"
        else:
            resultados["recomendacion"] = "Similar"

    else:
        resultados["recomendacion"] = "CPU (GPU no disponible)"

    return resultados
