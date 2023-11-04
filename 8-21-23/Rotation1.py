import numpy as np

def rotate_matrix(matrix, angle):
    if len(matrix) == 0:
        return []

    rows, cols = len(matrix), len(matrix[0])
    rotated_matrix = []

# 90 Degree
    if angle == 90:
        rotated_matrix = [[0] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                rotated_matrix[j][rows - i - 1] = matrix[i][j]

# 180 degree
    elif angle == 180:
        rotated_matrix = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                rotated_matrix[rows - i - 1][cols - j - 1] = matrix[i][j]

# Invalid degree
    else:
        print("Invalid angle. Supported angles are 90 and 180 degrees.")
        return []

    return rotated_matrix

def generate_random_matrix(rows, cols):
    return np.random.randint(2, size=(rows, cols))

original_matrix = generate_random_matrix(8, 8)

# Creating while loop
while True:
    print("Matrix:\n", original_matrix)

    rotation_angle = int(input("Enter rotation angle (90, 180): "))
    if rotation_angle not in [90, 180]:
        print("Invalid angle. Supported angles are 90 and 180 degrees.")
        continue

    original_matrix = rotate_matrix(original_matrix, rotation_angle)

    print("Rotated Matrix:")
    for row in original_matrix:
        print(row)

    continue_option = input("Do you want to continue rotating? (yes/no): ")
    if continue_option.lower() != 'yes':
        break

# Rotated matrix
print("Final Rotated Matrix:")
for row in original_matrix:
    print(row)
