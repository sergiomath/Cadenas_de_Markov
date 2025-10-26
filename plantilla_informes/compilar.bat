@echo off
REM Script de compilación para Template-Informe UNAL
REM Autor: Template adaptado para Universidad Nacional de Colombia

echo ======================================
echo   Compilador Template-Informe UNAL
echo ======================================
echo.

REM Verificar que existe main.tex
if not exist main.tex (
    echo X Error: No se encuentra main.tex
    echo   Asegurate de estar en el directorio raiz del proyecto
    pause
    exit /b 1
)

REM Compilación
echo Compilando documento (1/3)...
pdflatex -interaction=nonstopmode main.tex > nul 2>&1

echo Compilando documento (2/3)...
pdflatex -interaction=nonstopmode main.tex > nul 2>&1

echo Compilando documento (3/3)...
pdflatex -interaction=nonstopmode main.tex

REM Verificar si se generó el PDF
if exist main.pdf (
    echo.
    echo [OK] Compilacion exitosa!
    echo PDF  Documento generado: main.pdf
) else (
    echo.
    echo X Error en la compilacion
    echo   Revisa main.log para mas detalles
    pause
    exit /b 1
)

REM Preguntar si limpiar archivos temporales
echo.
set /p CLEAN="Deseas limpiar archivos temporales? (S/N): "

if /i "%CLEAN%"=="S" (
    echo Limpiando archivos temporales...
    del /Q *.aux *.log *.toc *.out *.lof *.lot *.lol *.bbl *.blg *.synctex.gz 2>nul
    echo [OK] Limpieza completada
)

echo.
echo ======================================
echo   Proceso finalizado!
echo ======================================
echo.
pause
