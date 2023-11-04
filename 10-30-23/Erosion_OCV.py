import cv2
import numpy as np

# Read the binary image
image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\circuit.png', cv2.IMREAD_GRAYSCALE)

# Define a structuring element (a simple 3x3 square kernel)
kernel = np.ones((3, 3), dtype=np.uint8)

# Perform erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Display the original and eroded images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
