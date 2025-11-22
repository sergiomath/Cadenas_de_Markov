# Análisis Computacional de Cadenas de Markov

**Universidad Nacional de Colombia**
**Autor:** Sergio Andrés Díaz Vera , Mateo 
		

## Descripción del Problema

Para una cadena de Markov irreducible con matriz de transición **P** y conjunto finito de estados **S = {1, 2, ..., k}**, existe una única distribución estacionaria **π**. Este proyecto compara la eficiencia computacional de dos métodos fundamentales para calcular π:

### Método 1: Vectores Propios
Utiliza la definición **πP = π**. La distribución estacionaria π es el único vector propio asociado al valor propio λ=1, normalizado para que sus componentes sumen 1.

**Complejidad:** O(n³)

### Método 2: Tiempos Medios de Retorno
Denotando r_i = E[T_i] (tiempo medio de retorno al estado i), se calcula:

**π = (1/r₁, 1/r₂, ..., 1/rₖ)**

donde r_i se obtiene resolviendo sistemas lineales basados en:
- t_{ij} = 0 si i=j
- t_{ij} = 1 + Σ P_{ix} t_{xj} si i≠j

**Complejidad:** O(n⁴)

## Preguntas de Investigación

1. ¿Cuál de los dos métodos es más eficiente?
2. ¿Qué tan más eficiente es un método comparado con el otro?
3. ¿Siempre un método le gana al otro en eficiencia o depende de la cadena?

## Metodología

### Cadena de Markov Analizada

Random walk modificado con n estados y probabilidad de avance p:

```
Estado 0:    P(0→0)=1-p,  P(0→1)=p
Estado i:    P(i→i+1)=p,  P(i→i-1)=1-p  (1≤i<n-1)
Estado n-1:  P(n-1→n-1)=p, P(n-1→n-2)=1-p
```

### Parámetros de Experimentación

- **n (estados):** 1 a 999
- **p (probabilidad):** {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9}
- **Total experimentos:** 8,991 por método
- **Hardware:** CPU y GPU (NVIDIA CUDA)

## Resultados Principales

| Métrica | Método 1 (Vectores Propios) | Método 2 (Tiempo Retorno) |
|---------|------------------------------|---------------------------|
| **Complejidad** | O(n³) | O(n⁴) |
| **Speedup GPU** | 10-30x (n>200) | 1.2-2x |
| **Paralelización** | Excelente | Limitada |
| **Estabilidad** | Alta | Media |
| **Recomendación** | GPU para n>50 | CPU siempre |

### Conclusión

**El Método 1 (Vectores Propios) es superior en eficiencia para la mayoría de casos**, especialmente con aceleración GPU. El Método 2 solo es competitivo para matrices muy pequeñas (n<20).

## Instalación Paso a Paso

### Prerequisitos

- **Python 3.8 o superior** - Verificar versión:
  ```bash
  python --version
  ```

- **Git** (para clonar el repositorio):
  ```bash
  git --version
  ```

- **GPU NVIDIA con CUDA** (opcional, para aceleración):
  ```bash
  nvidia-smi  # Verificar GPU disponible
  ```

---

### Opción 1: Instalación con UV (Recomendado)

UV es un manejador de paquetes moderno, más rápido que pip tradicional.

#### Paso 1: Instalar UV

**Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell como Administrador):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternativa multiplataforma (con pip):**
```bash
pip install uv
```

**Verificar instalación:**
```bash
uv --version
```

#### Paso 2: Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd Cadenas_de_Markov
```

#### Paso 3: Instalar Dependencias

**Solo CPU (suficiente para la mayoría de casos):**
```bash
uv sync
```

**Con soporte GPU (requiere CUDA 12.x):**
```bash
uv sync --extra gpu
```

**Con soporte GPU (CUDA 11.x):**
```bash
uv sync --extra gpu-cuda11
```

**Nota:** UV creará automáticamente un entorno virtual en `.venv/`

#### Paso 4: Verificar Instalación

```bash
uv run python -c "
import sys
sys.path.append('Primer_Parcial')
from src.markov_matrix import *
P = crear_matriz_probabilidad(5, 0.7)
pi = calcular_distribucion_metodo_autovalores(P)
print(f'✅ Instalación exitosa - Suma π: {pi.sum():.10f}')
"
```

**Salida esperada:** `✅ Instalación exitosa - Suma π: 1.0000000000`

---

### Opción 2: Instalación Legacy con pip

Si prefieres usar pip tradicional o tienes problemas con UV:

#### Paso 1: Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd Cadenas_de_Markov
```

