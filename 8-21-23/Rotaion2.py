import numpy as np

def rotate_matrix(matrix, angle):
    if len(matrix) == 0:
        return []

    rows, cols = len(matrix), len(matrix[0])
    rotated_matrix = []

    if angle == 90:
        rotated_matrix = [[0] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                rotated_matrix[j][rows - i - 1] = matrix[i][j]

    elif angle == 180:
        rotated_matrix = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                rotated_matrix[rows - i - 1][cols - j - 1] = matrix[i][j]

    else:
        print("Invalid angle. Supported angles are 90 and 180 degrees.")
        return []

    return rotated_matrix

def generate_random_matrix(rows, cols):
    return np.random.randint(2, size=(rows, cols))

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Main program
original_matrix = generate_random_matrix(8, 8)

print("Original Matrix:")
print_matrix(original_matrix)

rotation_angle = int(input("Enter rotation angle (--->90 or ---> 180): "))
if rotation_angle not in [90, 180]:
    print("Invalid angle. Supported angles are 90 and 180 degrees.")
else:
    rotated_matrix = rotate_matrix(original_matrix, rotation_angle)

    print("\nRotated Matrix:")
    print_matrix(rotated_matrix)


