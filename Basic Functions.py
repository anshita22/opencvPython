import cv2
import numpy as np

img = cv2.imread("Resources/my pic.png")
kernel= np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)

imgBlur= cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("Blur Image", imgBlur)
cv2.waitKey(0)

imgCanny = cv2.Canny(img, 100, 100)
cv2.imshow("Canny Image", imgCanny)
cv2.waitKey(0)

imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
cv2.imshow("Dilation image", imgDilation)
cv2.waitKey(0)

imgEroded = cv2.erode(imgDilation, kernel, iterations= 1)
cv2.imshow("Eroded Image", imgEroded0.)
cv2.waitKey(0)