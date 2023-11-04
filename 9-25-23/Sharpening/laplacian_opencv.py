import cv2
import numpy as np

input_image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\moon.png',cv2.IMREAD_GRAYSCALE)

# Compute gradients using Laplacian Operator
laplacian_gradient = cv2.Laplacian(input_image, cv2.CV_32F, ksize=1)

# Sharpened image
sharpened_image = cv2.convertScaleAbs(input_image - laplacian_gradient)

# Output
cv2.imshow('Original Image', input_image)
cv2.imshow('Sharpened Image', sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
