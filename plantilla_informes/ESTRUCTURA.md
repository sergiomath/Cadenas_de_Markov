# 📂 Estructura del Proyecto

## Archivos Principales

```
Template-Informe/
│
├── 📄 main.tex                  ← EDITAR: Archivo principal del documento
├── 📄 template.tex              ⚠️  NO MODIFICAR: Template base
│
├── 🔧 compilar.sh               ← Script de compilación (Linux/Mac)
├── 🔧 compilar.bat              ← Script de compilación (Windows)
│
├── 📖 README.md                 ← Documentación principal
├── 📖 ESTRUCTURA.md             ← Este archivo
├── 📄 LICENSE                   ← Licencia MIT
│
└── 📁 Carpetas principales...
```

## Carpetas

### 📁 `img/` - Imágenes

```
img/
├── Logotipounal2.png           ← Imagen de fondo (logo UNAL)
└── departamentos/
    └── unal.png                ← Logo para encabezado
```

**Propósito**: Almacena todas las imágenes del documento.

**Cómo agregar imágenes**:
1. Coloca tu imagen en esta carpeta
2. En tu documento, usa: `\insertimage{img/tu_imagen.png}{scale=0.5}{Descripción}`

---

### 📁 `src/` - Código Fuente

```
src/
├── cfg/                        ← Configuraciones de página
│   ├── final.tex              # Configuraciones finales
│   ├── init.tex               # Inicialización
│   ├── page.tex               # Configuración de página (FONDO AQUÍ)
│   └── page_*.tex             # Variantes de página
│
├── cmd/                        ← Comandos personalizados
│   ├── core.tex               # Comandos básicos
│   ├── equation.tex           # Comandos para ecuaciones
│   ├── image.tex              # Comandos para imágenes
│   ├── title.tex              # Comandos de título
│   └── *.tex                  # Otros comandos
│
├── env/                        ← Entornos y paquetes
│   ├── environments.tex       # Definición de entornos
│   └── imports.tex            # Importación de paquetes LaTeX
│
├── etc/                        ← Archivos adicionales
│   └── example.tex            ← EDITAR: Contenido del documento
│
├── page/                       ← Portadas y páginas especiales
│   ├── index.tex              # Índice
│   ├── portrait.tex           # Portada
│   └── portrait_config.tex    # Configuración de portada
│
└── style/                      ← Estilos
    ├── code.tex               # Estilo de código
    └── other.tex              # Otros estilos
```

---

### 📁 `ejemplos/` - Ejemplos

```
ejemplos/
└── ejemplo_compilado.pdf       ← PDF de ejemplo ya compilado
```

**Propósito**: Almacena ejemplos de documentos compilados.

---

### 📁 `docs/` - Documentación

```
docs/
└── README_ORIGINAL.md          ← README original del template base
```

**Propósito**: Documentación adicional y archivos de referencia.

---

## Archivos que DEBES editar

### 1. `main.tex`
**Qué modificar**:
- Título del documento
- Autor(es)
- Curso/materia
- Tabla de integrantes
- Información de la universidad

### 2. `src/etc/example.tex`
**Qué modificar**:
- Todo el contenido de tu documento
- Secciones, subsecciones
- Ecuaciones, tablas, imágenes
- Texto en general

---

## Archivos que PUEDES editar (avanzado)

### `src/cfg/page.tex` (líneas 17-35)
**Para qué**: Cambiar la opacidad o imagen del fondo

```latex
\node[anchor=center,opacity=0.6,inner sep=0pt]...  % ← Cambia opacity aquí
```

### `src/config.tex`
**Para qué**: Cambiar configuraciones globales del template (márgenes, colores, etc.)

---

## Archivos que NO debes modificar

⚠️ **NO modificar** estos archivos a menos que sepas lo que haces:

- `template.tex`
- `src/cmd/*.tex`
- `src/env/imports.tex`
- `src/env/environments.tex`
- `src/page/portrait.tex`

Modificar estos archivos puede romper el template.

---

## Flujo de Trabajo Recomendado

### Primera vez

1. **Edita** `main.tex` con tu información
2. **Edita** `src/etc/example.tex` con tu contenido
3. **Compila** con: `./compilar.sh` (Linux/Mac) o `compilar.bat` (Windows)
4. **Revisa** `main.pdf`

### Cada vez que hagas cambios

1. **Edita** tu contenido en `src/etc/example.tex`
2. **Compila** de nuevo
3. **Revisa** el PDF

---

## Archivos Temporales (se pueden borrar)

Estos archivos se generan automáticamente al compilar:

```
*.aux      # Archivos auxiliares
*.log      # Logs de compilación
*.toc      # Tabla de contenidos temporal
*.out      # Marcadores temporales
*.lof      # Lista de figuras temporal
*.lot      # Lista de tablas temporal
*.lol      # Lista de código temporal
*.bbl      # Bibliografía temporal
*.blg      # Log de bibliografía
*.synctex.gz  # Sincronización
```

**Limpiar**: Usa el script de compilación y responde "S" cuando pregunte si limpiar.

---

## Tamaño y Organización

| Tipo | Cantidad Aproximada |
|------|---------------------|
| Archivos totales | ~80 archivos |
| Tamaño total | ~70-80 MB |
| Archivos principales | 2 (main.tex, template.tex) |
| Archivos a editar | 2 (main.tex, example.tex) |

---

## Preguntas Frecuentes

### ¿Dónde está el contenido del documento?
→ `src/etc/example.tex`

### ¿Cómo cambio el título?
→ Edita `main.tex`, línea ~19

### ¿Cómo agrego imágenes?
→ Ponlas en `img/` y usa `\insertimage{img/nombre.png}...`

### ¿Cómo cambio el fondo?
→ Edita `src/cfg/page.tex`, línea 21 (opacidad) o 22 (imagen)

### ¿Puedo usar otro logo?
→ Sí, reemplaza `img/Logotipounal2.png` con tu imagen

---

<div align="center">

📚 Para más información, consulta el [README.md](README.md)

</div>
