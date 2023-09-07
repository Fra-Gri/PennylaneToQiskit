# PennylaneToQiskit
Integration of some functions to use Pennylane Dataset with Qiskit.

## Pennylane datasets
Pennylane has a library of quantum dataset for various molecules [here](https://pennylane.ai/datasets/), that include the hamiltonian ready for Pennylane circuit. 
For example, you can download the dataset for the H2 molecule:
```python
H2dataset = qml.data.load("qchem", molname="H2", bondlength=0.742, basis="STO-3G")[0]
```
## Hamiltonian
You can access the pannylane hamiltonian:
```python
pennylane_hamiltonian = H2dataset.hamiltonian
```

And you can convert it to a Qiskit hamiltonian simply
```python
qiskit_hamiltonian = to_qiskit_pauli_hamiltonian(pennylane_hamiltonian)
```
The Qiskit hamiltonian can be directly used as observable for the [Estimator](https://qiskit.org/ecosystem/ibm-runtime/stubs/qiskit_ibm_runtime.Estimator.html) Primitive.

> This function can be used only with Pauli Hamiltonian, like the ones in the Quantum Dataset

