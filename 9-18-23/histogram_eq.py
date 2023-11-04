import cv2
import numpy as np

def histogram_equalization(image):
    # Calculate the histogram
    histogram = [0] * 256
    cumulative_histogram = [0] * 256
    equalized_image = np.zeros_like(image)

    # Step 1: Calculate the histogram
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel_value = image[i, j]
            histogram[pixel_value] += 1

    # Step 2: Calculate the cumulative histogram
    cumulative_sum = 0
    for i in range(256):
        cumulative_sum += histogram[i]
        cumulative_histogram[i] = cumulative_sum

    # Step 3: Perform histogram equalization
    total_pixels = image.shape[0] * image.shape[1]
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel_value = image[i, j]
            equalized_value = int((cumulative_histogram[pixel_value] / total_pixels) * 255)
            equalized_image[i, j] = equalized_value

    return equalized_image

# Load an image
image = cv2.imread("img\HIstogram_eq.png", cv2.IMREAD_GRAYSCALE)

# Perform histogram equalization
equalized_image = histogram_equalization(image)

# Display the original and equalized images
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
