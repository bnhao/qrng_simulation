import numpy as np

def generate_random_bits(num_bits: int) -> np.ndarray:
    """
    Simulate a beam-splitter event to generate random bits.
    Each event has a 50/50 chance of returning 0 or 1.

    Args:
        num_bits (int): Number of random bits to generate.

    Returns:
        np.ndarray: An array of 0s and 1s.
    """
    # Generate bits using a Bernoulli distribution (p=0.5)
    bits = np.random.binomial(1, 0.5, num_bits)
    return bits

# Test the function if running this file directly
if __name__ == '__main__':
    bits = generate_random_bits(10)
    print("Generated Bits:", bits)
