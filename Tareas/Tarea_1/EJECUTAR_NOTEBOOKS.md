# Guía para Ejecutar los Notebooks

## Requisitos Previos

### Opción 1: Usar UV (Recomendado)

Desde la raíz del proyecto (`Cadenas_de_Markov/`):

```bash
# Asegurarse de que UV esté instalado
uv --version

# Sincronizar dependencias
uv sync

# Lanzar Jupyter
uv run jupyter notebook Tareas/Tarea_1/
```

### Opción 2: Usar pip + virtualenv

Desde la raíz del proyecto:

```bash
# Crear entorno virtual
python3 -m venv .venv

# Activar entorno virtual
source .venv/bin/activate  # Linux/macOS
# o
.venv\Scripts\activate     # Windows

# Instalar dependencias
pip install numpy matplotlib jupyter

# Lanzar Jupyter
jupyter notebook Tareas/Tarea_1/
```

## Notebooks Disponibles

### 1. ejercicio_1a.ipynb - Modelo Hard-Core

**Contenido:**
- Implementación del Gibbs Sampler para Hard-Core
- Análisis de convergencia con diferentes valores de T
- Generación de múltiples muestras independientes
- Distribución del número de partículas

**Orden de ejecución:** Ejecutar todas las celdas en orden (Run All)

**Tiempo estimado:** ~1-2 minutos

### 2. ejercicio_1b.ipynb - Estimación del Número de Partículas

**Contenido:**
- Análisis sistemático para múltiples tamaños K
- Estudio de escalamiento (μ vs K²)
- Histogramas por tamaño
- Análisis detallado de convergencia variando T

**Orden de ejecución:** Ejecutar todas las celdas en orden

**Tiempo estimado:** ~3-5 minutos (genera 100 muestras por cada K)

**Nota:** Este notebook puede tardar más debido al análisis extensivo.

### 3. ejercicio_2.ipynb - Modelo de q-Coloraciones

**Contenido:**
- Implementación del Gibbs Sampler para q-coloraciones
- Análisis de convergencia
- Múltiples muestras independientes
- Distribución de colores y uniformidad
- Comparación para diferentes valores de q

**Orden de ejecución:** Ejecutar todas las celdas en orden

**Tiempo estimado:** ~2-3 minutos

## Estructura del Código

Los notebooks importan funciones de los módulos en `src/`:

```
Tareas/Tarea_1/
├── src/
│   ├── __init__.py           # Exporta todas las funciones
│   ├── hard_core.py          # Gibbs Sampler Hard-Core
│   ├── q_coloraciones.py     # Gibbs Sampler q-coloraciones
│   ├── estadisticas.py       # Análisis estadístico
│   └── visualizacion.py      # Funciones de gráficos
├── ejercicio_1a.ipynb
├── ejercicio_1b.ipynb
└── ejercicio_2.ipynb
```

## Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'src'"

**Solución:** Los notebooks ya incluyen `sys.path.append('.')` en la primera celda. Asegúrate de ejecutar esa celda primero.

### Error: "ModuleNotFoundError: No module named 'numpy'"

**Solución:** Instalar dependencias:
```bash
uv sync  # Si usas UV
# o
pip install numpy matplotlib  # Si usas pip
```

### Error: "ImportError: libscipy_openblas64"

**Solución (WSL/Linux):**
```bash
sudo apt-get update
sudo apt-get install libopenblas-dev
```

### Los gráficos no se muestran

**Solución:** Asegúrate de que la primera celda de imports incluya:
```python
%matplotlib inline
```

Esto ya está incluido en los notebooks.

## Verificación

Para verificar que todo esté funcionando correctamente sin ejecutar los notebooks completos:

```bash
# Verificar sintaxis de los módulos Python
cd Tareas/Tarea_1/src
python3 -m py_compile *.py
echo "✓ Todos los módulos tienen sintaxis correcta"

# Verificar estructura de notebooks
cd ..
python3 << 'EOF'
import json
for nb in ['ejercicio_1a.ipynb', 'ejercicio_1b.ipynb', 'ejercicio_2.ipynb']:
    with open(nb) as f:
        data = json.load(f)
    print(f"✓ {nb}: {len(data['cells'])} celdas")
EOF
```

## Resultados Esperados

### ejercicio_1a.ipynb
- Visualizaciones de configuraciones Hard-Core
- Evolución de la cadena en diferentes tiempos
- Histograma de distribución de partículas
- Media ≈ 25 partículas para K=10, T=10000

### ejercicio_1b.ipynb
- Tabla de estadísticas para K ∈ {3, 5, 7, 10, 12, 15, 20}
- Gráfico de escalamiento mostrando μ ∝ K²
- Densidad límite ρ ≈ 0.234
- Histogramas de convergencia

### ejercicio_2.ipynb
- Visualizaciones de q-coloraciones con diferentes colores
- Distribución uniforme de colores
- Comparación para q = 2, 3, 4, 5
- Varianza decreciente con q creciente

## Notas Adicionales

- Todos los notebooks usan semillas aleatorias fijas para reproducibilidad
- Los resultados pueden variar ligeramente debido a la naturaleza estocástica del algoritmo
- Las figuras generadas pueden guardarse usando el botón "Save" en las ventanas de matplotlib
- Los notebooks están diseñados para ejecutarse desde el directorio `Tareas/Tarea_1/`
