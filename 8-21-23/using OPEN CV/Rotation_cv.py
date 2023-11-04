import cv2

def rotate_image(image, angle):
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

# Load your input image
input_image_path = r'C:\Users\Raja\PycharmProjects\Computer_Vision\img\einstein.jpg'  
original_image = cv2.imread(input_image_path)

if original_image is None:
    print("Failed to load the input image.")
else:
    # Creating while loop
    while True:
        cv2.imshow("Image", original_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        rotation_angle = int(input("Enter rotation angle (90, 180): "))
        if rotation_angle not in [90, 180]:
            print("Invalid angle. Supported angles are 90 and 180 degrees.")
            continue

        original_image = rotate_image(original_image, rotation_angle)

        cv2.imshow("Rotated Image", original_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        continue_option = input("Do you want to continue rotating? (yes/no): ")
        if continue_option.lower() != 'yes':
            break

    # Save the final rotated image
    output_image_path = "final_rotated_image.jpg"
    cv2.imwrite(output_image_path, original_image)
    print(f"Final rotated image saved as {output_image_path}")
