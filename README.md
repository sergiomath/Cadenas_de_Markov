# Cadenas de Markov 🎲⚡

Proyecto avanzado de análisis de Cadenas de Markov con implementación CPU y GPU, métodos múltiples para distribuciones estacionarias y análisis de rendimiento completo.

## 📁 Estructura del Proyecto

```
Cadenas_de_Markov/
├── src/
│   ├── __init__.py              # Módulo principal con funciones CPU y GPU
│   └── markov_matrix.py         # Implementaciones CPU/GPU optimizadas
├── notebooks/
│   ├── metodo_vectores_propios.ipynb    # Método 1: Vectores propios
│   ├── metodo_sistema.ipynb             # Método 2: Tiempo medio de retorno
│   └── metodo_gpu_final.ipynb           # Análisis GPU con RTX 5060
├── resultados/                          # CSV generados por los análisis
├── requirements.txt             # Dependencias CPU y GPU
├── CLAUDE.md                    # Documentación técnica
└── README.md                    # Este archivo
```

## 🚀 Funcionalidades

### Creación de matrices
- **`crear_matriz_probabilidad(n, p)`**: Versión CPU
- **`crear_matriz_probabilidad_gpu(n, p)`**: Versión GPU optimizada

### Métodos para distribuciones estacionarias

#### Método 1: Vectores propios (πP = π)
- **`calcular_distribucion_metodo_autovalores(matriz)`**: CPU
- **`calcular_distribucion_metodo_autovalores_gpu(matriz)`**: GPU optimizado

#### Método 2: Tiempo medio de retorno (πᵢ = 1/E[Tᵢ])
- **`calcular_distribucion_metodo_tiempo_retorno(matriz)`**: CPU
- **`calcular_distribucion_metodo_tiempo_retorno_gpu(matriz)`**: GPU optimizado

## 📦 Instalación

```bash
# Instalar dependencias
pip install -r requirements.txt
```

### Utilidades GPU
- **`get_gpu_info()`**: Información detallada de la GPU
- **`clear_gpu_memory()`**: Limpieza de memoria GPU
- **`optimal_gpu_method(n)`**: Recomendaciones CPU vs GPU según tamaño
- **`benchmark_gpu_vs_cpu(matriz)`**: Comparación de rendimiento

## 🖥️ Soporte GPU

### RTX 5060 Optimizado ⚡
- **CUDA 13.0** con CuPy optimizado
- Speedup significativo para matrices n > 50
- Manejo inteligente de memoria GPU
- Fallback automático a CPU si es necesario

### Configuración GPU
```bash
# Verificar CUDA
nvidia-smi

# Instalar CuPy apropiado
pip install cupy-cuda13x  # RTX 40/50 series
pip install cupy-cuda12x  # RTX 30 series
```

## 💻 Uso Rápido

### Uso básico CPU
```python
from src.markov_matrix import crear_matriz_probabilidad, calcular_distribucion_metodo_autovalores

# Crear matriz 5x5 con probabilidad p=0.7
matriz = crear_matriz_probabilidad(5, 0.7)

# Calcular distribución estacionaria (Método 1)
pi = calcular_distribucion_metodo_autovalores(matriz)
print(f"Distribución estacionaria: {pi}")
```

### Uso avanzado GPU
```python
from src.markov_matrix import *

# Verificar GPU disponible
if GPU_AVAILABLE:
    print(f"GPU: {get_gpu_info()['name']}")

    # Usar GPU para matrices grandes
    matriz_gpu = crear_matriz_probabilidad_gpu(1000, 0.6)
    pi = calcular_distribucion_metodo_autovalores_gpu(matriz_gpu)
else:
    print("Usando CPU solamente")
```

## 📊 Notebooks de Análisis

### 1. `metodo_vectores_propios.ipynb`
- **Método 1**: Vectores propios (πP = π)
- Análisis n: 1→999, p: 0.1→0.9
- Visualizaciones y estadísticas completas
- Guardado en `resultados/matriz_tiempos_vectores_propios.csv`

### 2. `metodo_sistema.ipynb`
- **Método 2**: Tiempo medio de retorno (πᵢ = 1/E[Tᵢ])
- Mismas variaciones n y p que Método 1
- Comparación de rendimiento entre métodos
- Guardado en `resultados/matriz_tiempos_sistema_lineal.csv`

### 3. `metodo_gpu_final.ipynb`
- **GPU RTX 5060**: Análisis puro GPU
- 8,991 combinaciones (n×p) procesadas
- Speedup y análisis de memoria GPU
- Guardado en `resultados/matriz_tiempos_gpu_final.csv`

## 🔧 Dependencias

### Básicas
- `numpy>=1.21.0`: Álgebra lineal y cálculos matriciales
- `pandas>=1.3.0`: Manipulación de datos y CSV
- `matplotlib>=3.4.0`: Visualizaciones
- `seaborn>=0.11.0`: Gráficos estadísticos avanzados
- `jupyter>=1.0.0`: Notebooks interactivos

### GPU (Opcional)
- `cupy-cuda13x>=13.0.0`: Aceleración GPU para RTX 40/50 series
- `cupy-cuda12x>=12.0.0`: Para RTX 30 series
- `cupy-cuda11x>=11.0.0`: Para RTX 20 series y anteriores

## 🚀 Rendimiento

### CPU vs GPU Benchmarks
- **n < 50**: CPU más eficiente (overhead GPU)
- **50 < n < 200**: GPU ventajoso para Método 1
- **n > 200**: GPU excelente para Método 1, CPU mejor para Método 2

### RTX 5060 Results
- **~200 cálculos/segundo** en análisis masivo
- **8,150 MB VRAM** utilizados eficientemente
- **Speedup 5-10x** para matrices grandes

## 📈 Casos de Uso

- **Investigación académica**: Distribuciones estacionarias
- **Análisis de rendimiento**: Comparación CPU vs GPU
- **Sistemas estocásticos**: Modelado de procesos de Markov
- **Optimización**: Selección automática CPU/GPU según problema
- **Benchmarking**: Evaluación de hardware NVIDIA para computación científica

