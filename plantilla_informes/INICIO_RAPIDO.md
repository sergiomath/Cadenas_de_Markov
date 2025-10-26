# 🚀 Inicio Rápido - Template UNAL

## ⚡ En 3 pasos

### 1️⃣ Edita tu información
Abre `main.tex` y cambia:
```latex
\def\documenttitle {Tu Título}
\def\documentauthor {Tu Nombre}
\def\coursename {Tu Curso}
```

### 2️⃣ Escribe tu contenido
Edita `src/etc/example.tex` con tu documento

### 3️⃣ Compila

**Linux/Mac:**
```bash
./compilar.sh
```

**Windows:**
```cmd
compilar.bat
```

**Manual:**
```bash
pdflatex main.tex
pdflatex main.tex
```

## 📄 Resultado

Tu PDF estará en `main.pdf`

---

## 📚 Más información

- [README.md](README.md) - Documentación completa
- [ESTRUCTURA.md](ESTRUCTURA.md) - Estructura del proyecto

---

## 💡 Comandos útiles

### Agregar sección
```latex
\section{Título}
\subsection{Subtítulo}
```

### Agregar ecuación
```latex
\insertequation[\label{eq:1}]{E = mc^2}
```

### Agregar imagen
```latex
\insertimage{img/foto.png}{scale=0.5}{Descripción}
```

### Agregar lista
```latex
\begin{itemize}
    \item Elemento 1
    \item Elemento 2
\end{itemize}
```

---

## ✅ Características incluidas

- ✓ Fondo con logo UNAL
- ✓ Formato profesional
- ✓ Portada automática
- ✓ Índice automático
- ✓ Numeración de páginas
- ✓ Encabezados y pies de página

---

¡Ya puedes empezar a escribir tu documento! 🎉
