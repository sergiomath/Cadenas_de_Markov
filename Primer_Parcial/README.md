# Primer Parcial (25%)

**Fecha:** Lunes 6 de octubre

## Contenido

Este parcial incluye el análisis comparativo de dos métodos para calcular distribuciones estacionarias en cadenas de Markov:

1. **Método 1:** Vectores propios (O(n³))
2. **Método 2:** Tiempos medios de retorno (O(n⁴))

## Estructura

- **[src/](src/)**: Implementaciones CPU/GPU de ambos métodos
- **[notebooks/](notebooks/)**: Análisis de rendimiento y benchmarks
- **[resultados/](resultados/)**: Datos experimentales en formato CSV
- **[docs/](docs/)**: Descripción original de la tarea
- **[Tareas/](Tareas/)**: Tareas optativas (Tarea 0, Tarea 0.1)

## Resultados Principales

| Métrica | Método 1 | Método 2 |
|---------|----------|----------|
| **Complejidad** | O(n³) | O(n⁴) |
| **Speedup GPU** | 10-30x (n>200) | 1.2-2x |
| **Recomendación** | GPU para n>50 | CPU siempre |

## Uso

Desde la raíz del proyecto:

```python
import sys
sys.path.append('Primer_Parcial')
from src.markov_matrix import *

P = crear_matriz_probabilidad(n=100, p=0.7)
pi = calcular_distribucion_metodo_autovalores(P)
```
