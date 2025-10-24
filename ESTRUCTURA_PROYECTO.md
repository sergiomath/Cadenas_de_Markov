# Estructura del Proyecto - Cadenas de Markov

**Universidad Nacional de Colombia**
**Estudiante:** Sergio Andrés Díaz Vera

---

## 📊 Resumen de Evaluación

| Componente | Peso | Fecha Entrega | Estado |
|-----------|------|---------------|--------|
| **Primer Parcial** | 25% | Lunes 6 de octubre | ✅ Completado |
| Tarea 0 (Optativa) | - | Viernes 3 de octubre | - |
| Tarea 0.1 (Optativa) | - | Lunes 6 de octubre | - |
| **Segundo Parcial** | 25% | Jueves 4 de diciembre | ⏳ Pendiente |
| Tarea 1 | 10% | Jueves 30 de octubre | ⏳ Pendiente |
| Tarea 2 | 10% | ¿Jueves 13? | ⏳ Pendiente |
| Tarea 3 | 10% | ¿Jueves 20? | ⏳ Pendiente |
| **Proyecto Final** | 20% | ¿Martes 9 de diciembre? | ⏳ Pendiente |
| Documento escrito | 10% | ~Semana 14 | ⏳ Pendiente |
| Video | 10% | ~Semana 15 | ⏳ Pendiente |

**Total evaluado:** 70%

---

## 🗂️ Estructura de Carpetas

```
Cadenas_de_Markov/
│
├── 📁 Primer_Parcial/                    # 25% - Trabajo completado
│   ├── README.md
│   ├── src/                              # Implementaciones CPU/GPU
│   │   ├── __init__.py
│   │   └── markov_matrix.py
│   ├── notebooks/                        # Análisis y benchmarks
│   │   ├── metodo_vectores_propios.ipynb
│   │   ├── metodo_sistema.ipynb
│   │   └── metodo_gpu_final.ipynb
│   ├── resultados/                       # Datos experimentales (CSV)
│   ├── docs/                             # Descripción original
│   └── Tareas/                           # Tareas optativas
│
├── 📁 Segundo_Parcial/                   # 25% - Por hacer
│   ├── README.md
│   └── Tareas/
│       ├── Tarea_1/                      # 10%
│       ├── Tarea_2/                      # 10%
│       └── Tarea_3/                      # 10%
│
├── 📁 Proyecto/                          # 20% - Por hacer
│   ├── README.md
│   ├── documento_escrito/                # 10%
│   └── video/                            # 10%
│
├── README.md                             # Documentación general
├── CLAUDE.md                             # Instrucciones para Claude Code
├── requirements.txt                      # Dependencias Python
└── ESTRUCTURA_PROYECTO.md                # Este archivo
```

---

## 🎯 Primer Parcial (Completado)

### Contenido
Análisis comparativo de dos métodos para calcular distribuciones estacionarias en cadenas de Markov:

1. **Método 1:** Vectores propios (O(n³))
2. **Método 2:** Tiempos medios de retorno (O(n⁴))

### Resultados Principales

| Métrica | Método 1 | Método 2 |
|---------|----------|----------|
| Complejidad | O(n³) | O(n⁴) |
| Speedup GPU | 10-30x (n>200) | 1.2-2x |
| Paralelización | Excelente | Limitada |
| Recomendación | GPU para n>50 | CPU siempre |

### Uso del Código

Desde la raíz del proyecto:

```python
import sys
sys.path.append('Primer_Parcial')
from src.markov_matrix import *

# Crear matriz
P = crear_matriz_probabilidad(n=100, p=0.7)

# Calcular distribución estacionaria
pi = calcular_distribucion_metodo_autovalores(P)
```

---

## 📝 Segundo Parcial (Pendiente)

### Tareas Programadas

**Tarea 1 (10%)**
- Entrega: Jueves 30 de octubre
- Carpeta: `Segundo_Parcial/Tareas/Tarea_1/`

**Tarea 2 (10%)**
- Entrega: ¿Jueves 13?
- Carpeta: `Segundo_Parcial/Tareas/Tarea_2/`

**Tarea 3 (10%)**
- Entrega: ¿Jueves 20?
- Carpeta: `Segundo_Parcial/Tareas/Tarea_3/`

---

## 🎓 Proyecto Final (Pendiente)

### Componentes

**Documento Escrito (10%)**
- Entrega: ~Semana 14
- Carpeta: `Proyecto/documento_escrito/`
- Debe incluir implementaciones numéricas

**Video (10%)**
- Entrega: ~Semana 15
- Carpeta: `Proyecto/video/`

---

## 🔧 Configuración del Entorno

### Instalación Base
```bash
pip install -r requirements.txt
```

### GPU (Opcional)
```bash
# Verificar CUDA
nvidia-smi

# Instalar CuPy según versión CUDA
pip install cupy-cuda12x  # CUDA 12.x
pip install cupy-cuda11x  # CUDA 11.x
```

---

## 📚 Referencias

- **Repositorio:** [Ubicación local del proyecto]
- **Documentación Principal:** [README.md](README.md)
- **Guía para Claude:** [CLAUDE.md](CLAUDE.md)

---

**Última actualización:** 24 de octubre, 2025
