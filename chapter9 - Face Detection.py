import cv2 ##Face Detection
## us the method is Viola & Jones
# Needs :
#     1. Positive Faces more
#     2. Negatives Non Faces
# Than Train them --(convert them)-->  XML file
## for this we use pre-train files which is provided by the openCV
faceCascade = cv2.CascadeClassifier(r"C:\Users\91911\Desktop\openCV\resources\haarcascade_frontalface_default.xml")
img = cv2.imread(r"C:\Users\91911\Desktop\openCV\resources\sharapova.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Result",img)
cv2.waitKey(0)