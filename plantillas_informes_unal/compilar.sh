#!/bin/bash
# Script de compilación para documentos LaTeX
# Universidad Nacional de Colombia

# Colores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Función para imprimir mensajes
print_msg() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

# Verificar que se proporcione un archivo
if [ $# -eq 0 ]; then
    print_error "Uso: $0 <archivo.tex>"
    echo "Ejemplo: $0 main.tex"
    exit 1
fi

ARCHIVO=$1
NOMBRE_BASE="${ARCHIVO%.tex}"

# Verificar que el archivo existe
if [ ! -f "$ARCHIVO" ]; then
    print_error "El archivo $ARCHIVO no existe"
    exit 1
fi

print_msg "Compilando $ARCHIVO..."

# Primera compilación
print_msg "Primera compilación..."
pdflatex -interaction=nonstopmode "$ARCHIVO" > /dev/null 2>&1
if [ $? -ne 0 ]; then
    print_error "Error en la primera compilación"
    print_warning "Ver archivo ${NOMBRE_BASE}.log para detalles"
    exit 1
fi

# Segunda compilación (para tabla de contenidos y referencias)
print_msg "Segunda compilación (tabla de contenidos)..."
pdflatex -interaction=nonstopmode "$ARCHIVO" > /dev/null 2>&1
if [ $? -ne 0 ]; then
    print_error "Error en la segunda compilación"
    print_warning "Ver archivo ${NOMBRE_BASE}.log para detalles"
    exit 1
fi

# Verificar que se generó el PDF
if [ -f "${NOMBRE_BASE}.pdf" ]; then
    TAMAÑO=$(ls -lh "${NOMBRE_BASE}.pdf" | awk '{print $5}')
    print_msg "Compilación exitosa: ${NOMBRE_BASE}.pdf (${TAMAÑO})"

    # Limpiar archivos auxiliares (opcional)
    read -p "¿Deseas limpiar archivos auxiliares (.aux, .log, .out, .toc)? [s/N]: " -n 1 -r
    echo
    if [[ $REPLY =~ ^[SsYy]$ ]]; then
        rm -f "${NOMBRE_BASE}.aux" "${NOMBRE_BASE}.log" "${NOMBRE_BASE}.out" \
              "${NOMBRE_BASE}.toc" "${NOMBRE_BASE}.lof" "${NOMBRE_BASE}.lot"
        print_msg "Archivos auxiliares eliminados"
    fi
else
    print_error "No se generó el archivo PDF"
    exit 1
fi
