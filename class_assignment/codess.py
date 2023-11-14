#AVERAGE FILTER

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

#MEDIAN FILTER
import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\saltpepper.png', cv2.IMREAD_GRAYSCALE)
img = img / 255

# Create a blank image
x, y = img.shape

# NOISEEEEEEE
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
cv2.imshow("Input Image", img)
cv2.imshow("Noisy Image", g)
cv2.imshow("Filtered image", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows


#LAPLACIAN SHARPENING
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


#SHARPENING
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


#EROSION
import cv2
import numpy as np

def erosion(image, kernel):
    m, n = image.shape
    k, l = kernel.shape
    padding = np.pad(image, ((k // 2, k //2),(l // 2, l // 2)), mode='constant', constant_values=0)
    eroded = np.zeros(image.shape, dtype=np.uint8)

    for i in range(m):
        for j in range(n):
            eroded[i, j] = np.min(padding[i:i+k, j:j+l] * kernel)
    return eroded

image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\circuit.png', cv2.IMREAD_GRAYSCALE)

kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]], dtype=np.uint8)

eroded = erosion(image, kernel)

cv2.imshow('Org image', image)
cv2.imshow('Eroded image', eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()


#DILATION
#min----> max


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

 