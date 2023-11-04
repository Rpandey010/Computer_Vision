import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\filtering.png', cv2.IMREAD_GRAYSCALE)

# Generate random Gaussian noise
mean = 0
stddev = 1  
noise = np.random.normal(mean, stddev, img.shape).astype(np.uint8)

# Add noise to the image
noisy_img = cv2.add(img, noise)

kernel_size = 5

output_image = cv2.blur(noisy_img, (kernel_size, kernel_size))

# Display the original and filtered images
cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
