"""
Análisis Computacional de Cadenas de Markov
Universidad Nacional de Colombia
"""

import numpy as np

def _initialize_gpu():
    try:
        import cupy as cp
        cp.cuda.Device().compute_capability
        return cp, True
    except:
        return None, False

cp, GPU_AVAILABLE = _initialize_gpu()

def crear_matriz_probabilidad(n, p):
    """Crea matriz de transición de n estados con probabilidad p."""
    if not 0 <= p <= 1 or n <= 0:
        raise ValueError("p debe estar en [0,1] y n>0")

    P = np.zeros((n, n), dtype=np.float64)
    if n == 1:
        P[0, 0] = 1.0
        return P

    P[0, [0, 1]] = [1-p, p]
    for i in range(1, n-1):
        P[i, [i-1, i+1]] = [1-p, p]
    P[n-1, [n-2, n-1]] = [1-p, p]

    return P

def calcular_distribucion_metodo_autovalores(matriz):
    """Método 1: Vectores propios. Resuelve πP = π."""
    valores, vectores = np.linalg.eig(matriz.T)
    idx = np.argmin(np.abs(valores - 1.0))
    pi = np.abs(np.real(vectores[:, idx]))
    return pi / np.sum(pi)

def calcular_distribucion_metodo_tiempo_retorno(matriz):
    """Método 2: Tiempos de retorno. Calcula πᵢ = 1/E[Tᵢ]."""
    n = matriz.shape[0]
    tiempos = np.zeros(n, dtype=np.float64)

    for i in range(n):
        idx = [j for j in range(n) if j != i]
        if not idx:
            tiempos[i] = 1.0
            continue

        P_red = matriz[np.ix_(idx, idx)]
        A = np.eye(len(idx), dtype=np.float64) - P_red
        b = np.ones(len(idx), dtype=np.float64)

        try:
            h = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            h = _resolver_iterativo(P_red, b)

        tiempos[i] = 1.0 + sum(matriz[i, j] * h[k] for k, j in enumerate(idx))

    pi = 1.0 / np.maximum(tiempos, 1e-15)
    pi = np.abs(pi) / np.sum(np.abs(pi))

    if np.any(np.isnan(pi)):
        return _metodo_potencias(matriz)
    return pi

def _resolver_iterativo(P_red, b, max_iter=5000, tol=1e-12):
    h = np.ones(len(b), dtype=np.float64)
    for _ in range(max_iter):
        h_new = P_red @ h + b
        if np.linalg.norm(h_new - h) < tol:
            break
        h = h_new
    return h

def _metodo_potencias(matriz, max_iter=10000, tol=1e-12):
    n = matriz.shape[0]
    pi = np.ones(n, dtype=np.float64) / n
    for _ in range(max_iter):
        pi_new = pi @ matriz
        pi_new /= np.sum(pi_new)
        if np.max(np.abs(pi_new - pi)) < tol:
            break
        pi = pi_new
    return pi

def calcular_distribucion_metodo_autovalores_gpu(matriz):
    """Versión GPU del Método 1."""
    if not GPU_AVAILABLE:
        raise RuntimeError("GPU no disponible")

    P_gpu = cp.asarray(matriz, dtype=cp.float64)
    n = P_gpu.shape[0]

    try:
        A = P_gpu.T - cp.eye(n, dtype=cp.float64)
        A[-1, :] = 1.0
        b = cp.zeros(n, dtype=cp.float64)
        b[-1] = 1.0
        pi = cp.linalg.solve(A, b)
        pi = cp.abs(pi) / cp.sum(cp.abs(pi))
        return cp.asnumpy(pi)
    except cp.linalg.LinAlgError:
        return _metodo_potencias_gpu(P_gpu)

def _metodo_potencias_gpu(P_gpu, max_iter=1000, tol=1e-12):
    n = P_gpu.shape[0]
    pi = cp.random.random(n, dtype=cp.float64)
    pi /= cp.sum(pi)
    PT = P_gpu.T
    for _ in range(max_iter):
        pi_new = pi @ PT
        pi_new /= cp.sum(pi_new)
        if cp.linalg.norm(pi_new - pi) < tol:
            break
        pi = pi_new
    return cp.asnumpy(pi)

def calcular_distribucion_metodo_tiempo_retorno_gpu(matriz):
    """Versión GPU del Método 2."""
    if not GPU_AVAILABLE:
        raise RuntimeError("GPU no disponible")
    if matriz.shape[0] > 200:
        return calcular_distribucion_metodo_tiempo_retorno(matriz)

    P_gpu = cp.asarray(matriz, dtype=cp.float64)
    n = P_gpu.shape[0]

    try:
        tiempos = cp.zeros(n, dtype=cp.float64)
        for i in range(n):
            idx = [j for j in range(n) if j != i]
            if not idx:
                tiempos[i] = 1.0
                continue

            idx_gpu = cp.array(idx)
            P_red = P_gpu[cp.ix_(idx_gpu, idx_gpu)]
            A = cp.eye(len(idx), dtype=cp.float64) - P_red
            b = cp.ones(len(idx), dtype=cp.float64)

            try:
                h = cp.linalg.solve(A, b)
            except cp.linalg.LinAlgError:
                h = _resolver_iterativo_gpu(P_red, b)

            tiempos[i] = 1.0 + sum(P_gpu[i, j] * h[k] for k, j in enumerate(idx))

        pi = 1.0 / tiempos
        return cp.asnumpy(pi / cp.sum(pi))
    except Exception:
        return calcular_distribucion_metodo_tiempo_retorno(matriz)

def _resolver_iterativo_gpu(P_red, b, max_iter=5000, tol=1e-12):
    h = cp.ones(len(b), dtype=cp.float64)
    for _ in range(max_iter):
        h_new = P_red @ h + b
        if cp.linalg.norm(h_new - h) < tol:
            break
        h = h_new
    return h

def get_gpu_info():
    """Retorna información de GPU disponible."""
    if not GPU_AVAILABLE:
        return {"available": False}
    try:
        device = cp.cuda.Device()
        props = cp.cuda.runtime.getDeviceProperties(device.id)
        return {
            "available": True,
            "device_id": device.id,
            "name": props['name'].decode(),
            "compute_capability": f"{props['major']}.{props['minor']}",
            "total_memory_mb": props['totalGlobalMem'] // 1024**2
        }
    except Exception as e:
        return {"available": False, "error": str(e)}

def clear_gpu_memory():
    """Libera memoria GPU."""
    if GPU_AVAILABLE:
        try:
            cp.get_default_memory_pool().free_all_blocks()
            cp.get_default_pinned_memory_pool().free_all_blocks()
            return True
        except:
            return False
    return False

def recomendar_metodo(n):
    """Recomienda método óptimo según tamaño de matriz."""
    if not GPU_AVAILABLE:
        return {"metodo1": "CPU", "metodo2": "CPU"}
    if n <= 50:
        return {"metodo1": "CPU", "metodo2": "CPU"}
    else:
        return {"metodo1": "GPU", "metodo2": "CPU"}
