import cv2
import numpy as np

# Read the gradient magnitude and direction images
gradient_magnitude = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\\10-30-23\CANNY\images\gradient_magnitude_output.png', cv2.IMREAD_GRAYSCALE)
gradient_direction = cv2.imread(r'C:\Users\Raja\PycharmProjects\Computer_Vision\\10-30-23\CANNY\images\gradient_direction_output.png', cv2.IMREAD_GRAYSCALE)

# Apply non-maximum suppression
def non_maximum_suppression(gradient_magnitude, gradient_direction):
    suppressed_image = np.copy(gradient_magnitude)
    for i in range(1, gradient_magnitude.shape[0] - 1):
        for j in range(1, gradient_magnitude.shape[1] - 1):
            angle = gradient_direction[i, j]
            if (0 <= angle < np.pi/4) or (7*np.pi/4 <= angle <= 2*np.pi):
                if (gradient_magnitude[i, j] < gradient_magnitude[i, j+1]) or (gradient_magnitude[i, j] < gradient_magnitude[i, j-1]):
                    suppressed_image[i, j] = 0
            elif (np.pi/4 <= angle < 3*np.pi/4):
                if (gradient_magnitude[i, j] < gradient_magnitude[i-1, j+1]) or (gradient_magnitude[i, j] < gradient_magnitude[i+1, j-1]):
                    suppressed_image[i, j] = 0
            elif (3*np.pi/4 <= angle < 5*np.pi/4):
                if (gradient_magnitude[i, j] < gradient_magnitude[i-1, j]) or (gradient_magnitude[i, j] < gradient_magnitude[i+1, j]):
                    suppressed_image[i, j] = 0
            else:  # 5*pi/4 <= angle < 7*pi/4
                if (gradient_magnitude[i, j] < gradient_magnitude[i-1, j-1]) or (gradient_magnitude[i, j] < gradient_magnitude[i+1, j+1]):
                    suppressed_image[i, j] = 0
    return suppressed_image

suppressed_image = non_maximum_suppression(gradient_magnitude, gradient_direction)


# Display the non-maximum suppressed image
cv2.imshow('Non-Maximum Suppression', suppressed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
