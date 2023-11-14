import cv2
import numpy as np

# Load the input image
input_image = cv2.imread(r"C:\Users\Raja\PycharmProjects\Computer_Vision\img\ladyinhat.png", cv2.IMREAD_GRAYSCALE)

# Rescale the image intensity values to fit within 0-255
# input_image = cv2.normalize(input_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Create a blank image of the same shape as the input image
x, y = input_image.shape
noisy_image = np.zeros((x, y), dtype=np.uint8)

# Salt and pepper noise levels
pepper = 0.1
salt = 0.95

# Add salt and pepper noise to the image
for i in range(x):
    for j in range(y):
        rdn = np.random.random()
        if rdn < pepper:
            noisy_image[i][j] = 0  # Pepper noise (black)
        elif rdn > salt:
            noisy_image[i][j] = 255  # Salt noise (white)
        else:
            noisy_image[i][j] = input_image[i][j]

# Adaptive Median Filter
Smax = 7
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

                A1 = Zmed - Zmin
                A2 = Zmed - Zmax

                if A1 > 0 and A2 < 0:
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

# Applying the Adaptive Median Filter to remove noise
# Smax = 7
filtered_image = adaptive_median_filter(noisy_image, Smax)

# Display the original, noisy, and filtered images
cv2.imshow("Original Image", input_image)
cv2.imshow("Noisy Image", noisy_image)
cv2.imshow("Filtered Image", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
