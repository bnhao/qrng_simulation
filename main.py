import simulation
import analysis
import matplotlib.pyplot as plt

def main():
    num_bits = 10000  # Number of bits to generate for the simulation
    bits = simulation.generate_random_bits(num_bits)
    
    # Run the frequency test on the generated bits
    freq_result = analysis.frequency_test(bits)
    print(f"Frequency test result (normalized difference): {freq_result:.4f}")

    run_results = analysis.runs_test(bits);
    print(f"Runs test result: {run_results['runs']}")

    # Visualize the distribution of generated bits with a histogram
    plt.hist(bits, bins=2, edgecolor='black', rwidth=0.7)
    plt.title('Distribution of Generated Random Bits')
    plt.xlabel('Bit Value')
    plt.ylabel('Count')
    plt.xticks([0, 1])
    plt.show()

if __name__ == '__main__':
    main()
