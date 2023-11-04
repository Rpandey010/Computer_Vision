import numpy as np

# G# Generating Two matrix through Random function, I have taken its dimension (3X3) for simplicity
random_matrix = np.random.randint(0, 10, size=(3, 3))
print("Random Matrix:")
print(random_matrix)

# ADJOINT
adjoint_matrix = np.linalg.inv(random_matrix)
print("\nAdjoint Matrix:")
print(adjoint_matrix)

try:
    # INVERSE
    inverse_matrix = np.linalg.inv(random_matrix)
    print("\nInverse Matrix:")
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("\nInverse does not exist for this matrix.")
