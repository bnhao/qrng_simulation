import numpy as np
import csv
import json
from datetime import datetime

def save_bits_to_csv(bits: np.ndarray, filename: str):
    """
    Save the generated bit sequence to a CSV file.
    
    Args:
        bits (np.ndarray): Array of bits (0s and 1s).
        filename (str): The name of the CSV file to save the data.
    """
    # Open the file in write mode
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Index", "Bit"])
        for idx, bit in enumerate(bits):
            writer.writerow([idx, bit])
    print(f"Bit sequence saved to {filename}")

def log_analysis_results(results: dict, filename: str):
    """
    Save the analysis results to a JSON file with a timestamp.
    
    Args:
        results (dict): Dictionary containing analysis results.
        filename (str): The name of the JSON file to save the data.
    """
    # Add a timestamp to the results
    results["timestamp"] = datetime.now().isoformat()
    with open(filename, 'w') as file:
        json.dump(results, file, indent=4)
    print(f"Analysis results saved to {filename}")

# Test the logger if running this module directly
if __name__ == '__main__':
    import simulation
    bits = simulation.generate_random_bits(100)
    save_bits_to_csv(bits, "test_bits.csv")
    sample_results = {"frequency": 0.02, "runs": 45}
    log_analysis_results(sample_results, "test_results.json")
