# 📘 Plantilla de Informes - Universidad Nacional de Colombia

**Plantilla LaTeX profesional para informes académicos**
Departamento de Matemáticas - Facultad de Ciencias

---

## 🚀 Inicio Rápido (3 Comandos)

```bash
cp plantilla_vacia.tex mi_informe.tex
# Editar mi_informe.tex con tu información
./compilar.sh mi_informe.tex
```

---

## 📚 Documentación

### Para Nuevos Usuarios
👉 **[GUIA_RAPIDA.md](GUIA_RAPIDA.md)** - Empieza aquí
- Comandos LaTeX básicos
- Ejemplos de uso común
- Tips y trucos

### Para Usuarios Avanzados
👉 **[README.md](README.md)** - Documentación completa
- Configuración detallada
- Personalización avanzada
- Estructura de la plantilla

### Referencia
👉 **[CONTENIDO.md](CONTENIDO.md)** - Índice de archivos
- Descripción de todos los archivos
- Estructura de carpetas
- Modificaciones realizadas

---

## 📂 Archivos Principales

| Archivo | Descripción | Tamaño |
|---------|-------------|---------|
| `plantilla_vacia.tex` | Plantilla lista para usar | 4.4 KB |
| `main.tex` | Ejemplo completo (Tarea 2) | 2.4 KB |
| `Tarea2_Informe_Final.pdf` | Documento de ejemplo | 771 KB |
| `plantilla_vacia.pdf` | Plantilla compilada | 252 KB |
| `compilar.sh` | Script de compilación | 2.1 KB |

---

## 🎯 ¿Qué Puedo Hacer?

### ✅ Crear un Nuevo Informe
```bash
cp plantilla_vacia.tex tarea1.tex
nano tarea1.tex  # Edita la información
./compilar.sh tarea1.tex
```

### ✅ Ver un Ejemplo Completo
Abre `main.tex` para ver un informe completo de la Tarea 2

### ✅ Compilar Manualmente
```bash
pdflatex mi_documento.tex
pdflatex mi_documento.tex  # Segunda vez para índices
```

---

## 📖 Características

✨ **Portada Profesional**
- Logo UNAL oficial
- Información de curso y autores
- Formato institucional

✨ **Contenido Estructurado**
- Tabla de contenidos automática
- Numeración de secciones
- Referencias cruzadas

✨ **Matemáticas**
- Entornos: teoremas, definiciones, proposiciones
- Ecuaciones numeradas
- Soporte completo para símbolos matemáticos

✨ **Figuras y Tablas**
- Comandos simplificados
- Numeración automática
- Captions profesionales

---

## 🛠️ Requisitos

- **LaTeX**: `texlive-full` o mínimo `texlive-latex-extra`
- **Compilador**: pdfLaTeX
- **Opcional**: Script bash para `compilar.sh`

### Instalación en Ubuntu/Debian
```bash
sudo apt-get install texlive-full
```

---

## 📋 Estructura de un Documento

```latex
% 1. Información del documento
\def\documenttitle {Mi Título}
\def\documentauthor {Mi Nombre}
...

% 2. Importar plantilla
\input{plantilla_src/template}

% 3. Iniciar documento
\begin{document}
\templatePortrait      % Portada
\templatePagecfg       % Configuración
\begin{abstractd}      % Resumen
...
\end{abstractd}
\templateIndex         % Tabla de contenidos
\templateFinalcfg      % Config. final

% 4. Tu contenido
\section{Introducción}
...

% 5. Cerrar
\end{document}
```

---

## 🎓 Casos de Uso

### Tareas del Curso
Ideal para entregas de tareas con formato profesional

### Proyectos de Investigación
Estructura clara para documentar investigaciones

### Informes de Laboratorio
Secciones predefinidas para metodología y resultados

### Trabajos Finales
Base profesional para documentos extensos

---

## 💡 Ejemplos Rápidos

### Insertar una Ecuación
```latex
\begin{equation}
    E = mc^2
\end{equation}
```

### Insertar una Figura
```latex
\insertimage[\label{fig:ejemplo}]{imagen.png}{width=12cm}{Mi figura}
```

### Crear una Tabla
```latex
\begin{table}[htbp]
\centering
\caption{Resultados}
\begin{tabular}{|c|c|}
\hline
A & B \\
\hline
1 & 2 \\
\hline
\end{tabular}
\end{table}
```

### Definir un Teorema
```latex
\begin{teo}[Pitágoras]
En un triángulo rectángulo, $a^2 + b^2 = c^2$
\end{teo}
```

---

## 🆘 Ayuda

**¿Primera vez usando LaTeX?**
→ Lee primero [GUIA_RAPIDA.md](GUIA_RAPIDA.md)

**¿Quieres personalizar el diseño?**
→ Consulta [README.md](README.md) sección "Configuración de la Plantilla"

**¿Error al compilar?**
→ Revisa [GUIA_RAPIDA.md](GUIA_RAPIDA.md) sección "Solución de Problemas"

**¿Necesitas ver la estructura?**
→ Consulta [CONTENIDO.md](CONTENIDO.md)

---

## 📊 Estadísticas

- 📄 **615 líneas** de documentación
- 🗂️ **~50 archivos** de plantilla
- 💾 **2.1 MB** tamaño total
- ✅ **100% funcional** y probado

---

## 📝 Créditos

**Plantilla Original**: Pablo Pizarro R.
**Licencia**: MIT
**Adaptación**: Universidad Nacional de Colombia
**Versión**: 2025

---

## 🔗 Enlaces Útiles

- [Overleaf](https://www.overleaf.com) - Editor LaTeX online
- [Detexify](http://detexify.kirelabs.org) - Encuentra símbolos LaTeX
- [Tables Generator](https://www.tablesgenerator.com) - Generador de tablas

---

**¡Listo para empezar!** 🎉

Copia `plantilla_vacia.tex`, edita tu información y compila.
Consulta la documentación cuando necesites ayuda.
