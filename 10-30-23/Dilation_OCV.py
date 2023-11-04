import cv2
import numpy as np

image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\script.png', cv2.IMREAD_GRAYSCALE)

# Define a structuring element 
kernel = np.ones((3, 3), dtype=np.uint8)

# Perform dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Display the original and dilated images
cv2.imshow('Original Image', image)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
