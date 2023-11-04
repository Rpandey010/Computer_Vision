import cv2

# Load the image
image_path = r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\einstein.jpg'
image = cv2.imread(image_path)


# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to load image.")
else:
    # Convert the image to its negative
    negative_image = 255 - image

    # Original as well as negative images
    cv2.imshow('Original Image', image)
    cv2.imshow('Negative Image', negative_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
