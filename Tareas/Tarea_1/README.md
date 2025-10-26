# Tarea 1 (10%)

**Estudiantes:**
- Sergio Andrés Díaz Vera (seadiazve@unal.edu.co)
- Julián Mateo Espinosa Ospina (juespinosao@unal.edu.co)

**Curso:** Cadenas de Markov y Aplicaciones (2025-II)
**Departamento:** Matemáticas - Universidad Nacional de Colombia
**Entrega:** 30 de octubre de 2025

## Descripción

Aplicación del muestreo de Gibbs a modelos estocásticos en rejillas: Hard-Core y q-coloraciones.

## Estructura

```
Tarea_1/
├── src/
│   ├── hard_core.py
│   ├── q_coloraciones.py
│   ├── estadisticas.py
│   ├── visualizacion.py
│   └── __init__.py
├── plantilla_src/          # Estructura de la plantilla LaTeX
│   ├── cfg/
│   ├── cmd/
│   ├── env/
│   ├── etc/
│   │   ├── contenido.tex
│   │   └── referencias.bib
│   ├── page/
│   ├── style/
│   ├── config.tex
│   └── defs.tex
├── img/                    # Imágenes y logotipos
│   ├── figuras/           # 11 figuras experimentales (577 KB total)
│   │   ├── hardcore_ejemplo.png
│   │   ├── trayectoria_cadena.png
│   │   ├── multiples_muestras_hc.png
│   │   ├── histograma_particulas.png
│   │   ├── verificacion_tiempos.png
│   │   ├── escalamiento.png
│   │   ├── qcoloracion_ejemplo.png
│   │   ├── trayectoria_q_coloraciones.png
│   │   ├── multiples_muestras_q3.png
│   │   ├── comparacion_q_valores.png
│   │   └── distribucion_colores.png
│   ├── Logotipounal2.png
│   └── departamentos/
│       └── unal.png
├── docs/
│   └── Tarea 1_muestreo de Gibbs.pdf
├── ejercicio_1a.ipynb
├── ejercicio_1b.ipynb
├── ejercicio_2.ipynb
├── main.tex
├── Tarea1_coautores.pdf    # PDF final con logotipos
├── template_local.tex
└── README.md
```

## Módulos Implementados

### `hard_core.py`
- `gibbs_sampler_hard_core()`: Muestreo de Gibbs para configuraciones factibles
- `es_configuracion_factible()`: Validación de restricción de adyacencia
- `contar_particulas()`: Conteo de elementos

### `q_coloraciones.py`
- `gibbs_sampler_q_coloraciones()`: Muestreo para q-coloraciones propias
- `es_coloracion_propia()`: Validación de restricción de colores
- `contar_colores()`: Distribución por color

### `estadisticas.py`
- `calcular_estadisticas()`: Estadísticas descriptivas
- `analizar_multiple_K()`: Análisis sistemático
- `crear_tabla_estadisticas()`: Tablas resumidas

### `visualizacion.py`
- `visualizar_configuracion()`: Visualización de rejillas
- `graficar_histograma()`: Distribuciones
- `graficar_escalamiento()`: Análisis de escalamiento
- `graficar_distribucion_colores()`: Distribución por color

## Ejercicios

### Ejercicio 1a: Modelo Hard-Core
Implementación del Gibbs Sampler para configuraciones sin partículas adyacentes.

### Ejercicio 1b: Estimación de Partículas
Análisis estadístico del número típico de partículas en configuraciones factibles.

### Ejercicio 2: q-Coloraciones
Generalización a q-coloraciones propias de la rejilla.

## Compilación en Overleaf

Este proyecto está completamente preparado para funcionar en Overleaf:

1. **Subir el proyecto completo** a Overleaf (incluye todas las carpetas y archivos)
2. **Archivo principal**: `main.tex`
3. **Compilador**: pdfLaTeX
4. **Compilación automática**: Overleaf compilará automáticamente al guardar cambios

**Estructura de archivos para Overleaf:**
- `main.tex`: Documento principal
- `plantilla_src/`: Plantilla LaTeX completa
- `plantilla_src/etc/contenido.tex`: Contenido del informe
- `img/`: Todas las imágenes y figuras
- `src/`: Código Python (referencia)

## Ejecución Local

```bash
# Notebooks
uv run jupyter notebook

# Compilar informe (desde Tareas/Tarea_1/)
pdflatex main.tex
pdflatex main.tex  # Segunda compilación para referencias cruzadas
```

## Entregables

- **Notebooks**: ejercicio_1a.ipynb, ejercicio_1b.ipynb, ejercicio_2.ipynb
- **Informe técnico**: Tarea1_coautores.pdf (20 páginas, 959 KB)
  - Estructura según documento del docente
  - 11 figuras experimentales de alta calidad
  - Visualizaciones de trayectorias de cadenas
  - Histogramas de verificación en diferentes tiempos
  - Múltiples muestras y comparaciones
  - Ambos autores incluidos
  - Logotipos institucionales
- **Código fuente**: src/ (4 módulos Python + __init__.py)
- **Figuras**: img/figuras/ (11 visualizaciones, 577 KB)

## Referencias

1. Levin, D.A., Peres, Y. (2017). *Markov Chains and Mixing Times*. AMS.
2. Norris, J.R. (1997). *Markov Chains*. Cambridge University Press.
