import cv2
import numpy as np

# Read the input image
image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\owl_canny.png', cv2.IMREAD_GRAYSCALE)

# Define the Gaussian kernel
kernel_size = 5
sigma = 1.4
kernel = np.fromfunction(lambda x, y: (1/ (2 * np.pi * sigma ** 2)) * np.exp(-((x - (kernel_size - 1) / 2) ** 2 + (y - (kernel_size - 1) / 2) ** 2) / (2 * sigma ** 2)), (kernel_size, kernel_size))

# Normalize the kernel
kernel = kernel / kernel.sum()

# Apply Gaussian blur to the image
blurred_image = cv2.filter2D(image, -1, kernel)

cv2.imwrite('output_image.png', blurred_image)

# Display the blurred image
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
