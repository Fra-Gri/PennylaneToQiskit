def to_qiskit_pauli_hamiltonian(hamiltonian):
    """
    Input: 
        Pennylane Hamiltonan: hamiltonian from a pennylane quantum dataset
    
    Return: 
        op : SparsePauliOp 
    
    """
    
    from pennylane.operation import Observable
    from qiskit.quantum_info import SparsePauliOp
    
    
    pauli_sparse_list= []
    
    # number of qubits of the circuit
    num_qubits = len(hamiltonian.wires)
                
    for i, obs in enumerate(hamiltonian.ops):
        pauli_string = qml.pauli.pauli_word_to_string(obs)
        qubits = obs.wires.tolist()
        coeff = hamiltonian.coeffs[i]
            
        pauli_sparse_list.append((pauli_string, qubits, coeff))
        
    op = SparsePauliOp.from_sparse_list(pauli_sparse_list, num_qubits)
    
    return op
