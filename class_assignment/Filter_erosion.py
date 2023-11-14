# Avg filtering followed by Erosion

import cv2
import numpy as np

# Load the image
img = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\circuit.png', cv2.IMREAD_GRAYSCALE)

# Generate random Gaussian noise
mean = 0
stddev = 1
noise = np.random.normal(mean, stddev, img.shape).astype(np.uint8)

# Add noise to the image
noisy_img = cv2.add(img, noise)

# Size of filter
kernel_size = 5

# Apply the average filter to remove noise
output_image = np.zeros_like(noisy_img)
padding_size = kernel_size // 2

for i in range(padding_size, noisy_img.shape[0] - padding_size):
    for j in range(padding_size, noisy_img.shape[1] - padding_size):
        roi = noisy_img[i - padding_size:i + padding_size + 1, j - padding_size:j + padding_size + 1]
        average_value = np.mean(roi)
        output_image[i, j] = average_value

# EROSION 
def erosion(image, kernel):
    m, n = image.shape
    k, l = kernel.shape
    padding = np.pad(image, ((k // 2, k //2),(l // 2, l // 2)), mode='constant', constant_values=0)
    eroded = np.zeros(image.shape, dtype=np.uint8)

    for i in range(m):
        for j in range(n):
            eroded[i, j] = np.min(padding[i:i+k, j:j+l] * kernel)
    return eroded

kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]], dtype=np.uint8)

eroded = erosion(output_image, kernel)

# Display the original, noisy, filtered, and eroded images
cv2.imshow("Input Image", img)
cv2.imshow("Noisy Image", noisy_img)
cv2.imshow("Filtered Image", output_image)
cv2.imshow("Eroded Image", eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()

