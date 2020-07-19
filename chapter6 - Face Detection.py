import cv2  ## Joining images
import numpy as np

img = cv2.imread(r"C:\Users\91911\Desktop\openCV\resources\sharapova.jpg")
# img1 = cv2.resize(img,(250,300))

## some code are the copy from the video github account the we can concat many images...
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)  ## convert the img to blur image
imgCanny = cv2.Canny(img,100,100)  ## image age detector, (img,100,100) stand for how many canny/edges want high value means few canny like 150,200
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)  ## increse the edge detector size
imgEroded = cv2.erode(imgDialation,kernel,iterations=1) ## decrese the edge detector size



imgStack = stackImages(0.5,([img,imgGray,imgBlur],[imgCanny,imgDialation,imgEroded]))

# imgHor = np.hstack((img1,img1))
# imgVer = np.vstack((img1,img1))

# cv2.imshow("Horizontal", imgHor)
# cv2.imshow("vertical", imgVer)
cv2.imshow("ImageStack",imgStack)

cv2.waitKey(0)

