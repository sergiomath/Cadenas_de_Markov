import sys
import os
sys.path.insert(0, os.path.abspath('.'))

try:
    from src.ising_model_gpu import run_mcmc_experiment_gpu, run_propp_wilson_experiment_gpu, GPU_AVAILABLE
    
    if not GPU_AVAILABLE:
        print("GPU no disponible. Saltando prueba.")
        sys.exit(0)
        
    print("Probando MCMC GPU...")
    res_mcmc = run_mcmc_experiment_gpu(K=10, beta=0.4, n_samples=10, burn_in=100, thin=10)
    print(f"MCMC OK. Mag: {res_mcmc['magnetization_mean']:.4f}, Time: {res_mcmc['elapsed_time']:.4f}s")
    
    print("\nProbando Propp-Wilson GPU...")
    res_pw = run_propp_wilson_experiment_gpu(K=10, beta=0.4, n_samples=5, max_time=1000)
    print(f"PW OK. Mag: {res_pw['magnetization_mean']:.4f}, Time: {res_pw['elapsed_time']:.4f}s")
    print(f"Tiempos de coalescencia: {res_pw['coalescence_times']}")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
