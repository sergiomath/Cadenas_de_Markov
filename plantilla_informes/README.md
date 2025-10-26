# 📄 Plantilla LaTeX - Universidad Nacional de Colombia

Plantilla profesional para la elaboración de informes, trabajos y documentos académicos de la Universidad Nacional de Colombia.

![UNAL](https://img.shields.io/badge/UNAL-Universidad%20Nacional%20de%20Colombia-green)
![LaTeX](https://img.shields.io/badge/LaTeX-Template-blue)
![License](https://img.shields.io/badge/license-MIT-orange)

## ✨ Características

- ✅ **Fondo con logo UNAL** en todas las páginas (opacidad 60%)
- ✅ **Degradado suave** en los bordes para mejor legibilidad
- ✅ **Estructura limpia** y organizada
- ✅ **Formato profesional** y consistente
- ✅ **Compatible** con pdfLaTeX
- ✅ **Fácil personalización**

---

## 📁 Estructura del Proyecto

```
Template-Informe/
├── 📄 main.tex                 # ← ARCHIVO PRINCIPAL (edita aquí)
├── 📄 template.tex             # Template base (NO MODIFICAR)
│
├── 📁 img/                     # Imágenes
│   ├── Logotipounal2.png      # Logo de fondo
│   └── departamentos/
│       └── unal.png           # Logo del encabezado
│
├── 📁 src/                     # Código fuente del template
│   ├── cfg/                    # Configuraciones de página
│   ├── cmd/                    # Comandos personalizados
│   ├── env/                    # Entornos y paquetes LaTeX
│   ├── etc/
│   │   └── example.tex        # ← Contenido de ejemplo (edita aquí)
│   ├── page/                   # Configuración de portadas
│   └── style/                  # Estilos
│
├── 📁 ejemplos/                # PDFs de ejemplo
│   └── ejemplo_compilado.pdf
│
└── 📁 docs/                    # Documentación adicional
```

---

## 🚀 Inicio Rápido

### 1️⃣ Compilar el documento

```bash
pdflatex main.tex
pdflatex main.tex  # Segunda vez para referencias
```

### 2️⃣ Ver el resultado

El archivo `main.pdf` se generará en el directorio raíz.

---

## 📝 Cómo usar esta plantilla

### ✏️ Paso 1: Editar información del documento

Abre `main.tex` y modifica:

```latex
% INFORMACIÓN DEL DOCUMENTO
\def\documenttitle {Tu Título Aquí}          % ← Cambia esto
\def\documentsubtitle {}
\def\documentsubject {Tu tema}               % ← Cambia esto

\def\documentauthor {Tu Nombre}              % ← Cambia esto
\def\coursename {Nombre del curso}           % ← Cambia esto
\def\coursecode {CÓDIGO-123}                 % ← Cambia esto

\def\universityname {Universidad Nacional de Colombia}
\def\universityfaculty {Tu Facultad}         % ← Cambia esto
\def\universitydepartment {Tu Departamento}  % ← Cambia esto
\def\universitylocation {Bogotá D.C., Colombia}
```

### ✏️ Paso 2: Editar autores/integrantes

En `main.tex`, modifica la tabla de autores:

```latex
\def\authortable {
	\begin{tabular}{ll}
		Integrantes:
		& \begin{tabular}[t]{l}
			Nombre 1 \\          % ← Cambia los nombres
			Nombre 2
		\end{tabular} \\
		Profesor:
		& \begin{tabular}[t]{l}
			Profesor 1           % ← Cambia el profesor
		\end{tabular} \\
		\multicolumn{2}{l}{Fecha: \today}
	\end{tabular}
}
```

### ✏️ Paso 3: Escribir tu contenido

Edita el archivo `src/etc/example.tex` con tu propio contenido, o crea un nuevo archivo:

```latex
% En main.tex, cambia la línea:
\input{src/etc/example}  % ← Cambia a tu archivo

% Por ejemplo:
\input{src/etc/mi_documento}
```

---

## 💻 Compilación Detallada

### Desde terminal/consola

#### 🐧 Linux / 🍎 macOS:

```bash
# Compilación básica
pdflatex main.tex

# Compilación completa (recomendado)
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex

# Limpiar archivos temporales
rm -f *.aux *.log *.toc *.out *.lof *.lot *.lol *.bbl *.blg *.synctex.gz
```

#### 🪟 Windows (PowerShell):

```powershell
# Compilación básica
pdflatex main.tex

# Compilación completa
pdflatex main.tex; pdflatex main.tex; pdflatex main.tex

# Limpiar archivos temporales
Remove-Item *.aux,*.log,*.toc,*.out,*.lof,*.lot,*.lol,*.bbl,*.blg,*.synctex.gz -Force
```

#### 🪟 Windows (CMD):

```cmd
pdflatex main.tex
pdflatex main.tex
pdflatex main.tex
```

### Desde editores LaTeX

- **Overleaf**: Sube todos los archivos y compila con pdfLaTeX
- **TeXstudio**: Abre `main.tex` y presiona F5
- **VS Code** (con LaTeX Workshop): Abre `main.tex` y guarda (Ctrl+S)

---

## 🎨 Personalización

### Cambiar la opacidad del fondo

Edita `src/cfg/page.tex` línea 21:

```latex
\node[anchor=center,opacity=0.6,inner sep=0pt] at (current page.center) {%
                        ↑
                    Cambia este valor (0.0 a 1.0)
```

- `0.0` = Completamente transparente (invisible)
- `0.3` = Muy tenue
- `0.6` = Visible pero no invasivo (valor actual)
- `1.0` = Completamente opaco

### Cambiar la imagen de fondo

Reemplaza el archivo `img/Logotipounal2.png` con tu imagen, o edita la ruta en `src/cfg/page.tex` línea 22.

### Cambiar colores

Los colores se pueden modificar en `src/config.tex` (busca las variables de color).

---

## 📚 Comandos LaTeX Útiles

### Estructura del documento

```latex
\section{Título de Sección}
\subsection{Título de Subsección}
\subsubsection{Título de Subsubsección}
```

### Ecuaciones

```latex
\insertequation[\label{eq:einstein}]{E = mc^2}

% Referencia:
Como se ve en la ecuación \eqref{eq:einstein}...
```

### Listas

```latex
% Lista con viñetas
\begin{itemize}
    \item Elemento 1
    \item Elemento 2
\end{itemize}

% Lista numerada
\begin{enumerate}
    \item Primer elemento
    \item Segundo elemento
\end{enumerate}
```

### Imágenes

```latex
\insertimage[\label{img:logo}]{img/mi_imagen.png}{scale=0.5}{Descripción}

% Referencia:
Ver la Figura \ref{img:logo}...
```

### Tablas

```latex
\begin{table}[htbp]
\centering
\begin{tabular}{|l|c|r|}
\hline
Columna 1 & Columna 2 & Columna 3 \\
\hline
Dato 1 & Dato 2 & Dato 3 \\
\hline
\end{tabular}
\caption{Descripción de la tabla}
\label{tab:ejemplo}
\end{table}
```

---

## 🔧 Solución de Problemas

### ❌ Error: "No se encuentra la imagen"

**Solución**:
1. Verifica que `img/Logotipounal2.png` existe
2. Verifica que la ruta en `src/cfg/page.tex` es correcta

### ❌ El fondo no se ve

**Solución**:
1. Compila el documento **DOS VECES**
2. Aumenta la opacidad en `src/cfg/page.tex` (línea 21)
3. Verifica que tienes instalado el paquete `tikz`

### ❌ Error de paquetes faltantes

**Solución**:
Instala la distribución completa de LaTeX:
- Linux: `sudo apt-get install texlive-full`
- Mac: Descarga MacTeX
- Windows: Descarga MiKTeX o TeX Live

### ❌ Compilación lenta

**Normal**: La primera compilación puede tardar. Las siguientes serán más rápidas.

---

## 📋 Requisitos del Sistema

### Software necesario

| Software | Descripción |
|----------|-------------|
| **LaTeX Distribution** | TeX Live (Linux), MiKTeX (Windows), MacTeX (Mac) |
| **pdfLaTeX** | Incluido en las distribuciones anteriores |

### Paquetes LaTeX principales

Los siguientes paquetes se cargan automáticamente:

- `tikz` → Gráficos y efectos
- `eso-pic` → Imágenes de fondo
- `graphicx` → Manejo de imágenes
- `fancyhdr` → Encabezados y pies de página
- `geometry` → Márgenes
- `hyperref` → Enlaces y referencias

---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**. Ver [LICENSE](LICENSE) para más detalles.

## 👤 Créditos

### Autor Original
- **Pablo Pizarro R.**
- 📧 pablo@ppizarror.com
- 🌐 https://latex.ppizarror.com/informe

### Adaptación UNAL
Plantilla adaptada para la Universidad Nacional de Colombia con:
- ✅ Logo institucional como fondo en todas las páginas
- ✅ Configuración predeterminada UNAL
- ✅ Estructura simplificada y documentada

---

## 📞 Soporte

¿Problemas o preguntas?

1. Revisa la sección **Solución de Problemas**
2. Consulta la documentación en `docs/`
3. Crea un issue en el repositorio

---

## 🎓 Recursos Adicionales

- [Documentación oficial de LaTeX](https://www.latex-project.org/)
- [Overleaf Learn](https://www.overleaf.com/learn)
- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX)

---

<div align="center">

**¡Disfruta escribiendo tus documentos académicos con estilo! 🎉**

</div>
