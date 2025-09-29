"""
Benchmark CPU vs GPU para cálculo de distribuciones estacionarias

Este script compara el rendimiento entre las implementaciones CPU (NumPy)
y GPU (CuPy) de ambos métodos para calcular distribuciones estacionarias.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.markov_matrix import (
    crear_matriz_probabilidad,
    calcular_distribucion_metodo_autovalores,
    calcular_distribucion_metodo_tiempo_retorno,
    GPU_AVAILABLE
)

if GPU_AVAILABLE:
    from src.markov_matrix import (
        crear_matriz_probabilidad_gpu,
        calcular_distribucion_metodo_autovalores_gpu,
        calcular_distribucion_metodo_tiempo_retorno_gpu
    )
    import cupy as cp

import numpy as np
import time
import pandas as pd

def benchmark_metodo_1(n, p, repeticiones=5):
    """Benchmark Método 1: Vectores propios"""

    # Crear matriz en CPU
    matriz_cpu = crear_matriz_probabilidad(n, p)

    # Benchmark CPU
    tiempos_cpu = []
    for _ in range(repeticiones):
        start = time.time()
        pi_cpu = calcular_distribucion_metodo_autovalores(matriz_cpu)
        tiempos_cpu.append(time.time() - start)

    tiempo_cpu = np.mean(tiempos_cpu)

    if not GPU_AVAILABLE:
        return tiempo_cpu, None, None, pi_cpu, None

    # Benchmark GPU
    tiempos_gpu = []
    for _ in range(repeticiones):
        start = time.time()
        pi_gpu = calcular_distribucion_metodo_autovalores_gpu(matriz_cpu)
        tiempos_gpu.append(time.time() - start)

    tiempo_gpu = np.mean(tiempos_gpu)
    speedup = tiempo_cpu / tiempo_gpu if tiempo_gpu > 0 else float('inf')

    return tiempo_cpu, tiempo_gpu, speedup, pi_cpu, pi_gpu

def benchmark_metodo_2(n, p, repeticiones=5):
    """Benchmark Método 2: Tiempo medio de retorno"""

    # Crear matriz en CPU
    matriz_cpu = crear_matriz_probabilidad(n, p)

    # Benchmark CPU
    tiempos_cpu = []
    for _ in range(repeticiones):
        start = time.time()
        pi_cpu = calcular_distribucion_metodo_tiempo_retorno(matriz_cpu)
        tiempos_cpu.append(time.time() - start)

    tiempo_cpu = np.mean(tiempos_cpu)

    if not GPU_AVAILABLE:
        return tiempo_cpu, None, None, pi_cpu, None

    # Benchmark GPU
    tiempos_gpu = []
    for _ in range(repeticiones):
        start = time.time()
        pi_gpu = calcular_distribucion_metodo_tiempo_retorno_gpu(matriz_cpu)
        tiempos_gpu.append(time.time() - start)

    tiempo_gpu = np.mean(tiempos_gpu)
    speedup = tiempo_cpu / tiempo_gpu if tiempo_gpu > 0 else float('inf')

    return tiempo_cpu, tiempo_gpu, speedup, pi_cpu, pi_gpu

def ejecutar_benchmark_completo():
    """Ejecutar benchmark completo con diferentes tamaños de matriz"""

    print("=== BENCHMARK CPU vs GPU ===")
    print(f"GPU disponible: {GPU_AVAILABLE}")
    if GPU_AVAILABLE:
        print(f"GPU: {cp.cuda.runtime.getDeviceProperties(0)['name'].decode()}")
    print()

    # Parámetros de prueba
    tamaños = [10, 50, 100, 200, 500]
    p = 0.6

    resultados = []

    print("Ejecutando benchmarks...")
    print("Tamaño | Método 1 CPU | Método 1 GPU | Speedup 1 | Método 2 CPU | Método 2 GPU | Speedup 2")
    print("-" * 95)

    for n in tamaños:
        print(f"n={n:3d} ", end="", flush=True)

        # Benchmark Método 1
        t1_cpu, t1_gpu, s1, pi1_cpu, pi1_gpu = benchmark_metodo_1(n, p)

        # Benchmark Método 2
        t2_cpu, t2_gpu, s2, pi2_cpu, pi2_gpu = benchmark_metodo_2(n, p)

        # Verificar precisión
        error1 = 0.0 if pi1_gpu is None else np.max(np.abs(pi1_cpu - pi1_gpu))
        error2 = 0.0 if pi2_gpu is None else np.max(np.abs(pi2_cpu - pi2_gpu))

        if GPU_AVAILABLE:
            print(f"| {t1_cpu:8.4f}s | {t1_gpu:8.4f}s | {s1:6.2f}x | {t2_cpu:8.4f}s | {t2_gpu:8.4f}s | {s2:6.2f}x")
        else:
            print(f"| {t1_cpu:8.4f}s |    N/A    |  N/A  | {t2_cpu:8.4f}s |    N/A    |  N/A")

        resultados.append({
            'n': n,
            'metodo1_cpu': t1_cpu,
            'metodo1_gpu': t1_gpu,
            'speedup1': s1,
            'metodo2_cpu': t2_cpu,
            'metodo2_gpu': t2_gpu,
            'speedup2': s2,
            'error1': error1,
            'error2': error2
        })

    return pd.DataFrame(resultados)

def ejemplo_uso_gpu():
    """Ejemplo de uso básico con GPU"""

    if not GPU_AVAILABLE:
        print("GPU no disponible. Ejecutando solo en CPU.")
        return

    print("\n=== EJEMPLO DE USO GPU ===")

    # Parámetros
    n = 4
    p = 0.7

    print(f"Matriz de {n}x{n} con p={p}")

    # Crear matriz
    matriz = crear_matriz_probabilidad(n, p)
    print("\nMatriz de transición:")
    print(matriz)

    # Método 1 - GPU
    start = time.time()
    pi1_gpu = calcular_distribucion_metodo_autovalores_gpu(matriz)
    t1_gpu = time.time() - start

    # Método 2 - GPU
    start = time.time()
    pi2_gpu = calcular_distribucion_metodo_tiempo_retorno_gpu(matriz)
    t2_gpu = time.time() - start

    print(f"\nResultados GPU:")
    print(f"Método 1 (vectores propios): {pi1_gpu} (tiempo: {t1_gpu:.6f}s)")
    print(f"Método 2 (tiempo retorno):   {pi2_gpu} (tiempo: {t2_gpu:.6f}s)")
    print(f"Diferencia entre métodos:    {np.max(np.abs(pi1_gpu - pi2_gpu)):.2e}")

    # Verificación
    verificacion = pi1_gpu @ matriz
    error = np.linalg.norm(pi1_gpu - verificacion)
    print(f"Verificación πP = π:         Error = {error:.2e}")

if __name__ == "__main__":
    # Ejecutar ejemplo básico
    ejemplo_uso_gpu()

    # Ejecutar benchmark completo
    df_resultados = ejecutar_benchmark_completo()

    # Guardar resultados
    df_resultados.to_csv('benchmark_cpu_gpu.csv', index=False)
    print(f"\nResultados guardados en: benchmark_cpu_gpu.csv")

    if GPU_AVAILABLE:
        print(f"\nResumen de speedups promedio:")
        print(f"Método 1 (vectores propios): {df_resultados['speedup1'].mean():.2f}x")
        print(f"Método 2 (tiempo retorno):   {df_resultados['speedup2'].mean():.2f}x")