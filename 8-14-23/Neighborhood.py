import numpy as np

def get_n4_neighbors(matrix, row, col):
    n4_neighbors = [
        (row - 1, col),  # Above
        (row + 1, col),  # Below
        (row, col - 1),  # Left
        (row, col + 1)  # Right
    ]
    return n4_neighbors

def get_nd_neighbors(matrix, row, col):
    nd_neighbors = [
        (row - 1, col - 1),  # Top left
        (row + 1, col - 1), # Bottom left
        (row - 1, col + 1),   # Top right
        (row + 1, col + 1)   # Bottom right
    ]
    return nd_neighbors

def get_n8_neighbors(matrix, row, col):
    n8_neighbors = get_n4_neighbors(matrix, row, col) + get_nd_neighbors(matrix, row, col)
    return n8_neighbors

def print_neighbor_values(matrix, neighbors):
    values = []
    for neighbor_row, neighbor_col in neighbors:
        if 0 <= neighbor_row < matrix.shape[0] and 0 <= neighbor_col < matrix.shape[1]:
            values.append(str(matrix[neighbor_row, neighbor_col]))
    print(", ".join(values))

# Generate a 5x5 matrix with whole number random values
matrix = np.random.randint(0, 100, size=(5, 5))

print("Generated Matrix:")
print(matrix)

# Ask the user to select a pixel
selected_row = int(input("Enter the row of the selected pixel: "))
selected_col = int(input("Enter the column of the selected pixel: "))

# Calculate neighborhoods
n4_neighbors = get_n4_neighbors(matrix, selected_row, selected_col)
nd_neighbors = get_nd_neighbors(matrix, selected_row, selected_col)
n8_neighbors = get_n8_neighbors(matrix, selected_row, selected_col)

selected_pixel_value = matrix[selected_row, selected_col]

print("\nSelected Pixel Value:", selected_pixel_value)

print("\nN4 Neighborhood Values:", end=" ")
print_neighbor_values(matrix, n4_neighbors)

print("Nd Neighborhood Values:", end=" ")
print_neighbor_values(matrix, nd_neighbors)

print("N8 Neighborhood Values:", end=" ")
print_neighbor_values(matrix, n8_neighbors)
