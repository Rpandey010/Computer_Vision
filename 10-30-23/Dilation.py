import cv2
import numpy as np

def dilation(image, kernel):
    m, n = image.shape
    k, l = kernel.shape
    pad_image = np.pad(image, ((k // 2, k // 2), (l // 2, l // 2)), mode='constant', constant_values=0)
    dilated_image = np.zeros(image.shape, dtype=np.uint8)

    for i in range(m):
        for j in range(n):
            dilated_image[i, j] = np.max(pad_image[i:i+k, j:j+l] * kernel)

    return dilated_image


image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\script.png', cv2.IMREAD_GRAYSCALE)

# Define a structuring element 
kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]], dtype=np.uint8)

# Perform dilation
dilated_image = dilation(image, kernel)

# Display the original and dilated images
cv2.imshow('Original Image', image)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
