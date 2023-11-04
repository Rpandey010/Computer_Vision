from PIL import Image
import numpy as np

def FLIP(input_image_path, output_image_path):
    image = Image.open(input_image_path)
    image_array = np.array(image)
    
    # Flip the image vertically
    flipped_image_array = np.flipud(image_array)
    flipped_image = Image.fromarray(flipped_image_array)
    flipped_image.save(output_image_path)

if __name__ == "__main__":
    input_image_path = r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\einstein.jpg'  
    output_image_path = "output_image.jpg"  

    FLIP(input_image_path, output_image_path)
