import numpy as np

def solve_circuit(G, I):
    V = np.linalg.solve(G, I)
    return V
