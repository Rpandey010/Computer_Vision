import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\saltpepper.png', 0)
img = img / 255

# Create a blank image
x, y = img.shape
g = np.zeros((x, y), dtype=np.float32)

# Salt and pepper noise levels
pepper = 0.1
salt = 0.95

# Create an image with salt and pepper noise
for i in range(x):
    for j in range(y):
        rdn = np.random.random()
        if rdn < pepper:
            g[i][j] = 0
        elif rdn > salt:
            g[i][j] = 1
        else:
            g[i][j] = img[i][j]

filter_size = 3

# OpenCV
filtered_image = cv2.medianBlur(g, filter_size)

plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(132)
plt.imshow(g, cmap='gray')
plt.title('Noisy Image')
plt.axis('off')

plt.subplot(133)
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image')
plt.axis('off')

plt.show()