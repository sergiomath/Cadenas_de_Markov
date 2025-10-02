# CLAUDE.md

Documentación técnica para Claude Code trabajando en este proyecto.

## Arquitectura

Proyecto Python para análisis comparativo de métodos de cálculo de distribuciones estacionarias en cadenas de Markov.

### Estructura de Archivos

- **`src/markov_matrix.py`**: Módulo principal con implementaciones CPU/GPU
  - `crear_matriz_probabilidad(n, p)`: Crea matriz de transición
  - `calcular_distribucion_metodo_autovalores(matriz)`: Método 1 (Vectores propios)
  - `calcular_distribucion_metodo_tiempo_retorno(matriz)`: Método 2 (Tiempos de retorno)
  - `calcular_distribucion_metodo_autovalores_gpu(matriz)`: Método 1 GPU
  - `calcular_distribucion_metodo_tiempo_retorno_gpu(matriz)`: Método 2 GPU

- **`src/__init__.py`**: Exporta funciones principales

- **`notebooks/`**: Análisis de rendimiento y benchmarks
  - `metodo_vectores_propios.ipynb`: Benchmark Método 1
  - `metodo_sistema.ipynb`: Benchmark Método 2
  - `metodo_gpu_final.ipynb`: Comparación GPU vs CPU

- **`resultados/`**: CSVs con datos de benchmarks

- **`docs/`**: Documento con descripción de la tarea original

## Lógica del Modelo

### Matriz de Transición
`crear_matriz_probabilidad(n, p)` genera matrices con estructura:
- **Estado 0**: probabilidad `p` avanzar, `1-p` quedarse
- **Estados intermedios**: probabilidad `p` avanzar, `1-p` retroceder
- **Estado n-1**: probabilidad `p` quedarse, `1-p` retroceder

### Métodos de Cálculo

**Método 1 (O(n³)):** Resuelve πP = π mediante eigendecomposición
**Método 2 (O(n⁴)):** Calcula πᵢ = 1/E[Tᵢ] resolviendo n sistemas lineales

## Comandos de Desarrollo

### Instalación
```bash
pip install -r requirements.txt

# GPU (opcional)
pip install cupy-cuda12x  # CUDA 12.x
pip install cupy-cuda11x  # CUDA 11.x
```

### Ejecución
```bash
# Notebooks
jupyter notebook notebooks/

# Tests
python -c "from src.markov_matrix import *; P = crear_matriz_probabilidad(5, 0.7); print(calcular_distribucion_metodo_autovalores(P))"
```

### Patrón de Importación
```python
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.markov_matrix import *
```

## Instrucciones para Claude Code

Estas instrucciones aplican a TODAS las interacciones con Claude Code en este proyecto:

### Estilo de Comunicación
- **Idioma**: Español siempre
- **Tono**: Profesional, conciso, académico
- **Documentación**: Docstrings en español con rigor matemático

### Preferencias de Código
- **Comentarios**: Mínimos y esenciales
- **Variables**: Nombres descriptivos en español donde sea apropiado
- **Simplicidad**: Código limpio sin prints excesivos

### Manejo de Tareas
- **Verificación**: Validar resultados antes de reportar completitud
- **Testing**: Ejecutar tests al modificar funciones críticas
- **Documentación**: Actualizar CLAUDE.md al agregar features

### Contexto del Proyecto
- Proyecto académico para comparación algorítmica
- Benchmarking de rendimiento es crítico
- Resultados deben ser reproducibles
- Orientado a análisis cuantitativo de eficiencia computacional

### Perfil: Sergio Andrés Díaz Vera
Actuario y Científico de Datos colombiano con experiencia en sector asegurador.

#### Generación de Documentación Técnica

1. **Objetivos**: Definir claramente objetivo y criterios de éxito
2. **Procesos**: Documentar detalladamente con herramientas y métodos
3. **Resultados**: Cuantificar siempre con métricas e indicadores claros
4. **Hallazgos**: Resumir con aplicabilidad y relevancia estratégica
5. **Comunicación**: Traducir complejidad técnica a explicaciones claras
6. **Transparencia**: Documentar supuestos, fuentes y limitaciones

#### Valores
- Rigor técnico accesible
- Reproducibilidad total
- Impacto medible
- Transparencia en supuestos
- Documentación para transferencia de conocimiento