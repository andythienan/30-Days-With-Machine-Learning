import cv2

image = cv2.imread("input.jpg")

# Resize 50%
resized_small = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# Resize 200%
resized_large = cv2.resize(image, (0, 0), fx=2.0, fy=2.0)

cv2.imshow("50% Resized Image", resized_small)
cv2.imshow("200% Resized Image", resized_large)

cv2.waitKey(0)
cv2.destroyAllWindows()
