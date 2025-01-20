from dwave.system import LeapHybridSampler

# Toggle to switch between real and mock quantum optimization
USE_MOCK_QUANTUM = False  # Set to True for mock results, False for real quantum optimization

def quantum_optimization(qubo):
    """
    Run QUBO problem on a quantum annealer or simulate results for demonstration.

    Parameters:
        qubo (dict): QUBO problem definition in dictionary format.
                     Keys are tuples of variable indices, and values are coefficients.

    Returns:
        dict or dimod.SampleSet: Mock results or results from the quantum annealer.
    """
    if USE_MOCK_QUANTUM:
        print("Using mock quantum optimization for demonstration purposes.")
        # Simulated results for demonstration
        return {
            ('Position_1', 'Position_1'): 1,
            ('Position_1', 'Position_2'): 0,
            ('Position_2', 'Position_2'): 1
        }
    
    try:
        print("Initializing the quantum sampler...")
        sampler = LeapHybridSampler()  # Connect to the D-Wave quantum sampler

        print("Submitting QUBO to the quantum annealer...")
        response = sampler.sample_qubo(qubo)  # Solve the QUBO problem

        print("Quantum optimization completed. Processing results...\n")
        return response
    except Exception as e:
        print(f"An error occurred during quantum optimization: {e}")
        return None

def display_results(response):
    """
    Display the results from quantum optimization.

    Parameters:
        response: The result set returned by the quantum annealer or mock results.
    """
    if response is None:
        print("No results to display due to an error during optimization.")
        return

    if USE_MOCK_QUANTUM:
        print("Quantum Optimization Results (Mock):")
        for key, value in response.items():
            print(f"{key}: {value}")
    else:
        print("Quantum Optimization Results:")
        for sample, energy in response.data(['sample', 'energy']):
            print(f"Sample: {sample}, Energy: {energy}")

# Example Usage
if __name__ == "__main__":
    # Toggle between real and mock quantum optimization
    USE_MOCK_QUANTUM = False  # Set this to True for mock results, False for real quantum optimization

    # Define a sample QUBO problem
    qubo = {
        ('Position_1', 'Position_1'): -0.1,  # Self-loop (diagonal term)
        ('Position_1', 'Position_2'): 0.05,  # Interaction term
        ('Position_2', 'Position_2'): -0.2   # Self-loop (diagonal term)
    }

    # Solve the QUBO problem
    print(f"Running quantum optimization with USE_MOCK_QUANTUM = {USE_MOCK_QUANTUM}")
    result = quantum_optimization(qubo)

    # Display results
    display_results(result)
