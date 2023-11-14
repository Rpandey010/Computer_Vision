import cv2
import numpy as np
from scipy.signal import convolve2d

input_image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\moon.png', cv2.IMREAD_GRAYSCALE)


# Laplacian operator
laplacian_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

# Gradient
laplacian_gradient = convolve2d(input_image, laplacian_kernel, mode='same', boundary='wrap')

# Sharpened image
sharpened_image = input_image - laplacian_gradient

sharpened_image = np.clip(sharpened_image, 0, 255)

sharpened_image = sharpened_image.astype(np.uint8)

# Output
cv2.imshow("Org Image", input_image)
cv2.imshow('Shapened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows
