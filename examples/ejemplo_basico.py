"""
Ejemplo básico de uso de las funciones de Cadenas de Markov
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.markov_matrix import crear_matriz_probabilidad
import numpy as np

# Parámetros
n = 5  # número de estados
p = 0.7  # probabilidad de transición

# Crear matriz de probabilidad
matriz = crear_matriz_probabilidad(n, p)

print("Matriz de Probabilidad:")
print(matriz)
print()
print(f"Suma de cada fila: {matriz.sum(axis=1)}")