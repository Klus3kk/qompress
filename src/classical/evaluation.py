from pennylane import numpy as np

def mean_squared_error(original, reconstructed):
    """Calculate the mean squared error between original and reconstructed data."""
    return np.mean((original - reconstructed) ** 2)

if __name__ == "__main__":
    # Example evaluation
    original = np.array([10, 20, 30, 40])
    reconstructed = np.array([9.8, 19.5, 29.9, 40.1])  # Example output
    error = mean_squared_error(original, reconstructed)
    print("Mean Squared Error:", error)
