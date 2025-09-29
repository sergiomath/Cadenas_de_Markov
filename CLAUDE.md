# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Architecture Overview

This is a Python project for Markov chain analysis with the following key structure:

- **`src/markov_matrix.py`**: Core module containing:
  - `crear_matriz_probabilidad(n, p)`: Creates transition probability matrices
  - `calcular_distribucion_metodo_autovalores(matriz)`: Método 1 - Vectores propios (CPU)
  - `calcular_distribucion_metodo_tiempo_retorno(matriz)`: Método 2 - Tiempo medio de retorno (CPU)
  - `calcular_distribucion_metodo_autovalores_gpu(matriz)`: Método 1 - Versión GPU
  - `calcular_distribucion_metodo_tiempo_retorno_gpu(matriz)`: Método 2 - Versión GPU

- **`src/__init__.py`**: Package initialization that exports the main functions

- **`notebooks/metodo_vectores_propios.ipynb`**: Análisis de rendimiento Método 1 (vectores propios)
- **`notebooks/metodo_sistema.ipynb`**: Análisis de rendimiento Método 2 (tiempo de retorno)
- **`notebooks/gpu_benchmark.ipynb`**: Comparación CPU vs GPU

- **`examples/ejemplo_basico.py`**: Uso básico del Método 1
- **`examples/ejemplo_metodo_sistema.py`**: Uso básico del Método 2
- **`examples/benchmark_cpu_vs_gpu.py`**: Benchmark completo CPU vs GPU

## Key Design Patterns

### Matrix Generation Logic
The `crear_matriz_probabilidad(n, p)` function creates matrices with asymmetric transition rules:
- **Initial state (0)**: probability `p` to advance, `1-p` to stay
- **Intermediate states**: probability `p` to advance, `1-p` to retreat
- **Final state (n-1)**: probability `p` to stay, `1-p` to retreat

### Eigenvector Normalization
The `calcular_vector_propio_dominante()` function normalizes eigenvectors so their components sum to 1, treating them as probability distributions.

## Development Commands

### Running Examples
```bash
# Basic example
python examples/ejemplo_basico.py

# Interactive analysis
jupyter notebook notebooks/methods.ipynb
```

### Installing Dependencies
```bash
pip install -r requirements.txt

# Para aceleración GPU (opcional):
pip install cupy-cuda11x  # para CUDA 11.x
pip install cupy-cuda12x  # para CUDA 12.x
```

### Module Import Pattern
When working in notebooks or scripts, use:
```python
import sys
import os
sys.path.append(os.path.join(os.path.dirname('__file__'), '..'))
from src.markov_matrix import crear_matriz_probabilidad, calcular_vector_propio_dominante
```

## Working with the Notebooks

The `methods.ipynb` notebook demonstrates:
- Matrix creation with different parameters (n, p)
- Eigenvalue/eigenvector analysis
- Eigenvector normalization and sum verification
- Tabular presentation using pandas DataFrames

When modifying notebook imports, ensure the sys.path modification points to the project root to access the `src/` module.