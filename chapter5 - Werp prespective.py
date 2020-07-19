import cv2 ## Werp prespective
import numpy as np

img = cv2.imread(r"C:\Users\91911\Desktop\openCV\resources\sharapova.jpg")

width,height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width,height))


cv2.imshow("Image", img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)
