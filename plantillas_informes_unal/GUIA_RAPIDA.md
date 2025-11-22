# Guía Rápida - Plantilla Informes UNAL

## Inicio Rápido (3 pasos)

### 1. Copiar plantilla vacía
```bash
cp plantilla_vacia.tex mi_tarea.tex
```

### 2. Editar información básica
Abre `mi_tarea.tex` y modifica:
- **Línea 12**: Título del trabajo
- **Línea 13**: Subtítulo (ej: "Tarea 1")
- **Línea 16**: Nombre de los estudiantes
- **Línea 17**: Nombre del curso
- **Líneas 30-35**: Correos de estudiantes
- **Línea 39**: Nombre del profesor
- **Línea 42**: Fecha de entrega

### 3. Compilar
```bash
./compilar.sh mi_tarea.tex
# O manualmente:
pdflatex mi_tarea.tex
pdflatex mi_tarea.tex
```

## Comandos Útiles

### Secciones
```latex
\section{Título Sección}
\subsection{Título Subsección}
\subsubsection{Título Subsubsección}
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

### Matemáticas
```latex
% Ecuación en línea
El resultado es $x^2 + y^2 = z^2$

% Ecuación centrada sin número
\[
    E = mc^2
\]

% Ecuación numerada
\begin{equation}
    \int_a^b f(x)dx = F(b) - F(a)
\end{equation}

% Varias ecuaciones alineadas
\begin{align}
    x + y &= 5 \\
    2x - y &= 1
\end{align}
```

### Teoremas y Definiciones
```latex
\begin{teo}[Nombre Opcional]
Enunciado del teorema...
\end{teo}

\begin{defn}[Nombre Opcional]
Texto de la definición...
\end{defn}

\begin{prop}
Enunciado de la proposición...
\end{prop}
```

### Tablas
```latex
\begin{table}[htbp]
\centering
\caption{Título de la tabla}
\label{tab:mitabla}
\begin{tabular}{|l|c|r|}
\hline
Izq & Centro & Der \\
\hline
A & B & C \\
D & E & F \\
\hline
\end{tabular}
\end{table}
```

### Figuras
```latex
% Opción 1: Con comando de plantilla
\insertimage[\label{fig:ejemplo}]{imagen.png}{width=12cm}{Descripción}

% Opción 2: Estándar LaTeX
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{img/imagen.png}
\caption{Descripción de la figura}
\label{fig:mifigura}
\end{figure}
```

### Referencias
```latex
% Referenciar una ecuación
Como se ve en la ecuación \ref{eq:miecuacion}...

% Referenciar una figura
La Figura \ref{fig:mifigura} muestra...

% Referenciar una tabla
Los datos de la Tabla \ref{tab:mitabla}...

% Referenciar una sección
En la Sección \ref{sec:intro}...
```

### Código
```latex
\begin{lstlisting}[language=Python]
def hello_world():
    print("Hello, World!")
\end{lstlisting}
```

## Estructura Típica de un Informe

```latex
\section{Introducción}
- Contexto del problema
- Objetivos
- Estructura del documento

\section{Marco Teórico}
- Definiciones
- Teoremas relevantes
- Estado del arte

\section{Metodología}
- Descripción del método
- Implementación
- Herramientas utilizadas

\section{Resultados}
- Presentación de resultados
- Tablas y figuras
- Análisis

\section{Discusión}
- Interpretación de resultados
- Comparación con trabajos previos
- Limitaciones

\section{Conclusiones}
- Resumen de logros
- Conclusiones principales
- Trabajo futuro

\section{Referencias}
- Bibliografía
```

## Solución de Problemas Comunes

### Error: "File not found"
- Verifica que la carpeta `plantilla_src/` esté en el mismo directorio
- Verifica que la carpeta `img/` exista

### Error: "Undefined control sequence"
- Puede que falte un paquete. Revisa el archivo `.log`
- Si es un comando de la plantilla, verifica que esté bien escrito

### La tabla de contenidos no aparece
- Compila dos veces el documento
- LaTeX genera el índice en la segunda compilación

### Las figuras no se ven
- Verifica la ruta de la imagen
- Por defecto, las imágenes deben estar en `img/`
- Formatos soportados: PNG, JPG, PDF

### Cambiar márgenes, fuente, colores
- Edita `plantilla_src/config.tex`
- Busca las variables correspondientes y modifica sus valores

## Tips

1. **Compila frecuentemente**: No esperes a terminar todo el documento
2. **Usa etiquetas descriptivas**: `\label{fig:resultados_exp1}` es mejor que `\label{fig1}`
3. **Organiza las imágenes**: Crea subcarpetas en `img/` por sección
4. **Comenta tu código**: Usa `%` para comentarios que ayuden a navegar el documento
5. **Versionado**: Usa Git para trackear cambios en tu documento

## Recursos Adicionales

- **Overleaf**: Editor LaTeX online - https://www.overleaf.com
- **Detexify**: Encuentra símbolos LaTeX dibujándolos - http://detexify.kirelabs.org
- **Tables Generator**: Genera código LaTeX para tablas - https://www.tablesgenerator.com

## Contacto y Soporte

Para preguntas sobre la plantilla, revisa primero el `README.md` completo.
