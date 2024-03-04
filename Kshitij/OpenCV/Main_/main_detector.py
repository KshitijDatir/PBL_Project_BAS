# This function returns 1 When A face Is Detected Other wise 0:
#Function Only Apllicable To Images:

def detect(img):

    import cv2 as cv
    import numpy as np

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    #Face Detector Code:

    haar_cascade = cv.CascadeClassifier("haar_face.xml")

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)

    if len(faces_rect) >= 1:
       return 1
    else:
       return 0   


