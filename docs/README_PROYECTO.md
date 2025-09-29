# Proyecto Cadenas de Markov

Este proyecto implementa funcionalidades para trabajar con Cadenas de Markov en Python.

## Estructura del Proyecto

```
Cadenas_de_Markov/
├── src/                    # Código fuente
│   ├── __init__.py        # Inicialización del módulo
│   └── markov_matrix.py   # Funciones principales
├── notebooks/             # Jupyter notebooks
│   └── pruebas_cadenas}.ipynb  # Notebook de pruebas
├── examples/              # Ejemplos de uso
│   └── ejemplo_basico.py  # Ejemplo básico
├── tests/                 # Tests (vacío por ahora)
├── docs/                  # Documentación
├── requirements.txt       # Dependencias
└── README.md             # Documentación principal
```

## Funciones Principales

### `crear_matriz_probabilidad(n, p)`
Crea una matriz de probabilidad para una cadena de Markov donde:
- **Estados intermedios**: probabilidad `p` de ir al siguiente, `1-p` de volver al anterior
- **Estado inicial**: probabilidad `p` de avanzar, `1-p` de quedarse
- **Estado final**: probabilidad `p` de quedarse, `1-p` de retroceder

### `calcular_vector_propio_dominante(matriz)`
Calcula el vector propio asociado al valor propio más grande de la matriz.

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

Ver `examples/ejemplo_basico.py` y `notebooks/pruebas_cadenas}.ipynb` para ejemplos de uso.