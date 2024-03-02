import cv2 as cv
import numpy as np
import os
import time

import main_rescale
import main_detector
import main_train_folder
import main_recogniser

people = []  #Needs To be Replaced
DIR = r'F:\Kshitij Folder\Python\Open CV\Kshitij\OpenCV\Faces Trainer'    #Directory Of Database


capture = cv.VideoCapture(0)

#Enroll Faces:

def Enroll(img_enroll,Name,img_count):
    img_path = os.path.join(DIR,f"{Name}")
    img_path = os.path.join(img_path,f"{Name}_{img_count}.png")
    cv.imwrite(img_path, img_enroll)

img_enroll1 = cv.imread(r"Faces Trainer/Adam Sandler/Adam Sandler 1.jpeg")
Enroll(img_enroll1,'AS',3)

#DETECT FACES ON LIVECAM:

def detect():
    while True:

        isTrue, frame = capture.read()

        #global detect_val

        detect_val = main_detector.detect(frame)

        time.sleep(0.33)

        #print(detect_val)
        
        cv.imshow('Enroll',frame)

        if detect_val == 1:

            input("Face Detected")
            cv.waitKey(0) 
            
            break
        else:
            None
            
        if cv.waitKey(1) & 0xFF==ord('d'):
            break
    capture.release() 
    cv.destroyAllWindows() 

    return detect_val 

# To Toggle the detector:
start_val = input('Do Want To Start The Program?')
if start_val == "Yes" :
    detect()

#To EnrollFace:
if detect() == 1:
    None    


main_train_folder.train(DIR)
