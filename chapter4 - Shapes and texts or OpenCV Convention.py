import cv2   ## Shapes and texts or OpenCV Convention
import numpy as np

img = np.zeros((512, 512,3),np.uint8) ## Gray image no color
print(img.shape)
#img[200:300,100:300] = 255,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) ## img.shape[0] --> height, img.shape[1] --> width , shape(height, width)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2) # cv2.FILLED  ## image, starting point, ending_point, thikness
cv2.circle(img,(400,50),30,(255,255,0),5) ## image, starting point, radius, thikness 

cv2.putText(img,"OpenCV",(300,100),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,150,0),1) ## image, image_name, starting_point, fontstyle, fontsize, color, thikness

cv2.imshow("Image",img)

cv2.waitKey(0)