import cv2
import numpy as np

img = cv2.imread("Resources/house.jpg")
print(img.shape)

imgResize = cv2.resize(img, (400, 300))

cv2.imshow("Image", img)
cv2.waitKey(0)

cv2.imshow("Image resize", imgResize)
cv2.waitKey(0)

imgCropped = img[0:200, 200:500]
cv2.imshow("Cropped image", imgCropped)
cv2.waitKey(0)