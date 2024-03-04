
def enroll(frame,counter,name):
    import os
    import cv2 as cv
    DIR = "F:\Kshitij Folder\Python\Open CV\Kshitij\OpenCV\Main_\Image_DB"   
    os.chdir(DIR)


    if counter == 1:
        os.mkdir(f"{name}")
        
    
    img_path_1 = os.path.join(DIR,name)
    img_path_2 = os.path.join(img_path_1,f"{name}_{counter}.png")
    cv.imwrite(img_path_2, frame)


# enroll()