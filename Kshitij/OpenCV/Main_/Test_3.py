import cv2 as cv
import numpy as np
import time 
import os

import main_rescale
import main_detector
import main_train
import main_recogniser
import main_enroll

video = cv.VideoCapture(0)

# def face
x = 0
enrol_flag = False
while True:
    flag, frame = video.read()
    x = main_detector.detect(frame)   
    
    if cv.waitKey(1)==ord('e')  and x == 1:
        enrol_flag = True
        break
        
    
    cv.imshow("demo",frame) 
    if cv.waitKey(1)== ord('q'):
        break

if enrol_flag == True:
    name = input("Enter A Name:")
    counter = 1 
    while True:
            
       
        flag, frame = video.read()
        cv.imshow('name',frame)
        if cv.waitKey(1) == ord("s"):
            
            main_enroll.enroll(frame,counter,name)
            print(f"{counter} images saved")
            counter += 1
            
        
        if cv.waitKey(1)== 27:
            break
    
