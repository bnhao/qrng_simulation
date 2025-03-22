import matplotlib.pyplot as plt

def plot_bit_distribution(bits, title="Bit Distribution"):
    plt.figure()
    plt.hist(bits, bins=2, edgecolor='black', rwidth=0.7)
    plt.title(title)
    plt.xlabel('Bit Value')
    plt.ylabel('Count')
    plt.xticks([0, 1])
    plt.show()

def plot_autocorrelation(lag_values, autocorr_values, title="Autocorrelation"):
    plt.figure()
    plt.plot(lag_values, autocorr_values, marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel('Lag')
    plt.ylabel('Autocorrelation Coefficient')
    plt.grid(True)
    plt.show()

def plot_runs_comparison(observed_runs, expected_runs, title="Runs Comparison"):
    plt.figure()
    labels = ['Observed', 'Expected']
    values = [observed_runs, expected_runs]
    plt.bar(labels, values, color=['blue', 'green'])
    plt.title(title)
    plt.ylabel('Number of Runs')
    plt.show()
