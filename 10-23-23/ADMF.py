import numpy as np
import cv2


input_image = cv2.imread(r"C:\Users\Raja\PycharmProjects\Computer_Vision\img\ladyinhat.png", 0)  # Load as grayscale


# Rescale the image intensity values to fit within 0-255
input_image = cv2.normalize(input_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)


# Function to add salt and pepper noise to the image
def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)
    total_pixels = image.size


    # Add salt noise
    num_salt = int(total_pixels * salt_prob)
    salt_coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[salt_coords[0], salt_coords[1]] = 255


    # Add pepper noise
    num_pepper = int(total_pixels * pepper_prob)
    pepper_coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[pepper_coords[0], pepper_coords[1]] = 0


    return noisy_image


# Adaptive Median Filter
def adaptive_median_filter(image, Smax):
    height, width = image.shape
    output_image = np.copy(image)


    for y in range(height):
        for x in range(width):
            window_size = 3  # Initial window size lets take this 3x3 for now


            while window_size <= Smax:
                half_size = window_size // 2
                window = image[max(0, y - half_size):min(height, y + half_size + 1),
                               max(0, x - half_size):min(width, x + half_size + 1)]


                Zmed = np.median(window)
                Zmin = np.min(window)
                Zmax = np.max(window)


                Al = Zmed - Zmin
                A2 = Zmed - Zmax


                if Al > 0 and A2 < 0:
                    B1 = image[y, x] - Zmin
                    B2 = image[y, x] - Zmax
                    if B1 > 0 and B2 < 0:
                        output_image[y, x] = image[y, x]
                    else:
                        output_image[y, x] = Zmed
                    break
                else:
                    window_size += 2


    return output_image


# Adddddinggg salt and pepper noise to the input image
salt_prob = 0.02
pepper_prob = 0.02  
noisy_image = add_salt_and_pepper_noise(input_image, salt_prob, pepper_prob)


# Applying the Adaptive Median Filter
Smax = 7  
filtered_image = adaptive_median_filter(noisy_image, Smax)


# Output
cv2.imshow("Original Image", input_image)
cv2.imshow("Noisy Image", noisy_image)
cv2.imshow("Filtered Image", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


