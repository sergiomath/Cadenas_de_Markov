# Instrucciones para Overleaf

## Cómo cargar el proyecto en Overleaf

### Opción 1: Subir como ZIP
1. Comprimir toda la carpeta `Tarea_1/` en un archivo ZIP
2. En Overleaf: `New Project` → `Upload Project`
3. Seleccionar el archivo ZIP
4. Overleaf descomprimirá y configurará automáticamente el proyecto

### Opción 2: Subir manualmente
1. Crear un nuevo proyecto en blanco en Overleaf
2. Subir las siguientes carpetas y archivos:
   - `main.tex` (archivo principal)
   - Carpeta `plantilla_src/` completa
   - Carpeta `img/` completa
   - Carpeta `src/` (opcional, solo para referencia del código)

## Configuración en Overleaf

- **Compilador**: pdfLaTeX (seleccionar en el menú de configuración)
- **Archivo principal**: `main.tex` (debe estar configurado automáticamente)
- **Modo de compilación**: Auto-compile (opcional, para compilar al guardar)

## Estructura de archivos necesaria

```
Tarea_1/
├── main.tex                    # Documento principal (REQUERIDO)
├── plantilla_src/              # Plantilla LaTeX (REQUERIDA)
│   ├── template.tex           # Configuración de la plantilla
│   ├── cfg/                   # Configuraciones
│   ├── cmd/                   # Comandos personalizados
│   ├── env/                   # Entornos
│   ├── etc/
│   │   └── contenido.tex     # Contenido del informe (IMPORTANTE)
│   ├── page/                  # Configuración de páginas
│   └── style/                 # Estilos
├── img/                        # Imágenes (REQUERIDAS)
│   ├── figuras/               # 11 figuras experimentales
│   ├── Logotipounal2.png      # Logo institucional
│   └── departamentos/
│       └── unal.png           # Logo departamento
└── src/                        # Código Python (opcional)
```

## Compilación

Overleaf compilará automáticamente el documento al abrir el proyecto. Si necesitas recompilar manualmente, usa el botón "Recompile" en la interfaz.

**Nota**: La primera compilación puede tardar unos segundos debido al tamaño de las imágenes (577 KB de figuras).

## Edición del contenido

Para modificar el contenido del informe, editar el archivo:
```
plantilla_src/etc/contenido.tex
```

Este archivo contiene todas las secciones del documento:
- Introducción
- Marco Teórico
- Resultados
- Discusión
- Conclusiones

## Metadatos del documento

Para modificar autores, título, o información del curso, editar `main.tex`:
- Líneas 9-11: Título y tema
- Líneas 13-15: Autores y curso
- Líneas 17-22: Información institucional
- Líneas 25-44: Tabla de autores y fecha

## Solución de problemas

### Error: "File not found"
- Verificar que todas las carpetas fueron subidas correctamente
- Verificar que la estructura de carpetas sea idéntica a la mostrada arriba

### Error: "Undefined control sequence"
- Asegurar que `plantilla_src/template.tex` existe
- Verificar que todas las subcarpetas de `plantilla_src/` fueron subidas

### Error: "Missing figure"
- Verificar que la carpeta `img/` y todas sus subcarpetas fueron subidas
- Verificar que las 11 imágenes en `img/figuras/` están presentes

### Compilación lenta
- Normal en la primera compilación debido a las imágenes
- Las compilaciones subsecuentes serán más rápidas (caché de Overleaf)

## Tamaño del proyecto

- **Documento PDF**: ~960 KB (20 páginas)
- **Figuras**: 577 KB (11 imágenes PNG)
- **Total del proyecto**: ~1.5 MB aproximadamente

Este tamaño está dentro de los límites de un proyecto gratuito de Overleaf.
