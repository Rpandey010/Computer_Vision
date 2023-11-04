import numpy as np
import cv2
import matplotlib.pyplot as plt

# Read the input image
input_image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\fruits.jpg')
height, width, channels = input_image.shape

# Translation parameters
tx = 50  # translation along x-axis
ty = 30  # translation along y-axis

# Initialize output images for forward and backward warping
output_forward = np.zeros_like(input_image)
output_backward = np.zeros_like(input_image)

# Forward Warping
for y_out in range(height):
    for x_out in range(width):
        x_in = x_out - tx
        y_in = y_out - ty
        if 0 <= x_in < width and 0 <= y_in < height:
            output_forward[y_out, x_out] = input_image[y_in, x_in]

# Backward Warping
for y_in in range(height):
    for x_in in range(width):
        x_out = x_in + tx
        y_out = y_in + ty
        if 0 <= x_out < width and 0 <= y_out < height:
            output_backward[y_in, x_in] = input_image[y_out, x_out]

# Display the images
plt.figure(figsize=(10, 5))
plt.subplot(131), plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)), plt.title("Input Image")
plt.subplot(132), plt.imshow(cv2.cvtColor(output_forward, cv2.COLOR_BGR2RGB)), plt.title("Forward Warping")
plt.subplot(133), plt.imshow(cv2.cvtColor(output_backward, cv2.COLOR_BGR2RGB)), plt.title("Backward Warping")
plt.tight_layout()
plt.show()
