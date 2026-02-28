import numpy as np

def solve_circuit(G, I):
    V = np.linalg.solve(G, I)
    return V

R1 = float(input("Enter R1 (Node1 to ground): "))
R2 = float(input("Enter R2 (Node1 to Node2): "))
R3 = float(input("Enter R3 (Node2 to ground): "))
I1 = float(input("Enter current injected at Node1 (A): "))

G = np.array([
    [1/R1 + 1/R2, -1/R2],
    [-1/R2, 1/R2 + 1/R3]
])

I = np.array([I1, 0])

voltages = solve_circuit(G, I)

print("\nNode Voltages:")
for i, v in enumerate(voltages):
    print(f"V{i+1} = {v:.4f} V")
