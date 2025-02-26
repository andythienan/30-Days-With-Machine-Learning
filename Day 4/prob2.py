import cv2

image = cv2.imread("input.jpg")

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow("Grayscale Image", gray)
cv2.imshow("HSV Image", hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()
