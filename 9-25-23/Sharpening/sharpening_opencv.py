import cv2
import numpy as np

# Load the image
input_image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\ladyinhat.png',cv2.IMREAD_GRAYSCALE)

# Compute horizontal and vertical gradients using Sobel operator
gradient_x = cv2.Sobel(input_image, cv2.CV_32F, 1, 0)
gradient_y = cv2.Sobel(input_image, cv2.CV_32F, 0, 1)

# Sharpened image
sharpened_image = cv2.addWeighted(input_image, 1.5, gradient_x, 0.5, 0, dtype=cv2.CV_8U)

sharpened_image = np.clip(sharpened_image, 0, 255).astype(np.uint8)

# Output
cv2.imshow('Original Image', input_image)
cv2.imshow('Sharpened Image', sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
