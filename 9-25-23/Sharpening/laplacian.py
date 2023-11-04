import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d

input_image = Image.open(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\moon.png').convert('L')
input_image = np.array(input_image)

# Laplacian operator
laplacian_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

# Gradient
laplacian_gradient = convolve2d(input_image, laplacian_kernel, mode='same', boundary='wrap')

# Sharpened image
sharpened_image = input_image - laplacian_gradient

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
