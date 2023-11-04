import cv2 
import matplotlib.pyplot as plt 
import math
import numpy as np 

# Read an image 
image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\gamma.webp') 
plt.imshow(image) 

# Trying 2 different gamma values 
for gamma in [0.4, 2.2]:

    # Apply gamma correction. 
    gamma_corrected = np.array(255*(image / 255) ** gamma, dtype = 'uint8') 
    plt.imshow(gamma_corrected) 
    plt.show() 
