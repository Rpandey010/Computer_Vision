import cv2
import numpy as np

def erosion(image, kernel):
    m, n = image.shape
    k, l = kernel.shape
    pad_image = np.pad(image, ((k // 2, k // 2), (l // 2, l // 2)), mode='constant', constant_values=0)
    eroded_image = np.zeros(image.shape, dtype=np.uint8)

    for i in range(m):
        for j in range(n):
            eroded_image[i, j] = np.min(pad_image[i:i+k, j:j+l] * kernel)

    return eroded_image


image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\circuit.png', cv2.IMREAD_GRAYSCALE)

# Define a structuring element
kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]], dtype=np.uint8)

# Perform erosion
eroded_image = erosion(image, kernel)

# Display the original and eroded images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
