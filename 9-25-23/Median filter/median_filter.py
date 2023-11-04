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

# Function to apply the median filter
def median_filter(image, filter_size):
    padding_size = filter_size // 2
    filtered_image = np.copy(image)
    
    for i in range(padding_size, image.shape[0] - padding_size):
        for j in range(padding_size, image.shape[1] - padding_size):
            neighborhood = image[i - padding_size:i + padding_size + 1, j - padding_size:j + padding_size + 1]
            median_value = np.median(neighborhood)
            filtered_image[i, j] = median_value
    
    return filtered_image

# Apply the median filter to remove noise
filtered_image = median_filter(g, filter_size)

# Output
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