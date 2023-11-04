import numpy as np

# Creating the input matrix with specified coordinates as 1
input_matrix = np.zeros((8, 8))
input_matrix[2, 2] = 1
input_matrix[2, 4] = 1
input_matrix[4, 2] = 1
input_matrix[4, 4] = 1

# Initialize the output matrix for scaling
output_matrix_scaling = np.zeros((8*2, 8*2))

# Scaling parameters
scale_x = 2
scale_y = 2

# Apply scaling transformation using loops
for i in range(8):
    for j in range(8):
        new_i = int(i * scale_y)
        new_j = int(j * scale_x)
        output_matrix_scaling[new_i:new_i+scale_y, new_j:new_j+scale_x] = input_matrix[i, j]

# Input and Output matrices
print("Input Matrix:")
print(input_matrix)
print("\nOutput Matrix (Scaling):")
print(output_matrix_scaling)