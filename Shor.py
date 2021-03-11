from qiskit.aqua.algorithms import Shor
from qiskit.aqua import QuantumInstance
import numpy as np
from qiskit import QuantumCircuit, Aer, execute
backend = Aer.get_backend('qasm_simulator')
quanInst =  QuantumInstance(backend, shots=1000)
shorShot = Shor(N=35,a=3,quantum_instance=quanInst)
print(Shor.run(shorShot))