#### Paso 2: Crear Entorno Virtual (Recomendado)

**Linux/macOS:**
```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Paso 3: Instalar Dependencias

**Solo CPU:**
```bash
pip install -r requirements.txt
```

**Con soporte GPU (CUDA 12.x):**
```bash
pip install -r requirements.txt
pip install cupy-cuda12x
```

**Con soporte GPU (CUDA 11.x):**
```bash
pip install -r requirements.txt
pip install cupy-cuda11x
```

#### Paso 4: Verificar Instalación

```bash
python -c "
import sys
sys.path.append('Primer_Parcial')
from src.markov_matrix import *
P = crear_matriz_probabilidad(5, 0.7)
pi = calcular_distribucion_metodo_autovalores(P)
print(f'✅ Instalación exitosa - Suma π: {pi.sum():.10f}')
"
```

---

### Verificación Completa de GPU (Opcional)

Si instalaste soporte GPU, verifica que funcione correctamente:

```bash
# Verificar GPU detectada
nvidia-smi

# Test GPU con el proyecto
uv run python -c "
import sys
sys.path.append('Primer_Parcial')
from src.markov_matrix import *

info = get_gpu_info()
if info['available']:
    print(f\"✅ GPU detectada: {info['name']}\")
    print(f\"   Memoria: {info['memory_total']:.2f} GB\")

    # Test rápido
    P = crear_matriz_probabilidad(100, 0.7)
    pi = calcular_distribucion_metodo_autovalores_gpu(P)
    print(f\"✅ Cálculo GPU exitoso - Suma π: {pi.sum():.10f}\")
else:
    print('❌ GPU no disponible')
"
```

---

### Solución de Problemas Comunes

**Problema: `ModuleNotFoundError: No module named 'cupy'`**
- Solución: Instalar CuPy según tu versión de CUDA (ver arriba)

**Problema: UV no reconocido en terminal**
- Solución: Reiniciar terminal o agregar UV al PATH manualmente
- Linux/macOS: `export PATH="$HOME/.cargo/bin:$PATH"`

**Problema: GPU no detectada**
- Verificar drivers NVIDIA: `nvidia-smi`
- Verificar versión CUDA: `nvcc --version`
- Instalar CuPy compatible con tu versión de CUDA

**Problema: Tests fallan con error de suma ≠ 1.0**
- Normal si la diferencia es < 1e-10 (error numérico)
- Si diferencia > 1e-6, verificar instalación de NumPy/SciPy

## Uso

### Activar Entorno Virtual

```bash
# UV crea automáticamente un entorno virtual en .venv/
# Activarlo manualmente si es necesario:

# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate

# O usar uv run para ejecutar comandos directamente
uv run python script.py
uv run jupyter notebook
```

### Ejemplo Básico

```python
# Agregar ruta del Primer Parcial al path
import sys
sys.path.append('Primer_Parcial')

from src.markov_matrix import crear_matriz_probabilidad, calcular_distribucion_metodo_autovalores

# Crear matriz de transición
P = crear_matriz_probabilidad(n=100, p=0.7)

# Calcular distribución estacionaria
pi = calcular_distribucion_metodo_autovalores(P)

# Validar
print(f"Suma: {pi.sum():.10f}")  # Debe ser 1.0
```

### Comparación de Métodos

```python
from src.markov_matrix import *
import time

P = crear_matriz_probabilidad(n=200, p=0.6)

# Método 1
t1 = time.time()
pi1 = calcular_distribucion_metodo_autovalores(P)
tiempo1 = time.time() - t1

# Método 2
t2 = time.time()
pi2 = calcular_distribucion_metodo_tiempo_retorno(P)
tiempo2 = time.time() - t2

print(f"Método 1: {tiempo1:.4f}s")
print(f"Método 2: {tiempo2:.4f}s")
print(f"Speedup: {tiempo2/tiempo1:.2f}x")
```

### Uso con GPU

```python
from src.markov_matrix import *

# Verificar GPU
info = get_gpu_info()
if info['available']:
    print(f"GPU: {info['name']}")

    # Usar GPU
    P = crear_matriz_probabilidad(n=500, p=0.6)
    pi = calcular_distribucion_metodo_autovalores_gpu(P)

    # Liberar memoria
    clear_gpu_memory()
else:
    print("GPU no disponible")
```

### Recomendación Automática

```python
from src.markov_matrix import recomendar_metodo

recomendacion = recomendar_metodo(n=500)
print(recomendacion)
# {'metodo1': 'GPU', 'metodo2': 'CPU'}
```

## Estructura del Proyecto

```
Cadenas_de_Markov/
├── Primer_Parcial/               # Primer Parcial (25%)
│   ├── src/
│   │   ├── __init__.py
│   │   └── markov_matrix.py      # Implementaciones CPU/GPU
│   ├── notebooks/
│   │   ├── metodo_vectores_propios.ipynb
│   │   ├── metodo_sistema.ipynb
│   │   └── metodo_gpu_final.ipynb
│   ├── resultados/               # Datos de benchmarks
│   ├── docs/
│   │   └── Descripcion tarea 0 (1).pdf
│   └── Tareas/                   # Tareas optativas (0, 0.1)
├── Tareas/                       # Tareas del curso (30% total)
│   ├── Tarea_1/                  # 10%
│   ├── Tarea_2/                  # 10%
│   └── Tarea_3/                  # 10%
├── Proyecto/                     # Proyecto Final (20%)
│   ├── documento_escrito/        # 10%
│   └── video/                    # 10%
├── requirements.txt
├── CLAUDE.md
├── ESTRUCTURA_PROYECTO.md
└── README.md

Nota: El Segundo Parcial (25%) será agregado cuando esté disponible.
```

## Notebooks de Análisis

Los notebooks se ejecutan con:

```bash
# Usando UV
uv run jupyter notebook Primer_Parcial/notebooks/

# O activando el entorno virtual
source .venv/bin/activate  # Linux/macOS
jupyter notebook Primer_Parcial/notebooks/
```

### 1. metodo_vectores_propios.ipynb
Benchmark completo del Método 1 (Vectores Propios) variando n y p.

### 2. metodo_sistema.ipynb
Benchmark completo del Método 2 (Tiempos de Retorno) variando n y p.

### 3. metodo_gpu_final.ipynb
Comparación GPU vs CPU para ambos métodos con análisis de speedup.

## Validación de Instalación

```bash
# Ejecutar validación con UV
uv run python -c "
import sys
sys.path.append('Primer_Parcial')
from src.markov_matrix import *

# Test matriz pequeña
P = crear_matriz_probabilidad(5, 0.7)
assert P.shape == (5, 5)
assert abs(P.sum(axis=1).sum() - 5.0) < 1e-10

# Test Método 1
pi1 = calcular_distribucion_metodo_autovalores(P)
assert abs(pi1.sum() - 1.0) < 1e-10

# Test Método 2
pi2 = calcular_distribucion_metodo_tiempo_retorno(P)
assert abs(pi2.sum() - 1.0) < 1e-10

# Test GPU (si disponible)
if GPU_AVAILABLE:
    pi1_gpu = calcular_distribucion_metodo_autovalores_gpu(P)
    assert abs(pi1_gpu.sum() - 1.0) < 1e-10
    print('✅ GPU funcional')

print('✅ Todos los tests pasaron')
"
```

## Referencias

1. Norris, J.R. (1997). *Markov Chains*. Cambridge University Press.
2. Levin, D.A., Peres, Y. (2017). *Markov Chains and Mixing Times*. AMS.
3. Stewart, W.J. (2009). *Probability, Markov Chains, Queues, and Simulation*. Princeton UP.

## Comandos Útiles con UV

```bash
# Instalar nuevas dependencias
uv add numpy pandas

# Actualizar dependencias
uv sync --upgrade

# Ver dependencias instaladas
uv pip list

# Limpiar caché
uv cache clean

# Ejecutar scripts Python
uv run python mi_script.py

# Ejecutar Jupyter
uv run jupyter notebook

# Ver información del proyecto
uv tree
```

## Recomendaciones de Uso

1. **Usar Método 1 por defecto** - Superior en 95% de casos
2. **Activar GPU solo si n>50** - Overhead no justifica en matrices pequeñas
3. **Evitar Método 2 para n>200** - Escalabilidad pobre (O(n⁴))
4. **Validar resultados** - Verificar Σπᵢ = 1 siempre
5. **Usar UV para gestión de dependencias** - Más rápido y confiable que pip

## Licencia

Proyecto académico - Universidad Nacional de Colombia

**Citar como:**
```Análisis Computacional de Cadenas de Markov.
Universidad Nacional de Colombia.
```
