import cv2
import numpy as np
from scipy.signal import convolve2d

image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\ladyinhat.png', cv2.IMREAD_GRAYSCALE)

sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

gradient_x = convolve2d(image, sobel_x, mode='same', boundary='wrap')
gradient_y = convolve2d(image, sobel_y, mode='same', boundary='wrap')

sharpened_image = image + gradient_x + gradient_y
sharpened_image = np.clip(sharpened_image, 0, 255)
sharpened_image = sharpened_image.astype(np.uint8)

cv2.imshow('org image', image)
cv2.imshow('Sharp image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
