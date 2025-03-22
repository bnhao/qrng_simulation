import requests
import numpy as np

def fetch_external_random_numbers(length: int = 1000) -> np.ndarray:
    """
    Fetch random numbers from an external QRNG API and convert them to a binary sequence.
    
    Args:
        length (int): The number of random numbers to fetch.
        
    Returns:
        np.ndarray: A binary sequence (0s and 1s) derived from the fetched data.
    """
    # Construct the API URL with the desired length and type
    QRN_URL = "https://api.quantumnumbers.anu.edu.au/"
    QRN_KEY = "J9yW19rXu9aVgwXfDEKhQ236o4DOZG692NkoKhp5"  # replace with your secret API-KEY

    DTYPE = "uint8"  # uint8, uint16, hex8, hex16
    BLOCKSIZE = 1  # between 1--10. Only needed for hex8 and hex16
    LENGTH = 1000

    params = {"length": LENGTH, "type": DTYPE, "size": BLOCKSIZE}
    headers = {"x-api-key": QRN_KEY}
    
    try:
        response = requests.get(QRN_URL, headers=headers, params=params)
        response.raise_for_status()  # Raises an HTTPError if the response code was unsuccessful
        data = response.json()
        
        # Check if the API returned a valid result
        if data.get("success", False):
            # Extract the list of numbers; the API returns numbers in the "data" field
            numbers = data.get("data", [])
            # Convert each uint8 number to a bit by taking the least significant bit (for example)
            bits = [num & 1 for num in numbers]
            return np.array(bits)
        else:
            print("API request was not successful.")
            return np.array([])
    except Exception as e:
        print(f"Error fetching data from external API: {e}")
        return np.array([])

# For testing the module independently
if __name__ == '__main__':
    bits = fetch_external_random_numbers(100)
    print("Fetched external random bits:")
    print(bits)
