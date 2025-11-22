# Plantilla de Informes - Universidad Nacional de Colombia

Plantilla LaTeX profesional para informes académicos de la Universidad Nacional de Colombia, Departamento de Matemáticas.

## Contenido

- **`main.tex`**: Archivo principal del documento (ejemplo: Tarea 2)
- **`plantilla_src/`**: Carpeta con todos los archivos de la plantilla
- **`img/`**: Carpeta con imágenes (logo UNAL y figuras)
- **`Tarea2_Informe_Final.pdf`**: Ejemplo de documento compilado

## Estructura del Documento

### 1. Encabezado (main.tex)

```latex
% Informe - Cadenas de Markov y Aplicaciones

\documentclass[
	spanish,
	letterpaper, oneside
]{article}

% INFORMACIÓN DEL DOCUMENTO
\def\documenttitle {Título del Trabajo}
\def\documentsubtitle {Subtítulo}
\def\documentsubject {Tema del Documento}

\def\documentauthor {Nombre Estudiante 1, Nombre Estudiante 2}
\def\coursename {Nombre del Curso}
\def\coursecode {Código del Curso}

\def\universityname {Universidad Nacional de Colombia}
\def\universityfaculty {Facultad de Ciencias}
\def\universitydepartment {Departamento de Matemáticas}
\def\universitydepartmentimage {departamentos/unal}
\def\universitydepartmentimagecfg {height=1.57cm}
\def\universitylocation {Bogotá D.C., Colombia}
```

### 2. Tabla de Autores

```latex
% INTEGRANTES, PROFESORES Y FECHAS
\def\authortable {
	\begin{tabular}{ll}
		Estudiantes:
		& \begin{tabular}[t]{l}
			Nombre Estudiante 1 \\
			correo1@unal.edu.co \\
			\\
			Nombre Estudiante 2 \\
			correo2@unal.edu.co
		\end{tabular} \\
		& \\
		Profesor:
		& \begin{tabular}[t]{l}
			Nombre del Profesor
		\end{tabular} \\
		& \\
		\multicolumn{2}{l}{Fecha de entrega: DD de mes de YYYY} \\
		\multicolumn{2}{l}{\universitylocation}
	\end{tabular}
}
```

### 3. Importación de Plantilla

```latex
% IMPORTACIÓN DEL TEMPLATE
\input{plantilla_src/template}

% INICIO DE PÁGINAS
\begin{document}

% PORTADA
\templatePortrait

% CONFIGURACIÓN DE PÁGINA Y ENCABEZADOS
\templatePagecfg

% RESUMEN
\begin{abstractd}
Texto del resumen del documento...
\end{abstractd}

% TABLA DE CONTENIDOS
\templateIndex

% CONFIGURACIONES FINALES
\templateFinalcfg
```

### 4. Contenido

Puedes incluir el contenido de dos formas:

**Opción 1: Archivo externo**
```latex
\input{plantilla_src/etc/contenido}
```

**Opción 2: Directamente en main.tex**
```latex
\section{Introducción}
Contenido de la introducción...

\section{Marco Teórico}
Contenido del marco teórico...
```

### 5. Cierre del Documento

```latex
% FIN DEL DOCUMENTO
\end{document}
```

## Entornos Matemáticos Disponibles

La plantilla define los siguientes entornos:

- **`\begin{teo}...\end{teo}`**: Teoremas
- **`\begin{defn}...\end{defn}`**: Definiciones
- **`\begin{cor}...\end{cor}`**: Corolarios
- **`\begin{lema}...\end{lema}`**: Lemas
- **`\begin{prop}...\end{prop}`**: Proposiciones

Ejemplo:
```latex
\begin{teo}[Nombre del Teorema]
Enunciado del teorema...
\end{teo}
```

## Insertar Imágenes

La plantilla proporciona el comando `\insertimage`:

```latex
\insertimage[\label{fig:ejemplo}]{ruta/imagen.png}{width=12cm}{Descripción de la figura}
```

Parámetros:
- `[\label{fig:ejemplo}]`: Etiqueta opcional para referencias
- `{ruta/imagen.png}`: Ruta a la imagen (relativa a la carpeta por defecto `img/`)
- `{width=12cm}`: Opciones de tamaño
- `{Descripción de la figura}`: Caption de la figura

## Compilación

### Comando Simple
```bash
pdflatex main.tex
pdflatex main.tex  # Compilar dos veces para tabla de contenidos
```

### Con Bibliografía
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Configuración de la Plantilla

Los archivos principales de configuración están en:

- **`plantilla_src/config.tex`**: Configuración general (márgenes, fuentes, colores)
- **`plantilla_src/defs.tex`**: Definiciones de colores personalizados
- **`plantilla_src/env/imports.tex`**: Paquetes LaTeX importados
- **`plantilla_src/page/portrait.tex`**: Configuración de la portada

## Modificaciones Realizadas

Para compatibilidad con sistemas que no tienen todos los paquetes:

1. **`plantilla_src/env/imports.tex`** (línea 145):
   ```latex
   %\usepackage{physics}  % Comentado - no disponible en todos los sistemas
   ```

2. **`plantilla_src/env/imports.tex`** (línea 847):
   ```latex
   %\usepackage{commonunicode}  % Comentado - requiere stmaryrd
   ```

## Estructura de Carpetas

```
plantillas_informes_unal/
├── README.md                          # Este archivo
├── main.tex                           # Documento principal
├── Tarea2_Informe_Final.pdf          # Ejemplo compilado
├── img/                               # Imágenes
│   ├── Logotipounal2.png             # Logo UNAL
│   └── departamentos/                # Logos de departamentos
│       └── unal.png
└── plantilla_src/                    # Archivos de la plantilla
    ├── template.tex                  # Núcleo de la plantilla
    ├── config.tex                    # Configuración general
    ├── defs.tex                      # Definiciones
    ├── cfg/                          # Configuraciones específicas
    ├── cmd/                          # Comandos personalizados
    ├── env/                          # Entornos y paquetes
    ├── etc/                          # Contenido de ejemplo
    ├── page/                         # Configuración de páginas
    └── style/                        # Estilos
```

## Personalización Rápida

Para adaptar la plantilla a tu curso/tarea:

1. Abre `main.tex`
2. Modifica las siguientes líneas:
   - Línea 9: `\def\documenttitle {Tu Título}`
   - Línea 10: `\def\documentsubtitle {Tu Subtítulo}`
   - Línea 14: `\def\coursename {Tu Curso}`
   - Líneas 28-33: Información de estudiantes
   - Línea 38: Nombre del profesor
   - Línea 41: Fecha de entrega
3. Modifica el resumen (líneas 59-61)
4. Agrega tu contenido después de la línea 69

## Créditos

- **Plantilla original**: Pablo Pizarro R. (https://latex.ppizarror.com/informe)
- **Adaptación UNAL**: Sergio Andrés Díaz Vera
- **Licencia**: MIT

## Soporte

Para problemas con la compilación:
- Verifica que tienes instalado `texlive-full` o al menos `texlive-latex-extra`
- Si falta algún paquete, puedes comentarlo en `plantilla_src/env/imports.tex`
- Compila siempre dos veces para generar correctamente la tabla de contenidos

## Ejemplo de Uso

Ver el archivo `main.tex` incluido como ejemplo completo de un informe de la Tarea 2 del curso de Cadenas de Markov.
