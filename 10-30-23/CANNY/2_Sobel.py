import cv2
import numpy as np

# Read the blurred image
blurred_image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\\10-30-23\CANNY\images\\gaussian_output.png', cv2.IMREAD_GRAYSCALE)

# Define Sobel operators for gradient calculation
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Calculate gradients using Sobel operators
gradient_x = cv2.filter2D(blurred_image, -1, sobel_x)
gradient_y = cv2.filter2D(blurred_image, -1, sobel_y)

# Calculate gradient magnitude and direction
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
gradient_direction = np.arctan2(gradient_y, gradient_x)

cv2.imwrite('output_image.png', gradient_direction)

# Display the gradient magnitude image
cv2.imshow('Gradient Magnitude', gradient_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
