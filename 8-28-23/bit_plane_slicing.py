import numpy as np
import cv2
import matplotlib.pyplot as plt

# Read the image in grayscale
image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\xray.webp', 0)
width = image.shape[0]
height = image.shape[1]

#Iterating each pixel and changing pixel value to binary.
binary_pixel_list = []
for i in range(width):
    for j in range(height):
        binary_pixel_list.append(np.binary_repr(image[i][j], width=8)) # here width ----------> no. of bits

# here each variable holds a array where each pixel's intensity value corresponds to the LSB of the corresponding pixel in the original image

bit0_img = (np.array([int(pixel[7]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
bit1_img = (np.array([int(pixel[6]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
bit2_img = (np.array([int(pixel[5]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
bit3_img = (np.array([int(pixel[4]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
bit4_img = (np.array([int(pixel[3]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
bit5_img = (np.array([int(pixel[2]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
bit6_img = (np.array([int(pixel[1]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
bit7_img = (np.array([int(pixel[0]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)

# Coverting bit plane images to RGB format 
bit0_img = cv2.cvtColor(bit0_img, cv2.COLOR_BGR2RGB)
bit1_img = cv2.cvtColor(bit1_img, cv2.COLOR_BGR2RGB)
bit2_img = cv2.cvtColor(bit2_img, cv2.COLOR_BGR2RGB)
bit3_img = cv2.cvtColor(bit3_img, cv2.COLOR_BGR2RGB)
bit4_img = cv2.cvtColor(bit4_img, cv2.COLOR_BGR2RGB)
bit5_img = cv2.cvtColor(bit5_img, cv2.COLOR_BGR2RGB)
bit6_img = cv2.cvtColor(bit6_img, cv2.COLOR_BGR2RGB)
bit7_img = cv2.cvtColor(bit7_img, cv2.COLOR_BGR2RGB)


plt.figure(figsize=(12, 6))


plt.subplot(241), plt.imshow(bit0_img), plt.title("bit0")
plt.subplot(242), plt.imshow(bit1_img), plt.title("bit1")
plt.subplot(243), plt.imshow(bit2_img), plt.title("bit2")
plt.subplot(244), plt.imshow(bit3_img), plt.title("bit3")

plt.subplot(245), plt.imshow(bit4_img), plt.title("bit4")
plt.subplot(246), plt.imshow(bit5_img), plt.title("bit5")
plt.subplot(247), plt.imshow(bit6_img), plt.title("bit6")
plt.subplot(248), plt.imshow(bit7_img), plt.title("bit7")

plt.suptitle("Bit Plane Slicing") 
plt.tight_layout() 
plt.show()
