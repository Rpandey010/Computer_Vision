import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d

input_image = Image.open(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\ladyinhat.png').convert('L')
input_image = np.array(input_image)

# Horizontal and verticalSobel operator
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
plt.subplot(1, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(sharpened_image, cmap='gray')
plt.title('Sharpened Image')

plt.show()
