import numpy as np

# Generating Two matrix through Random function, I have taken its dimension (3X3) for simplicity
matrix1 = np.random.randint(0, 10, size=(3, 3))
matrix2 = np.random.randint(0, 10, size=(3, 3))

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

operation = input("\nEnter the operation (+ for addition, - for subtraction, * for multiplication): ")

if operation == '+':
    result = matrix1 + matrix2
    operation_text = "addition"
elif operation == '-':
    result = matrix1 - matrix2
    operation_text = "subtraction"
elif operation == '*':
    result = matrix1 * matrix2
    operation_text = "multiplication"
else:
    print("In VALID")
    exit()

print(f"\nResult of {operation_text}:")
print(result)
