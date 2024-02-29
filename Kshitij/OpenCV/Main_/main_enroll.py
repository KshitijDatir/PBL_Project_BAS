import os
import cv2 as cv

DIR = "/home/soham/codes/pbl/PBL_Project_BAS/Kshitij/OpenCV/Main_/faces_DB"

def enroll(frame,counter,name):
    
    os.chdir(DIR)
    if counter == 1:
        os.mkdir(f"{name}")
    
    img_path_1 = os.path.join(DIR,name)
    img_path_2 = os.path.join(img_path_1,f"{name}_{counter}.png")
    cv.imwrite(img_path_2, frame)


# enroll()