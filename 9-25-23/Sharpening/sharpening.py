import cv2
import numpy as np
from scipy.signal import convolve2d

input_image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\ladyinhat.png', cv2.IMREAD_GRAYSCALE)


# Horizontal and vertical Sobel operator
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Gradients
gradient_x = convolve2d(input_image, sobel_x, mode='same', boundary='wrap')
gradient_y = convolve2d(input_image, sobel_y, mode='same', boundary='wrap')

# Sharpened image
sharpened_image = input_image + gradient_x + gradient_y
sharpened_image = np.clip(sharpened_image, 0, 255)
sharpened_image = sharpened_image.astype(np.uint8)

# Output
cv2.imshow('org image', input_image)
cv2.imshow('Sharp image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()