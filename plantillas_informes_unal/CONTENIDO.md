# Contenido de la Plantilla

## 📁 Archivos Principales

### Documentación
- **`README.md`** (6.7 KB) - Documentación completa de la plantilla
- **`GUIA_RAPIDA.md`** (4.8 KB) - Guía rápida de uso con comandos comunes
- **`CONTENIDO.md`** (este archivo) - Índice de contenidos

### Archivos LaTeX
- **`main.tex`** (2.4 KB) - Ejemplo completo (Tarea 2 de Cadenas de Markov)
- **`plantilla_vacia.tex`** (4.4 KB) - Plantilla lista para usar en nuevos proyectos

### PDFs de Ejemplo
- **`Tarea2_Informe_Final.pdf`** (771 KB) - Documento compilado de ejemplo
- **`plantilla_vacia.pdf`** (252 KB) - Plantilla vacía compilada

### Utilidades
- **`compilar.sh`** (2.1 KB) - Script bash para compilar documentos

## 📂 Directorios

### `plantilla_src/` - Núcleo de la Plantilla
Sistema de plantilla LaTeX completo con todos los archivos de configuración.

**Estructura:**
```
plantilla_src/
├── template.tex              # Archivo principal que carga todo
├── config.tex                 # Configuración general (márgenes, fuentes, etc.)
├── defs.tex                   # Definiciones de colores
│
├── cfg/                       # Configuraciones específicas
│   ├── init.tex              # Inicialización del documento
│   ├── page.tex              # Configuración de páginas
│   └── final.tex             # Configuraciones finales
│
├── cmd/                       # Comandos personalizados
│   ├── core.tex              # Comandos básicos
│   ├── equation.tex          # Comandos para ecuaciones
│   ├── image.tex             # Comandos para imágenes
│   ├── math.tex              # Comandos matemáticos
│   ├── title.tex             # Comandos de títulos
│   ├── other.tex             # Otros comandos
│   └── column.tex            # Comandos de columnas
│
├── env/                       # Entornos y paquetes
│   ├── imports.tex           # Importación de paquetes LaTeX
│   └── environments.tex      # Definición de entornos personalizados
│
├── etc/                       # Contenido de ejemplo
│   ├── contenido.tex         # Contenido de Tarea 1 (para referencia)
│   └── contenido_tarea2.tex  # Contenido de Tarea 2
│
├── page/                      # Configuración de páginas especiales
│   ├── portrait.tex          # Generación de portada
│   ├── portrait_config.tex   # Configuración de portada
│   └── index.tex             # Generación de índices
│
└── style/                     # Estilos
    ├── code.tex              # Estilos para código
    └── other.tex             # Otros estilos
```

### `img/` - Recursos Gráficos
Contiene todas las imágenes necesarias para los documentos.

**Contenido:**
```
img/
├── Logotipounal2.png         # Logo oficial UNAL
├── departamentos/             # Logos de departamentos
│   └── unal.png              # Logo departamento
└── figuras/                   # Carpeta para figuras del documento
    └── (tus figuras aquí)
```

## 🎯 Archivos Clave para Personalización

### Para Empezar un Nuevo Documento
1. Copia `plantilla_vacia.tex`
2. Edita las variables de información (líneas 12-42)
3. Agrega tu contenido después de la línea 69

### Para Modificar el Diseño
- **Márgenes**: `plantilla_src/config.tex` (líneas 276-280)
- **Fuentes**: `plantilla_src/config.tex` (líneas 17-18)
- **Colores**: `plantilla_src/defs.tex` (líneas 15-24)
- **Portada**: `plantilla_src/page/portrait.tex`

### Para Agregar Paquetes
- **Archivo**: `plantilla_src/env/imports.tex`
- Agrega `\usepackage{nombre_paquete}` en la sección apropiada

## 📊 Estadísticas

- **Tamaño total**: 2.1 MB
- **Archivos LaTeX**: 2
- **PDFs de ejemplo**: 2
- **Archivos de documentación**: 3
- **Archivos de plantilla**: ~50

## 🔧 Modificaciones Realizadas

Para asegurar compatibilidad en diferentes sistemas:

1. **`plantilla_src/env/imports.tex:145`**
   ```latex
   %\usepackage{physics}  % Comentado - no disponible
   ```

2. **`plantilla_src/env/imports.tex:847`**
   ```latex
   %\usepackage{commonunicode}  % Comentado - requiere stmaryrd
   ```

3. **Entornos matemáticos adaptados**:
   - `\begin{theorem}` → `\begin{teo}`
   - Definidos en `plantilla_src/cfg/init.tex:668-672`

## 🚀 Inicio Rápido

```bash
# 1. Copiar plantilla
cp plantilla_vacia.tex mi_informe.tex

# 2. Editar información básica
nano mi_informe.tex  # o tu editor preferido

# 3. Compilar
./compilar.sh mi_informe.tex
```

## 📖 Documentación

Para información detallada sobre:
- **Uso básico**: Ver `GUIA_RAPIDA.md`
- **Configuración avanzada**: Ver `README.md`
- **Ejemplos**: Ver `main.tex` y `plantilla_vacia.tex`

## 📝 Notas

- La plantilla está basada en el trabajo de Pablo Pizarro R.
- Licencia: MIT
- Adaptada para Universidad Nacional de Colombia
- Compatible con pdfLaTeX

## ✅ Verificación

Todos los archivos han sido probados y funcionan correctamente:
- ✓ `main.tex` compila → `Tarea2_Informe_Final.pdf` (771 KB)
- ✓ `plantilla_vacia.tex` compila → `plantilla_vacia.pdf` (252 KB)
- ✓ Script `compilar.sh` funcional
- ✓ Todos los recursos gráficos presentes
