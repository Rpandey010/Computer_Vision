import cv2
import numpy as np

# Load the image
img = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\filtering.png', cv2.IMREAD_GRAYSCALE)

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

# Output
cv2.imshow("Input Image", img)
cv2.imshow("Noisy Image", noisy_img)
cv2.imshow("Filtered image", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows
