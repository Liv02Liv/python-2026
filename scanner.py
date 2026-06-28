
import cv2
import os

pasta = os.path.dirname(os.path.abspath(__file__))
caminho = os.path.join(pasta, "c0c174250bffd16cb8f625ee9c97787d.jpg")
img = cv2.imread("c0c174250bffd16cb8f625ee9c97787d.jpg")

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
