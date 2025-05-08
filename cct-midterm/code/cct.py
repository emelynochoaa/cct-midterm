import os
import pandas as pd
import numpy as np
import pymc as pm
import arviz as az
import matplotlib.pyplot as plt

def load_data(fp):
    df = pd.read_csv(fp)
    return df.drop(columns="Informant").to_numpy()

def run_model(data, draws=2000, tune=1000, chains=4):
    N, M = data.shape
    with pm.Model() as model:
        
        D = pm.Uniform("D", lower=0.5, upper=1, shape=N)
        
        Z = pm.Bernoulli("Z", p=0.5, shape=M)
        
        p = Z * D[:, None] + (1 - Z) * (1 - D[:, None])
        
        pm.Bernoulli("X_obs", p=p, observed=data)
        trace = pm.sample(draws=draws, tune=tune, chains=chains,
                          target_accept=0.90, return_inferencedata=True)
    return trace

def show_results(trace, data):

    D_mean = trace.posterior["D"].mean(dim=["chain", "draw"]).values
    print("Posterior Mean Competence (D):")
    for i, d in enumerate(D_mean, start=1):
        print(f"  Informant {i}: {d:.3f}")
    
    Z_mean = trace.posterior["Z"].mean(dim=["chain", "draw"]).values
    print("\nPosterior Mean Consensus Answers (Z):")
    for i, z in enumerate(Z_mean, start=1):
        print(f"  Item {i}: Mean = {z:.3f}, Estimated = {int(round(z))}")
    
    majority = np.round(data.mean(axis=0))
    print("\nMajority Vote (raw data):")
    for i, m in enumerate(majority, start=1):
        print(f"  Item {i}: {int(m)}")
    
    az.plot_posterior(trace, var_names=["D"])  
    plt.title("Posterior for Informant Competence (D)")
    plt.show()

    
    az.plot_posterior(trace, var_names=["Z"])
    plt.title("Posterior for Consensus Answers (Z)")
    plt.show()
    
    print("\nModel Diagnostics Summary:")
    print(az.summary(trace, var_names=["D", "Z"]))

#ChatGPT Acknowledgement: az_plot to plt.show imported from software, with adjustments to suggested "credible_interval" code.

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(script_dir, "..", "data", "plant_knowledge.csv")
    print("Loading data from:", data_path)
    
    if not os.path.exists(data_path):
        print("Error: Data file not found at", data_path)
        exit(1)
    
    try:
        data = load_data(data_path)
        print("Data shape:", data.shape)
    except Exception as e:
        print("Error loading data:", e)
        exit(1)
    #ChatGPT Acknowledgement: "ifnot, try, except" code taken from software to fix "plant_knowledge.csv not found" error. 
    trace = run_model(data)
    show_results(trace, data)
