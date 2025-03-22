import simulation
import analysis
import data_logger
import visualization
import matplotlib.pyplot as plt
import numpy as np

def main():
    num_bits = 10000  # Number of bits to simulate
    bits = simulation.generate_random_bits(num_bits)
    
    # Perform Analysis Tests
    freq_result = analysis.frequency_test(bits)
    runs_result = analysis.runs_test(bits)
    lag = 1
    autocorr_result = analysis.autocorrelation_test(bits, lag)
    entropy_result = analysis.calculate_entropy(bits)
    
    # Print analysis results to the console
    print(f"Frequency test result (normalized difference): {freq_result:.4f}")
    print("Runs Test Result:")
    for key, value in runs_result.items():
        print(f"  {key}: {value}")
    print(f"Autocorrelation (lag={lag}): {autocorr_result:.4f}")
    print(f"Entropy of the bit sequence: {entropy_result:.4f}")
    
    # Prepare a dictionary of analysis results for logging
    analysis_results = {
        "frequency_test": freq_result,
        "runs_test": runs_result,
        "autocorrelation_lag_1": autocorr_result,
        "entropy": entropy_result
    }
    
    # Data Logging: Save bits and analysis results to files
    data_logger.save_bits_to_csv(bits, "simulation_bits.csv")
    data_logger.log_analysis_results(analysis_results, "analysis_results.json")
    
    # Enhanced Visualization
    visualization.plot_bit_distribution(bits)
    
    # Plot autocorrelation over a range of lags (e.g., 1 to 10)
    lags = np.arange(1, 11)
    autocorr_values = [analysis.autocorrelation_test(bits, lag) for lag in lags]
    visualization.plot_autocorrelation(lags, autocorr_values)
    
    # Plot runs comparison using the runs test results
    observed_runs = runs_result.get("runs")
    expected_runs = runs_result.get("expected_runs")
    visualization.plot_runs_comparison(observed_runs, expected_runs)

if __name__ == '__main__':
    main()
