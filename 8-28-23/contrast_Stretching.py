import cv2 
import matplotlib.pyplot as plt 

# Read an image 
image = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\Contrast_stretching.webp') 
plt.show()

# Apply contrast stretching method 
MAX_input = 250    #any pixel value in the original image equal to or below 250 will be stretched.
MIN_input = 3      #any pixel value in the original image equal to or above 3 will be stretched.

MAX_output = 155 
MIN_output = 0

stretched_image = image.copy()
# get height and width of the image 
height, width, _ = image.shape 

for i in range(0, height - 1): 
    for j in range(0, width - 1): 
        
        # Get the pixel value 
        pixel = stretched_image[i, j] 
        
        # 1st index contains red pixel 
        pixel[0] = (pixel[0] - MIN_input) * ((MAX_output-MIN_output) / (MAX_input-MIN_input)) + MIN_output 
        
        # index containing green pixel 
        pixel[1] = (pixel[1] - MIN_input) * ((MAX_output-MIN_output) / (MAX_input-MIN_input)) + MIN_output 
        
        # this index contains blue pixel 
        pixel[2] = (pixel[2] - MIN_input) * ((MAX_output-MIN_input) / (MAX_input-MIN_input)) + MIN_input 
        
        stretched_image[i, j] = pixel 


# Create a figure with subplots to display the images side by side
plt.figure(figsize=(12, 6))

# Display the original image in the first subplot
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

# Display the stretched image in the second subplot
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(stretched_image, cv2.COLOR_BGR2RGB))
plt.title('Stretched Image')

# Show the plot
plt.tight_layout()
plt.show()