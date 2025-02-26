import cv2

image = cv2.imread("input.jpg")

cv2.rectangle(image, (50, 50), (200, 200), (0, 255, 0), 3)

cv2.circle(image, (300, 300), 50, (255, 0, 0), 3)

cv2.putText(image, "OpenCV Drawing", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("Drawing on Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
