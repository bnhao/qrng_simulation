import numpy as np
from scipy.stats import norm

def frequency_test(bits: np.ndarray) -> float:
    """
    Perform a basic frequency (monobit) test on the generated bits.
    This test calculates the normalized absolute difference between the count
    of 1s and 0s. A value near zero indicates balanced randomness.

    Args:
        bits (np.ndarray): Array of bits (0s and 1s).

    Returns:
        float: Normalized absolute difference between counts of 1s and 0s.
    """
    n = len(bits)
    count_ones = np.sum(bits)
    count_zeros = n - count_ones
    normalized_diff = abs(count_ones - count_zeros) / n
    return normalized_diff




def runs_test(bits: np.ndarray) -> dict:
    """
    Perform the runs test on a sequence of bits.
    
    Args:
        bits (np.ndarray): Array of bits (0s and 1s).

    Returns:
        dict: A dictionary containing:
              - 'runs': Observed number of runs.
              - 'expected_runs': Expected number of runs.
              - 'z_value': Z-statistic for the test.
              - 'p_value': p-value for the z statistic.
    """
    n = len(bits)
    n1 = np.sum(bits)
    n0 = n - n1

    # Check if we have enough variation in the data
    if n1 == 0 or n0 == 0:
        return {"error": "Runs test cannot be performed because the bit sequence lacks variation."}

    # Count the observed number of runs
    runs = 1
    for i in range(1, n):
        if bits[i] != bits[i - 1]:
            runs += 1

    # Calculate expected number of runs and variance
    expected_runs = ((2 * n1 * n0) / n) + 1
    numerator = 2 * n1 * n0 * (2 * n1 * n0 - n)
    denominator = (n ** 2) * (n - 1)
    variance_runs = numerator / denominator if denominator != 0 else 0

    # Compute z statistic
    z_value = (runs - expected_runs) / np.sqrt(variance_runs) if variance_runs > 0 else 0

    # Two-tailed p-value
    p_value = 2 * (1 - norm.cdf(abs(z_value)))

    return {
        "runs": runs,
        "expected_runs": expected_runs,
        "z_value": z_value,
        "p_value": p_value
    }

# Test the frequency test if running this file directly
if __name__ == '__main__':
    from simulation import generate_random_bits
    bits = generate_random_bits(10)
    result = frequency_test(bits)
    print("Frequency Test Result:", result)

    run_results = runs_test(bits)
    print(f"Runs test result: {run_results['runs']}")
