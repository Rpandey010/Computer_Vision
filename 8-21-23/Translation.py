import numpy as np

# Creating the input matrix with specified coordinates as 1
input_matrix = np.zeros((8, 8))
input_matrix[2, 2] = 1
input_matrix[2, 4] = 1
input_matrix[4, 2] = 1
input_matrix[4, 4] = 1

# Initialize the output matrix with zeros
output_matrix = np.zeros_like(input_matrix)

# Perform translation for each pixel
Tx, Ty = 2, -1
for y_out in range(output_matrix.shape[0]):
    for x_out in range(output_matrix.shape[1]):
        # New coordinates after translation
        x_in = x_out - Tx
        y_in = y_out - Ty

        if 0 <= x_in < input_matrix.shape[1] and 0 <= y_in < input_matrix.shape[0]:
            output_matrix[y_out, x_out] = input_matrix[y_in, x_in]

# Input and output matrices
print("Input Matrix:")
print(input_matrix)

print("\nOutput Matrix:")
print(output_matrix)
