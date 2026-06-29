import cv2

img = cv2.imread("shema.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

scan = cv2.adaptiveThreshold(
    gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11, 2
)

cv2.namedWindow("Scanned", cv2.WINDOW_NORMAL)
cv2.imshow("Scanned", scan)
cv2.waitKey(0)


