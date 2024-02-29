# This Function Use Recogniser Algorithm To Return Labal:

def Recognise(img):
        import cv2 as cv
        import numpy as np
        import os

        people = os.listdir(r'F:\Kshitij Folder\Python\Open CV\Kshitij\OpenCV\Faces Trainer')

        haar_cascade = cv.CascadeClassifier('haar_face.xml')

        #features = np.load('features.npy' , allow_pickle = True)
        #labels = np.load('labels.npy')

        face_recognizer = cv.face.LBPHFaceRecognizer_create()
        face_recognizer.read('fMain_face_trained.yml')

        gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
        
        # Detect The Face:
        faces_rect= haar_cascade.detectMultiScale(gray , 1.1 , 4)
    
        for (x,y,w,h) in faces_rect:
            faces_roi = gray[y:y+h , x:x+h]

            label, confidence = face_recognizer.predict(faces_roi)
            print(f' Label = {people[label]} with a confidence of {confidence}')

            cv.putText(img , str(people[label]) , (20,20), cv.FONT_HERSHEY_COMPLEX , 1.0 ,  (0,255,0) , 2)
            cv.rectangle(img , (x,y) , (x+w,y+h) , (0,255,0), 2)

        cv.imshow('Detected Face', img)
        cv.waitKey(0)    





