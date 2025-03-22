import simulation
import analysis
import data_logger
import visualization
import external_api
import numpy as np
import matplotlib.pyplot as plt

def analyze_simulated_data(num_bits):
    """
    Analyze and visualize simulated QRNG data.
    """
    # Generate simulated random bits
    sim_bits = simulation.generate_random_bits(num_bits)
    
    # Perform Analysis on Simulated Data
    sim_freq = analysis.frequency_test(sim_bits)
    sim_runs = analysis.runs_test(sim_bits)
    sim_autocorr = analysis.autocorrelation_test(sim_bits, lag=1)
    sim_entropy = analysis.calculate_entropy(sim_bits)
    
    # Print simulated data analysis results
    print("Simulated Data Analysis:")
    print(f"  Frequency test (normalized difference): {sim_freq:.4f}")
    print("  Runs test:", sim_runs)
    print(f"  Autocorrelation (lag=1): {sim_autocorr:.4f}")
    print(f"  Entropy: {sim_entropy:.4f}")
    
    # Log simulated data to separate files
    data_logger.save_bits_to_csv(sim_bits, "simulated_bits.csv")
    sim_analysis_results = {
        "frequency_test": sim_freq,
        "runs_test": sim_runs,
        "autocorrelation_lag_1": sim_autocorr,
        "entropy": sim_entropy
    }
    data_logger.log_analysis_results(sim_analysis_results, "simulated_analysis_results.json")
    
    # Enhanced Visualization for Simulated Data
    visualization.plot_bit_distribution(sim_bits, title="Simulated Data Bit Distribution")
    
    lags = np.arange(1, 11)
    sim_autocorr_values = [analysis.autocorrelation_test(sim_bits, lag) for lag in lags]
    visualization.plot_autocorrelation(lags, sim_autocorr_values, title="Simulated Data Autocorrelation")
    
    visualization.plot_runs_comparison(sim_runs.get("runs"), sim_runs.get("expected_runs"),
                                       title="Simulated Data: Observed vs. Expected Runs")
    
    return sim_bits

def analyze_external_data(num_bits):
    """
    Fetch, analyze, and visualize external QRNG data.
    """
    print("\nFetching external quantum random numbers...")
    ext_bits = external_api.fetch_external_random_numbers(num_bits)
    
    if ext_bits.size == 0:
        print("No external data was fetched.")
        return None
    
    # Perform Analysis on External Data
    ext_freq = analysis.frequency_test(ext_bits)
    ext_runs = analysis.runs_test(ext_bits)
    ext_autocorr = analysis.autocorrelation_test(ext_bits, lag=1)
    ext_entropy = analysis.calculate_entropy(ext_bits)
    
    # Print external data analysis results
    print("\nExternal Data Analysis:")
    print(f"  Frequency test (normalized difference): {ext_freq:.4f}")
    print("  Runs test:", ext_runs)
    print(f"  Autocorrelation (lag=1): {ext_autocorr:.4f}")
    print(f"  Entropy: {ext_entropy:.4f}")
    
    # Log external data to separate files
    data_logger.save_bits_to_csv(ext_bits, "external_bits.csv")
    ext_analysis_results = {
        "frequency_test": ext_freq,
        "runs_test": ext_runs,
        "autocorrelation_lag_1": ext_autocorr,
        "entropy": ext_entropy
    }
    data_logger.log_analysis_results(ext_analysis_results, "external_analysis_results.json")
    
    # Enhanced Visualization for External Data with distinct titles
    visualization.plot_bit_distribution(ext_bits, title="External QRNG Data Bit Distribution")
    
    lags = np.arange(1, 11)
    ext_autocorr_values = [analysis.autocorrelation_test(ext_bits, lag) for lag in lags]
    visualization.plot_autocorrelation(lags, ext_autocorr_values, title="External Data Autocorrelation")
    
    visualization.plot_runs_comparison(ext_runs.get("runs"), ext_runs.get("expected_runs"),
                                       title="External Data: Observed vs. Expected Runs")
    
    return ext_bits

def main():
    num_bits = 10000  # Number of bits to simulate or fetch
    
    # --- Process Simulated Data ---
    sim_bits = analyze_simulated_data(num_bits)
    
    # --- Process External Data ---
    ext_bits = analyze_external_data(num_bits)

if __name__ == '__main__':
    main()
