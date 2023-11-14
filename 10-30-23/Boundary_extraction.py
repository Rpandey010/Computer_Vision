import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Raja\PycharmProjects\Computer_Vision\img\Polka.jpg")

def boundary_extraction(image):
    h, w, _ = image.shape
    boundary = np.zeros((h, w), dtype=np.uint8)

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            # Calculate the gradient using Sobel operators
            dx = int(image[y, x + 1, 0]) - int(image[y, x - 1, 0])
            dy = int(image[y + 1, x, 0]) - int(image[y - 1, x, 0])
            gradient_magnitude = np.sqrt(dx**2 + dy**2)

            # Threshold the gradient magnitude to find edges
            if gradient_magnitude > 105:
                boundary[y, x] = 255

    return boundary

boundary = boundary_extraction(image)

cv2.imshow("Input Image", image)
cv2.imshow("Boundary", boundary)
cv2.waitKey(0)
cv2.destroyAllWindows()