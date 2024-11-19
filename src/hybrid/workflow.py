import sys
import os

# Thank you chat
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from pennylane import numpy as np
from src.quantum.circuit import compression_circuit

def preprocess_data(data):
    """Preprocess classical data for quantum encoding."""
    # Normalize data to fit between 0 and pi
    return (data - np.min(data)) / (np.max(data) - np.min(data)) * np.pi

def reconstruct_data(compressed_state):
    # TODO
    return compressed_state

def quantum_compression(data, params):
    """Full hybrid quantum-classical compression workflow."""
    # Preprocess data
    normalized_data = preprocess_data(data)
    print("Normalized Data:", normalized_data)

    # Apply quantum compression circuit
    compressed_state = compression_circuit(normalized_data, params)

    # Reconstruct data (placeholder logic)
    reconstructed_data = reconstruct_data(compressed_state)

    return compressed_state, reconstructed_data

if __name__ == "__main__":
    # Example data
    raw_data = np.array([10, 20, 30, 40])
    params = np.random.random((2, 4)) 

    # Run hybrid workflow
    compressed, reconstructed = quantum_compression(raw_data, params)
    print("Compressed State:", compressed)
    print("Reconstructed Data:", reconstructed)
