import cv2

# Load the input image
input_image_path = r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\einstein.jpg'  # Replace with the path to your image
input_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

if input_image is None:
    print("Failed to load the input image.")
else:
    # Scaling parameters
    scale_x = 2
    scale_y = 2

    # Calculate the new dimensions for the scaled image
    height, width = input_image.shape[:2]
    new_height = int(height * scale_y)
    new_width = int(width * scale_x)

    # Initialize the output image for scaling
    output_image_scaling = cv2.resize(input_image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    # Display input and output images
    cv2.imshow("Input Image", input_image)
    cv2.imshow("Scaled Image", output_image_scaling)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the scaled image
    output_image_path = "scaled_image.jpg"
    cv2.imwrite(output_image_path, output_image_scaling)
    print(f"Scaled image saved as {output_image_path}")
