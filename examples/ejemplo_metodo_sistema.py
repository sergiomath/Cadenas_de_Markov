"""
Ejemplo básico del Método 2: Tiempo Medio de Retorno

Este script demuestra cómo usar el método 2 para calcular la distribución
estacionaria de una cadena de Markov usando tiempos medios de retorno.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.markov_matrix import crear_matriz_probabilidad, calcular_distribucion_metodo_tiempo_retorno
import numpy as np

def ejemplo_basico():
    """Ejemplo básico usando método 2 (tiempo medio de retorno)"""

    print("=== Método 2: Tiempo Medio de Retorno ===\n")

    # Parámetros
    n = 5  # número de estados
    p = 0.7  # probabilidad de avance

    print(f"Parámetros:")
    print(f"• Número de estados: {n}")
    print(f"• Probabilidad de avance: {p}")
    print(f"• Probabilidad de retroceso: {1-p}")

    # Crear matriz de transición
    matriz = crear_matriz_probabilidad(n, p)

    print(f"\nMatriz de transición P:")
    for i, fila in enumerate(matriz):
        print(f"Estado {i}: {fila}")

    # Calcular distribución estacionaria usando método 2 (tiempo de retorno)
    pi = calcular_distribucion_metodo_tiempo_retorno(matriz)

    print(f"\nDistribución estacionaria π (πᵢ = 1/E[Tᵢ]):")
    print(f"π = {pi}")
    print(f"Suma de componentes: {np.sum(pi):.6f}")

    # Calcular y mostrar los tiempos medios de retorno
    tiempos_retorno = 1.0 / pi
    print(f"\nTiempos medios de retorno E[Tᵢ]:")
    for i, tiempo in enumerate(tiempos_retorno):
        print(f"Estado {i}: E[T{i}] = {tiempo:.4f}")

    # Verificar que πP = π
    verificacion = pi @ matriz
    error = np.linalg.norm(pi - verificacion)

    print(f"\nVerificación πP = π:")
    print(f"πP = {verificacion}")
    print(f"Error ||π - πP||: {error:.2e}")

    return pi, matriz

def comparar_con_metodo_1():
    """Comparar resultados con método 1 (vectores propios)"""

    print("\n" + "="*50)
    print("COMPARACIÓN ENTRE MÉTODOS")
    print("="*50)

    from src.markov_matrix import calcular_distribucion_metodo_autovalores

    # Parámetros
    n = 4
    p = 0.6

    # Crear matriz
    matriz = crear_matriz_probabilidad(n, p)

    # Método 1: Vectores propios
    pi1 = calcular_distribucion_metodo_autovalores(matriz)

    # Método 2: Tiempo medio de retorno
    pi2 = calcular_distribucion_metodo_tiempo_retorno(matriz)

    print(f"\nPara n={n}, p={p}:")
    print(f"Método 1 (vectores propios):      {pi1}")
    print(f"Método 2 (tiempo de retorno):     {pi2}")
    print(f"Diferencia absoluta máxima:       {np.max(np.abs(pi1 - pi2)):.2e}")

    # Mostrar interpretación del tiempo de retorno
    tiempos_retorno = 1.0 / pi2
    print(f"\nInterpretación física (Método 2):")
    for i, tiempo in enumerate(tiempos_retorno):
        print(f"Estado {i}: visitas promedio cada {tiempo:.2f} pasos")

if __name__ == "__main__":
    # Ejecutar ejemplo básico
    ejemplo_basico()

    # Comparar métodos
    comparar_con_metodo_1()