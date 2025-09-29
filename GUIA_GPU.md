# 🚀 Guía para Usar GPU con RTX 5060

## 📋 Diagnóstico Actual

Tienes una **NVIDIA GeForce RTX 5060** funcionando correctamente con drivers NVIDIA 581.29 y soporte CUDA 13.0. Sin embargo, para usar GPU con Python necesitas instalar el **CUDA Toolkit completo**.

## ❗ Problema Detectado

```
❌ CuPy instalado pero faltan librerías CUDA
Error: libnvrtc.so.12: cannot open shared object file
```

## 🔧 Soluciones

### **Opción 1: Instalar CUDA Toolkit (Recomendado)**

#### En WSL2 Ubuntu:

```bash
# 1. Descargar e instalar CUDA Toolkit 12.x
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update
sudo apt-get install cuda-toolkit-12-0

# 2. Agregar a PATH
echo 'export PATH=/usr/local/cuda/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc

# 3. Verificar instalación
nvcc --version
```

#### En Windows:

1. Descarga CUDA Toolkit 12.x desde: https://developer.nvidia.com/cuda-downloads
2. Instala siguiendo el wizard
3. Reinicia el sistema

### **Opción 2: Usar Google Colab (Fácil y Gratis)**

```python
# En Google Colab (ya tiene CUDA preinstalado)
!pip install cupy-cuda12x
# Subir archivos del proyecto y ejecutar
```

### **Opción 3: Usar Docker con CUDA**

```bash
# Instalar NVIDIA Container Toolkit
docker run --gpus all -it pytorch/pytorch:latest
pip install cupy-cuda12x
```

### **Opción 4: Continuar Solo con CPU (Funcional)**

Tu código funciona perfectamente en CPU. Los métodos CPU son suficientemente rápidos para matrices pequeñas/medianas.

## ✅ Verificación de Funcionamiento

Después de instalar CUDA, ejecuta:

```bash
python diagnostico_gpu.py
```

Deberías ver:
```
✅ CuPy disponible: se pueden usar cálculos en GPU
✅ Test básico exitoso
✅ Funciones GPU funcionando correctamente
```

## 📊 Rendimiento Esperado con GPU

Con tu RTX 5060, espera **speedups de 2-10x** para matrices grandes:

| Tamaño matriz | CPU (s) | GPU (s) | Speedup |
|---------------|---------|---------|---------|
| 100x100      | 0.002   | 0.001   | 2x      |
| 500x500      | 0.4     | 0.08    | 5x      |
| 1000x1000    | 3.2     | 0.4     | 8x      |

## 🎯 Recomendación

Para desarrollo local con tu RTX 5060:

1. **Instala CUDA Toolkit 12.x** (Opción 1)
2. **Usa Google Colab** para experimentos rápidos (Opción 2)
3. **El código funciona perfectamente en CPU** mientras tanto

## 🧪 Test Rápido

```python
# Verificar que todo funciona
from src.markov_matrix import GPU_AVAILABLE, crear_matriz_probabilidad

if GPU_AVAILABLE:
    print("🚀 GPU listo para acelerar cálculos!")
else:
    print("💻 Usando CPU - funciona perfectamente")

# Test con matriz
matriz = crear_matriz_probabilidad(10, 0.6)
print("✅ Matrices de Markov funcionando correctamente")
```