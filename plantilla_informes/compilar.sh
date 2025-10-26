#!/bin/bash

# Script de compilación para Template-Informe UNAL
# Autor: Template adaptado para Universidad Nacional de Colombia

echo "======================================"
echo "  Compilador Template-Informe UNAL"
echo "======================================"
echo ""

# Verificar que existe main.tex
if [ ! -f "main.tex" ]; then
    echo "❌ Error: No se encuentra main.tex"
    echo "   Asegúrate de estar en el directorio raíz del proyecto"
    exit 1
fi

# Compilación
echo "📝 Compilando documento (1/3)..."
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1

echo "📝 Compilando documento (2/3)..."
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1

echo "📝 Compilando documento (3/3)..."
pdflatex -interaction=nonstopmode main.tex

# Verificar si se generó el PDF
if [ -f "main.pdf" ]; then
    echo ""
    echo "✅ ¡Compilación exitosa!"
    echo "📄 Documento generado: main.pdf"

    # Mostrar información del PDF
    if command -v pdfinfo &> /dev/null; then
        echo ""
        echo "Información del PDF:"
        pdfinfo main.pdf 2>/dev/null | grep -E "Pages|File size|Producer"
    fi
else
    echo ""
    echo "❌ Error en la compilación"
    echo "   Revisa main.log para más detalles"
    exit 1
fi

# Preguntar si limpiar archivos temporales
echo ""
read -p "¿Deseas limpiar archivos temporales? (s/N): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[SsYy]$ ]]; then
    echo "🧹 Limpiando archivos temporales..."
    rm -f *.aux *.log *.toc *.out *.lof *.lot *.lol *.bbl *.blg *.synctex.gz
    echo "✅ Limpieza completada"
fi

echo ""
echo "======================================"
echo "  ¡Proceso finalizado!"
echo "======================================"
