import cv2
import numpy as np

def erosion(image, kernel):
    m, n = image.shape
    k, l = kernel.shape
    padding = np.pad(image, ((k // 2, k //2),(l // 2, l // 2)), mode='constant', constant_values=0)
    eroded = np.zeros(image.shape, dtype=np.uint8)

    for i in range(m):
        for j in range(n):
            eroded[i, j] = np.min(padding[i:i+k, j:j+l] * kernel)
    return eroded

image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\circuit.png', cv2.IMREAD_GRAYSCALE)

kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]], dtype=np.uint8)

eroded = erosion(image, kernel)

cv2.imshow('Org image', image)
cv2.imshow('Eroded image', eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()