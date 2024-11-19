import pennylane as qml
from pennylane import numpy as np

# Define the quantum device
n_qubits = 4  # Number of qubits
dev = qml.device("default.qubit", wires=n_qubits)

def encode_data(data):
    """Encodes classical data into quantum states."""
    if len(data) > n_qubits:
        raise ValueError(f"Data length {len(data)} exceeds number of qubits {n_qubits}")
    for i, value in enumerate(data):
        qml.RY(value, wires=i)  # Use rotations to encode data

@qml.qnode(dev)
def compression_circuit(data, params):
    """Quantum compression circuit."""
    # Encode classical data into quantum states
    encode_data(data)

    # Apply compression gates
    qml.BasicEntanglerLayers(params, wires=range(n_qubits))

    # Return all qubit states
    return qml.state()

if __name__ == "__main__":
    # Example input
    data = np.array([0.1, 0.5, 0.3, 0.7])  # Normalize between 0 and pi
    params = np.random.random((2, n_qubits))  # Random initial parameters

    # Run the circuit
    output = compression_circuit(data, params)
    print("Compressed quantum state:", output)
