import cv2
import numpy as np

image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\Thumb.jpg', cv2.IMREAD_GRAYSCALE)
kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]], dtype=np.uint8)

def erosion(image, kernel):
    m, n = image.shape
    k, l = kernel.shape
    pad_image = np.pad(image, ((k // 2, k // 2), (l // 2, l // 2)), mode='constant', constant_values=0)
    eroded_image = np.zeros(image.shape, dtype=np.uint8)

    for i in range(m):
        for j in range(n):
            eroded_image[i, j] = np.min(pad_image[i:i+k, j:j+l] * kernel)

    return eroded_image

def dilation(image, kernel):
    m, n = image.shape
    k, l = kernel.shape
    pad_image = np.pad(image, ((k // 2, k // 2), (l // 2, l // 2)), mode='constant', constant_values=0)
    dilated_image = np.zeros(image.shape, dtype=np.uint8)

    for i in range(m):
        for j in range(n):
            dilated_image[i, j] = np.max(pad_image[i:i+k, j:j+l] * kernel)

    return dilated_image

def opening(image, kernel):
    eroded = erosion(image, kernel)
    opened = dilation(eroded, kernel)
    return opened

def closing(image, kernel):
    dilated = dilation(image, kernel)
    closed = erosion(dilated, kernel)
    return closed

# Performingggg erosion
eroded_image = erosion(image, kernel)

# Performinggg dilation
dilated_image = dilation(image, kernel)

# Performinggg opening
opened_image = opening(image, kernel)

# Performingg closing
closed_image = closing(image, kernel)

# Display the original, eroded, dilated, opened, and closed images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)
cv2.imshow('Dilated Image', dilated_image)
cv2.imshow('Opened Image', opened_image)
cv2.imshow('Closed Image', closed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
