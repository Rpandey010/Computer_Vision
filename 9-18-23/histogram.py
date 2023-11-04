import cv2
import numpy as np
import matplotlib.pyplot as plt

# Custom histogram calculation function
def cal_histogram(img):
    histogram = [0] * 256
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            histogram[img[i, j]] += 1
    return histogram

# Input image
image_path = r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\lighthouse.webp'
img = cv2.imread(image_path, 0)

# OpenCV
histr_cv2 = cv2.calcHist([img], [0], None, [256], [0, 256])

# Custom method
histogram_custom = cal_histogram(img)

# Plot both histograms
plt.figure(figsize=(12, 6))

# plotting using OpenCV
plt.subplot(1, 2, 1)
plt.plot(histr_cv2)
plt.title('Histogram (OpenCV)')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# plotting using Custom method
plt.subplot(1, 2, 2)
plt.plot(histogram_custom)
plt.title('Histogram (Custom)')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
