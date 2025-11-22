#!/usr/bin/env python
"""
Script de verificación rápida para los notebooks de Tarea 2.
Simula la ejecución de las celdas principales de ambos notebooks.
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

print("="*70)
print("VERIFICACIÓN DE NOTEBOOKS - TAREA 2")
print("="*70)

# Test 1: Importaciones
print("\n[1/5] Verificando importaciones...")
try:
    from src.mcmc_counting import (
        LatticeGraph,
        QColoringMCMC,
        HardCoreMCMC,
        MCMCConfig,
        QColoringApproximation,
        HardCoreApproximation,
        exact_q_colorings_small,
        exact_hardcore_small,
        exact_chromatic_polynomial,
        exact_hardcore_count,
        run_q_coloring_experiment,
        run_hardcore_experiment
    )
    print("   ✓ Todas las importaciones exitosas")
except Exception as e:
    print(f"   ✗ Error en importaciones: {e}")
    sys.exit(1)

# Test 2: Crear Lattice y configuración
print("\n[2/5] Creando objetos básicos...")
try:
    lattice = LatticeGraph(3)
    config = MCMCConfig(epsilon=0.5, num_samples=10)
    print(f"   ✓ Lattice 3x3: {lattice.n_vertices} vértices, grado máx {lattice.max_degree()}")
    print(f"   ✓ Config: ε={config.epsilon}, muestras={config.num_samples}")
except Exception as e:
    print(f"   ✗ Error: {e}")
    sys.exit(1)

# Test 3: Q-Coloring básico
print("\n[3/5] Probando Q-Coloring MCMC...")
try:
    qcolor = QColoringMCMC(lattice, q=9, config=config)
    estimate, stats = qcolor.count_approximate(verbose=False)
    print(f"   ✓ Estimación: {estimate:.2e}")
    print(f"   ✓ Simulaciones: {stats['num_simulations']}")
except Exception as e:
    print(f"   ✗ Error: {e}")
    sys.exit(1)

# Test 4: Hard-Core básico
print("\n[4/5] Probando Hard-Core MCMC...")
try:
    hardcore = HardCoreMCMC(lattice, config=config)
    hc_estimate, hc_stats = hardcore.count_approximate(verbose=False)
    print(f"   ✓ Estimación HC: {hc_estimate:.2e}")
    print(f"   ✓ Tiempo de mezcla: {hc_stats['mixing_time']}")
except Exception as e:
    print(f"   ✗ Error: {e}")
    sys.exit(1)

# Test 5: Conteo exacto
print("\n[5/5] Probando conteo exacto...")
try:
    exact_q = exact_q_colorings_small(2, 3)
    exact_hc = exact_hardcore_small(2)
    print(f"   ✓ Q-coloring exacto (K=2, q=3): {exact_q}")
    print(f"   ✓ Hard-Core exacto (K=2): {exact_hc}")
except Exception as e:
    print(f"   ✗ Error: {e}")
    sys.exit(1)

# Resumen final
print("\n" + "="*70)
print("✅ TODOS LOS TESTS PASARON - LOS NOTEBOOKS ESTÁN LISTOS")
print("="*70)
print("\nPuedes ejecutar los notebooks con:")
print("  - Jupyter Notebook: jupyter notebook notebooks/")
print("  - JupyterLab: jupyter lab notebooks/")
print("  - VSCode: Abrir directamente los archivos .ipynb")
