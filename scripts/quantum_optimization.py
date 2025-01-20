from dwave.system import LeapHybridSampler
import json
import os

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
    if not isinstance(qubo, dict) or not all(isinstance(k, tuple) and len(k) == 2 for k in qubo.keys()):
        raise ValueError("Invalid QUBO format. Keys must be tuples of two indices, and values must be coefficients.")

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

        print(f"Submitting QUBO with {len(qubo)} terms to the quantum annealer...")
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

def save_results(response, filename="data/quantum_optimization_results.json"):
    """
    Save quantum optimization results to a JSON file in the data folder.

    Parameters:
        response: The result set from the quantum annealer or mock results.
        filename (str): The file to save the results.
    """
    if response is None:
        print("No results to save.")
        return

    # Ensure the data folder exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    print(f"Saving results to {filename}...")
    try:
        if USE_MOCK_QUANTUM:
            with open(filename, "w") as f:
                json.dump(response, f, indent=4)
        else:
            # Convert response to Python types
            response_dict = [
                {"sample": {k: int(v) for k, v in sample.items()}, "energy": float(energy)}
                for sample, energy in response.data(['sample', 'energy'])
            ]
            with open(filename, "w") as f:
                json.dump(response_dict, f, indent=4)
        print(f"Results saved successfully to {filename}.")
    except Exception as e:
        print(f"Error while saving results: {e}")

# Example Integration
if __name__ == "__main__":
    from scripts.data_ingestion import get_data

    # Toggle between real and mock quantum optimization
    USE_MOCK_QUANTUM = False  # Set this to True for mock results, False for real quantum optimization

    # Fetch market data
    ticker = "AAPL US Equity"
    start_time = "2024-12-29T09:30:00"
    end_time = "2024-12-29T16:00:00"
    data = get_data(ticker, start_time, end_time)

    # Example: Prepare a simple QUBO problem based on fetched data (using close prices as an example)
    close_prices = data['close'].values[:3]  # Use a subset of prices for QUBO example
    qubo = {
        ('Position_1', 'Position_1'): -close_prices[0],
        ('Position_1', 'Position_2'): close_prices[1],
        ('Position_2', 'Position_2'): -close_prices[2]
    }

    # Solve the QUBO problem
    print(f"Running quantum optimization with USE_MOCK_QUANTUM = {USE_MOCK_QUANTUM}")
    result = quantum_optimization(qubo)

    # Display results
    display_results(result)

    # Save results
    save_results(result, "data/quantum_optimization_results.json")
