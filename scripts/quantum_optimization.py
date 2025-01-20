from dwave.system import LeapHybridSampler

def quantum_optimization(qubo):
    """
    Run QUBO problem on a quantum annealer.
    
    Parameters:
        qubo (dict): QUBO problem definition in dictionary format.
                     Keys are tuples of variable indices, and values are coefficients.
    
    Returns:
        dimod.SampleSet: Results from the quantum annealer, including solutions and energies.
    """
    print("Initializing the quantum sampler...")
    sampler = LeapHybridSampler()  # Connect to the D-Wave quantum sampler
    
    print("Submitting QUBO to the quantum annealer...")
    response = sampler.sample_qubo(qubo)  # Solve the QUBO problem
    
    print("Quantum optimization completed. Processing results...\n")
    return response

# Example Usage
if __name__ == "__main__":
    # Example QUBO problem
    qubo = {
        ('Position_1', 'Position_1'): -0.1,  # Self-loop (diagonal term)
        ('Position_1', 'Position_2'): 0.05,  # Interaction between Position_1 and Position_2
        ('Position_2', 'Position_2'): -0.2   # Self-loop (diagonal term)
    }
    
    # Run quantum optimization
    result = quantum_optimization(qubo)
    
    # Display results
    print("Quantum Optimization Results:")
    for sample, energy in result.data(['sample', 'energy']):
        print(f"Sample: {sample}, Energy: {energy}")
