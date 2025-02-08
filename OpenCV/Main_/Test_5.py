import cv2 as cv
import os

import main_detector
import main_enroll
import main_train as mt

DIR = r"F:\Kshitij Folder\Python\Open CV\Kshitij\OpenCV\Main_\Image_DB"

#Live Cam (Always On):

capture = cv.VideoCapture(0)

enroll_flag = False


def train(name):

        DIR2 = r"F:\Kshitij Folder\Python\Open CV\Kshitij\OpenCV\Main_\Image_DB"


        #Creating A File For Storing Each Person's Name:

        def create_file(person):
        
            with open("F:\Kshitij Folder\Python\Open CV\Kshitij\OpenCV\Main_\DB_File\People","a+") as People_File:
                People_File.write(f"{person}\n") 
                #index = len(People_File.readlines)

        create_file(name)    
        #index = create_file.index

        def make_list():

            with open("F:\Kshitij Folder\Python\Open CV\Kshitij\OpenCV\Main_\DB_File\People","r") as People_File:
                list=[]
                for line in People_File:
                    list.append(line)
                    
                for i in range(0,len(list)):
                    
                    list[i] = list[i].replace("\n","")
                    

            return list
        
        # Main List: ******************************************************************************************************
        list = make_list()
        

        # mtf.main_train(DIR2,list,name)
        mt.train_images(list)

        print("Data Trained,Enrollment Successful")



def Image_save(enroll_flag):        

        if enroll_flag == True:
            capture2 = cv.VideoCapture(0)
            while True:

                name = input("Enter A  Name:")

                img_path_0 = f"{DIR}\{name}"

                
                flag1 = os.path.isdir(img_path_0)

                if not flag1:
                    break
                print("Directory already exists") 

            counter = 1   

            while True: 

                flag,frame = capture2.read()

                cv.imshow("Capturing Images",frame)

                save_key = input("Press \'s\' to Capture An Image of")
                print("Press 'q' to quit ")

                if save_key == "s" :
                    
                    main_enroll.enroll(frame,counter,name)


                    print(f"{counter} Images Saved.")
                    counter += 1
                    
                    
                elif save_key == "q":

                    train(name)

                    capture2.release
                    cv.destroyAllWindows
                    break



while True:

    flag,frame = capture.read()

    detect_flag = main_detector.detect(frame)

    cv.imshow("Always On",frame)

    enroll_key = input("Press \'e\' to Enter Enroll Mode.")

    if enroll_key == "e" :
        enroll_flag = True 
        print("Enroll Mode Is Active")

        Image_save(enroll_flag)
        capture.release()
        cv.destroyAllWindows()

        break
        
    if cv.waitKey(1) == 27:
        capture.release
        cv.destroyAllWindows
        break


