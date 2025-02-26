import cv2

image = cv2.imread("input.jpg")

cv2.imshow("Original Image", image)

cv2.imwrite("output.png", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
