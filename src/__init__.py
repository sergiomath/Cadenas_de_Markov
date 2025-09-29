"""
Módulo para trabajar con Cadenas de Markov
"""

from .markov_matrix import (
    crear_matriz_probabilidad,
    calcular_distribucion_metodo_autovalores,
    calcular_distribucion_metodo_tiempo_retorno,
    calcular_distribucion_metodo_autovalores_gpu,
    calcular_distribucion_metodo_tiempo_retorno_gpu,
    crear_matriz_probabilidad_gpu,
    GPU_AVAILABLE,
    get_gpu_info,
    clear_gpu_memory,
    optimal_gpu_method,
    benchmark_gpu_vs_cpu
)

__all__ = [
    'crear_matriz_probabilidad',
    'calcular_distribucion_metodo_autovalores',
    'calcular_distribucion_metodo_tiempo_retorno',
    'calcular_distribucion_metodo_autovalores_gpu',
    'calcular_distribucion_metodo_tiempo_retorno_gpu',
    'crear_matriz_probabilidad_gpu',
    'GPU_AVAILABLE',
    'get_gpu_info',
    'clear_gpu_memory',
    'optimal_gpu_method',
    'benchmark_gpu_vs_cpu'
]