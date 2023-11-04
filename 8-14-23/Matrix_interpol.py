import numpy as np

def nearest_neighbor_interpolation(input_matrix, output_shape):
    input_height, input_width = input_matrix.shape
    output_height, output_width = output_shape
    y_ratio = input_height / output_height            #The ratios are calculated to determine how much each pixel
    x_ratio = input_width / output_width              #in the output matrix corresponds to in the input matrix.

    output_matrix = np.empty(output_shape, dtype=input_matrix.dtype)

    for y_out in range(output_height):
        for x_out in range(output_width):
            y_in = int(y_out * y_ratio)
            x_in = int(x_out * x_ratio)
            output_matrix[y_out, x_out] = input_matrix[y_in, x_in]

    return output_matrix

# Generate Matrix using Random func
input_matrix = np.random.randint(0, 100, size=(3, 3))

# Define output shape
output_shape = (6, 6)

# Perform nearest-neighbor interpolation
interpolated_matrix = nearest_neighbor_interpolation(input_matrix, output_shape)

# Print the original and interpolated matrices
print("Input Matrix:")
print(input_matrix)

print("\nInterpolated Matrix:")
for row in interpolated_matrix:
    print(" ".join(map(str, row)))
