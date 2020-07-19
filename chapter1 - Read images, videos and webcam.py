import cv2   #Read images, videos and webcam
# print("Package Imported")

############# for image read and display ##################
# img = cv2.imread(r"C:\Users\91911\Desktop\openCV\resources\sharapova.jpg")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

######## for video read and display #################
# cap = cv2.VideoCapture(r"E:\Courses\faceRecogniation\Data Science & Machine Learning Project - Part 1 Introduction - Image Classification.mp4")

# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


############### for WebCam #############
cap = cv2.VideoCapture(0)  ## 0 = first camera , 1 = if second camera have
cap.set(3,640) ## 3 is id for width
cap.set(4,480) ## 4 is id for height
cap.set(10,100) ## 10 stands for brightness
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


