
import cv2 as cv
import numpy as np
#import time 
import os

#import main_rescale
import main_detector
#import main_train_folder
#import main_recogniser
import main_enroll

video = cv.VideoCapture(0)

DIR = "F:\Kshitij Folder\Python\Open CV\Kshitij\OpenCV\Main_\Image_DB"

# def face
x = 0
enrol_flag = False
while True:
    flag, frame = video.read()
    x = main_detector.detect(frame)   
    
    
    cv.imshow("Name",frame)

    if cv.waitKey(1)==ord('e')  and x == 1:
        enrol_flag = True
        cv.destroyAllWindows()
        
        break
        
    
    
    if cv.waitKey(1)== ord('q'):
        break

if enrol_flag == True:
    while True:

        name = input("Enter A Name:")

        img_path_0 = f"{DIR}\{name}"

        flag1 = os.path.isdir(img_path_0)
        if not flag1:
            break
        print("Directory already exists") 

    counter = 1

    while True:
            
       
        flag, frame = video.read()
        
        if cv.waitKey(1) == ord("s"):
            cv.imshow('name',frame)
            main_enroll.enroll(frame,counter,name)

             

            print(f"{counter} images saved")
            counter += 1
            
        
        if cv.waitKey(1)== 27:
            break
    