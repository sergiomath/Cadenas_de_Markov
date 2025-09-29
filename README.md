# Cadenas de Markov 🎲

Proyecto de implementación y análisis de Cadenas de Markov en Python, con funcionalidades para crear matrices de probabilidad y analizar vectores propios.

## 📁 Estructura del Proyecto

```
Cadenas_de_Markov/
├── src/
│   ├── __init__.py              # Módulo principal
│   └── markov_matrix.py         # Funciones de matrices de Markov
├── notebooks/
│   └── methods.ipynb            # Análisis interactivo y pruebas
├── examples/
│   └── ejemplo_basico.py        # Ejemplo de uso básico
├── docs/
│   └── README_PROYECTO.md       # Documentación detallada
├── tests/                       # Tests unitarios (por implementar)
├── requirements.txt             # Dependencias
└── README.md                    # Este archivo
```

## 🚀 Funcionalidades

### `crear_matriz_probabilidad(n, p)`
Crea una matriz de transición de Markov con características específicas:

- **Estado inicial (0)**:
  - Probabilidad `p` de avanzar al estado 1
  - Probabilidad `1-p` de quedarse en el mismo estado

- **Estados intermedios (1 a n-2)**:
  - Probabilidad `p` de avanzar al siguiente estado
  - Probabilidad `1-p` de retroceder al estado anterior

- **Estado final (n-1)**:
  - Probabilidad `p` de quedarse en el mismo estado
  - Probabilidad `1-p` de retroceder al estado anterior

### `calcular_vector_propio_dominante(matriz)`
- Calcula todos los valores y vectores propios de la matriz
- Identifica el vector propio asociado al valor propio de mayor magnitud
- Retorna el vector normalizado (suma de componentes = 1)

## 📦 Instalación

```bash
# Instalar dependencias
pip install -r requirements.txt
```

## 💻 Uso Rápido

```python
from src.markov_matrix import crear_matriz_probabilidad, calcular_vector_propio_dominante
import numpy as np

# Crear matriz 5x5 con probabilidad p=0.7
matriz = crear_matriz_probabilidad(5, 0.7)

# Calcular vector propio dominante
vector = calcular_vector_propio_dominante(matriz)

print(f"Vector propio dominante: {vector}")
```

## 📊 Ejemplos Incluidos

1. **`examples/ejemplo_basico.py`**: Implementación básica con matriz 5x5
2. **`notebooks/methods.ipynb`**: Análisis completo incluyendo:
   - Creación de matrices de diferentes tamaños
   - Cálculo de todos los vectores propios
   - Normalización y análisis de sumas
   - Tablas comparativas

## 🔧 Dependencias

- `numpy`: Cálculos matriciales y álgebra lineal
- `pandas`: Manipulación de datos y tablas
- `matplotlib`: Visualización de datos
- `jupyter`: Notebooks interactivos

## 🧮 Ejemplo de Salida

Para una matriz 5x5 con p=0.7:
```
Matriz de Probabilidad:
[[0.3 0.7 0.  0.  0. ]
 [0.3 0.  0.7 0.  0. ]
 [0.  0.3 0.  0.7 0. ]
 [0.  0.  0.3 0.  0.7]
 [0.  0.  0.  0.3 0.7]]

Vector Propio Dominante: [0.1 0.1 0.1 0.1 0.6]
```

## 📈 Casos de Uso

- Análisis de sistemas estocásticos
- Modelado de procesos de Markov
- Estudio de distribuciones estacionarias
- Investigación en teoría de probabilidades

