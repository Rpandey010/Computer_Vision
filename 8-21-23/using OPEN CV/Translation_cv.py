import cv2
import numpy as np

# Load the input image
input_image_path = r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\fruits.jpg'  # Replace with the path to your image
input_image = cv2.imread(input_image_path)

if input_image is None:
    print("Failed to load the input image.")
else:
    # Define the translation parameters (Tx and Ty)
    Tx = 2
    Ty = -1

    # Create the transformation matrix for translation
    translation_matrix = np.float32([[1, 0, Tx], [0, 1, Ty]])

    # Apply the translation to the input image
    output_image_translation = cv2.warpAffine(input_image, translation_matrix, (input_image.shape[1], input_image.shape[0]))

    # Display input and output images
    cv2.imshow("Input Image", input_image)
    cv2.imshow("Translated Image", output_image_translation)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the translated image
    output_image_path = "translated_image.jpg"
    cv2.imwrite(output_image_path, output_image_translation)
    print(f"Translated image saved as {output_image_path}")
