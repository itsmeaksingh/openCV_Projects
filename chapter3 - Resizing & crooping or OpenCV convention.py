import cv2  # Resizing & crooping or OpenCV convention
import numpy as np

img = cv2.imread(r"C:\Users\91911\Desktop\openCV\resources\sharapova.jpg")
print(img.shape)  ## height, width, color_no

imgResize = cv2.resize(img,(100,100)) # values --> width , height
print(imgResize.shape)  ## print --> height, width, color_no


imgCropped = img[0:200,200:500]

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)


cv2.waitKey(0)


