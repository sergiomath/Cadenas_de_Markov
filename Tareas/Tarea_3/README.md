# Tarea 3: Muestreo MCMC vs Simulación Perfecta

**Curso:** Cadenas de Markov y Aplicaciones (2025-II)
**Profesor:** Freddy Hernández-Romero
**Integrantes:** Sergio Andrés Díaz Vera, Julián Mateo Espinosa Ospina

## Descripción

Comparación entre muestreo MCMC (Gibbs Sampler) y simulación perfecta (Propp-Wilson) aplicados al modelo de Ising en lattice 2D.

## Estructura

```
Tarea_3/
├── docs/                    # Enunciado original
├── src/                     # Implementación de algoritmos
│   └── ising_model.py
├── notebooks/               # Experimento completo
│   └── tarea3_ising.ipynb
├── resultados/              # Gráficas y datos generados
└── informe_tarea_3/         # Informe en LaTeX
    └── main.pdf
```

## Ejecución

### Opción 1: Notebook Jupyter
```bash
cd Tareas/Tarea_3
uv run jupyter notebook notebooks/tarea3_ising.ipynb
# Ejecutar todas las celdas (Kernel → Restart & Run All)
```

### Opción 2: Compilar informe
```bash
cd informe_tarea_3
pdflatex main.tex
pdflatex main.tex  # Segunda vez para referencias
```

## Parámetros

- **Lattice:** K = 12 (144 sitios)
- **β valores:** 0.0, 0.1, ..., 1.0 (11 valores)
- **Muestreo adaptativo** para factibilidad computacional
- **Tiempo estimado:** 10-15 minutos

## Resultados Principales

1. **Transición de fase** observable en β ≈ 0.44
2. **Tiempo de coalescencia** crece exponencialmente: T ~ exp(7.5β)
3. **Consistencia** entre métodos: diferencia < 5%

## Estado: ✅ Completado