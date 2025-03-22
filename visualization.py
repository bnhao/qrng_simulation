import matplotlib.pyplot as plt

def plot_bit_distribution(bits):
    """
    Plot a histogram of the bit distribution.
    
    Args:
        bits (array-like): Sequence of bits.
    """
    plt.figure()
    plt.hist(bits, bins=2, edgecolor='black', rwidth=0.7)
    plt.title('Distribution of Generated Random Bits')
    plt.xlabel('Bit Value')
    plt.ylabel('Count')
    plt.xticks([0, 1])
    plt.show()

def plot_autocorrelation(lag_values, autocorr_values):
    """
    Plot the autocorrelation coefficients for a range of lag values.
    
    Args:
        lag_values (list or array): The lag values.
        autocorr_values (list or array): The autocorrelation coefficients for each lag.
    """
    plt.figure()
    plt.plot(lag_values, autocorr_values, marker='o', linestyle='-')
    plt.title('Autocorrelation over Different Lags')
    plt.xlabel('Lag')
    plt.ylabel('Autocorrelation Coefficient')
    plt.grid(True)
    plt.show()

def plot_runs_comparison(observed_runs, expected_runs):
    """
    Create a bar chart comparing observed and expected number of runs.
    
    Args:
        observed_runs (int): Observed number of runs.
        expected_runs (float): Expected number of runs.
    """
    plt.figure()
    labels = ['Observed', 'Expected']
    values = [observed_runs, expected_runs]
    plt.bar(labels, values, color=['blue', 'green'])
    plt.title('Observed vs. Expected Number of Runs')
    plt.ylabel('Number of Runs')
    plt.show()
