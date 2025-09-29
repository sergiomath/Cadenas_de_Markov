#!/usr/bin/env python3
"""
Script de diagnóstico GPU para verificar la disponibilidad de CUDA y CuPy
"""

import sys
import subprocess

def run_command(cmd):
    """Ejecutar comando y devolver resultado"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except Exception as e:
        return "", str(e), -1

def check_nvidia_driver():
    """Verificar driver NVIDIA"""
    print("=== VERIFICANDO DRIVER NVIDIA ===")
    stdout, stderr, code = run_command("nvidia-smi")
    if code == 0:
        print("✅ Driver NVIDIA instalado correctamente")
        lines = stdout.split('\n')
        for line in lines:
            if 'CUDA Version' in line:
                cuda_version = line.split('CUDA Version:')[1].strip().split()[0]
                print(f"📌 Versión CUDA soportada: {cuda_version}")
    else:
        print("❌ Driver NVIDIA no encontrado o error")
        print(f"Error: {stderr}")
    print()

def check_cupy_installation():
    """Verificar instalación de CuPy"""
    print("=== VERIFICANDO CUPY ===")
    try:
        import cupy as cp
        print("✅ CuPy importado correctamente")

        # Verificar dispositivos CUDA
        n_devices = cp.cuda.runtime.getDeviceCount()
        print(f"📌 Dispositivos CUDA detectados: {n_devices}")

        if n_devices > 0:
            for i in range(n_devices):
                props = cp.cuda.runtime.getDeviceProperties(i)
                name = props['name'].decode()
                total_mem_gb = props['totalGlobalMem'] // (1024**3)
                print(f"   GPU {i}: {name} ({total_mem_gb} GB)")

        # Verificar versión CUDA runtime
        cuda_runtime = cp.cuda.runtime.runtimeGetVersion()
        print(f"📌 CUDA Runtime Version: {cuda_runtime // 1000}.{(cuda_runtime % 100) // 10}")

        # Test básico
        print("🧪 Ejecutando test básico...")
        a = cp.array([1, 2, 3])
        b = cp.array([4, 5, 6])
        c = a + b
        result = cp.asnumpy(c)
        print(f"   Test: [1,2,3] + [4,5,6] = {result}")
        print("✅ Test básico exitoso")

        return True

    except ImportError as e:
        print("❌ CuPy no está instalado")
        print(f"Error: {e}")
        return False
    except Exception as e:
        print("❌ Error al usar CuPy")
        print(f"Error: {e}")
        return False
    finally:
        print()

def check_markov_gpu():
    """Verificar funciones GPU del proyecto"""
    print("=== VERIFICANDO FUNCIONES GPU DEL PROYECTO ===")
    try:
        sys.path.append('.')
        from src.markov_matrix import GPU_AVAILABLE, crear_matriz_probabilidad

        print(f"📌 GPU_AVAILABLE = {GPU_AVAILABLE}")

        if GPU_AVAILABLE:
            from src.markov_matrix import (
                calcular_distribucion_metodo_autovalores_gpu,
                calcular_distribucion_metodo_tiempo_retorno_gpu
            )

            # Test con matriz pequeña
            print("🧪 Ejecutando test con matriz 4x4...")
            matriz = crear_matriz_probabilidad(4, 0.6)

            # Método 1 GPU
            pi1 = calcular_distribucion_metodo_autovalores_gpu(matriz)
            print(f"   Método 1 GPU: {pi1}")

            # Método 2 GPU
            pi2 = calcular_distribucion_metodo_tiempo_retorno_gpu(matriz)
            print(f"   Método 2 GPU: {pi2}")

            print("✅ Funciones GPU funcionando correctamente")
        else:
            print("❌ GPU no disponible en el proyecto")

    except Exception as e:
        print("❌ Error al probar funciones GPU del proyecto")
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    print()

def check_python_environment():
    """Verificar entorno Python"""
    print("=== VERIFICANDO ENTORNO PYTHON ===")
    print(f"📌 Python version: {sys.version}")
    print(f"📌 Python executable: {sys.executable}")

    # Verificar paquetes instalados
    try:
        import numpy as np
        print(f"📌 NumPy version: {np.__version__}")
    except ImportError:
        print("❌ NumPy no instalado")

    print()

def main():
    print("🔍 DIAGNÓSTICO GPU PARA CADENAS DE MARKOV")
    print("=" * 50)

    check_python_environment()
    check_nvidia_driver()
    cupy_ok = check_cupy_installation()
    check_markov_gpu()

    print("=== RESUMEN ===")
    if cupy_ok:
        print("✅ Tu RTX 5060 debería funcionar correctamente")
        print("💡 Si aún hay problemas, reinicia el kernel/terminal")
    else:
        print("❌ Problemas detectados con CuPy")
        print("💡 Solución sugerida:")
        print("   pip install cupy-cuda12x")
    print()

if __name__ == "__main__":
    main()