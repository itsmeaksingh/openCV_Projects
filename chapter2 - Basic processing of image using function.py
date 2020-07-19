import cv2  # Basic processing of image using function
import numpy as np


img = cv2.imread(r"C:\Users\91911\Desktop\openCV\resources\my_photo.jpg")
# img = cv2.imread(r"C:\Users\91911\Pictures\my photo\IMG_20200608_120457.jpg")
kernel = np.ones((5,5),np.uint8)  ## uint8 --> positive integer

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert the colour img to gray
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)  ## convert the img to blur image
imgCanny = cv2.Canny(img,100,100)  ## image age detector, (img,100,100) stand for how many canny/edges want high value means few canny like 150,200
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)  ## increse the edge detector size
imgEroded = cv2.erode(imgDialation,kernel,iterations=1) ## decrese the edge detector size

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("imgDialation Image", imgDialation)
cv2.imshow("imgEroded Image", imgEroded)


# note : if you give the name is same the it run first and just second and you dont get the secong img only get the last one
##  name is like a id for show the image

cv2.waitKey(0) ## press any key to remove the img








