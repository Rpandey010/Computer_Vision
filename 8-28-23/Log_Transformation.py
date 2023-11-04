import cv2 
import matplotlib.pyplot as plt 
import math
import numpy as np 

# Read an image 
image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\log_star.jpg') 

# Apply log transformation method 
# The log transformation enhances darker areas of the image while compressing higher pixel values. 
# The 'c' value is calculated to ensure that the output values are within the valid pixel range (0 to 255).

c = 255 / np.log(1 + np.max(image)) 
log_image = c * (np.log(image + 1)) 

# Specify the data type so that 
# float value will be converted to int 
log_image = np.array(log_image, dtype = np.uint8) 

# Create a figure with 1 row and 2 columns for subplots
plt.figure(figsize=(10, 5))

# Display the original image in the first subplot
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')

# Display the log-transformed image in the second subplot
plt.subplot(1, 2, 2)
plt.imshow(log_image)
plt.title('Log-Transformed Image')

# Show the plot
plt.tight_layout()
plt.show()
