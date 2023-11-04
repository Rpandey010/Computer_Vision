import cv2
import numpy as np

# Load the input image
input_image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\einstein.jpg')  

if input_image is None:
    print("Error: Could not read the image.")
else:
    height, width, _ = input_image.shape

    output_image = np.zeros_like(input_image)

    # Flip the image vertically
    for i in range(height):
        for j in range(width):
            output_image[i, j] = input_image[height - 1 - i, j]

    # Display Input and Output image
    cv2.imshow('Input Image', input_image)
    cv2.imshow('Vertical Flipped Image', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
