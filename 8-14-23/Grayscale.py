import cv2
img = cv2.imread('img/2049.jpg', 0)

# Resizing (I was not getting the full image in output)
cv2.namedWindow('img/2049', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img/2049', img.shape[1], img.shape[0])

print(img)
cv2.imshow('img/2049', img)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('test.png', img)
    cv2.destroyAllWindows()


