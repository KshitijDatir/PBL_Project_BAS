# This Function Trains Data Model Live:
#Currently Not Working!!!

def live_train(img, label, name):
        
    import cv2 as cv
    import numpy as np
    import os

    haar_cascade = cv.CascadeClassifier("haar_face.xml")

    features = []
    labels = []

    def create_train():

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                
        faces_rect = haar_cascade.detectMultiScale( gray , scaleFactor=1.1 , minNeighbors=4 )

        for (x,y,w,h) in faces_rect:
            faces_roi = gray[ y:y+h , x:x+w ]
            features.append(faces_roi)
            labels.append(label)

        create_train()

        print(f'Face Enrolled!! Wwelcome {name}')

        features = np.array(features , dtype='object')
        labels = np.array(labels)


        #print(f'Lenght of the Features = {len(features)}')
        #print(f'Lenght of the Labels = {len(labels)}')

        face_recognizer = cv.face.LBPHFaceRecognizer_create()

        # Train The Recognizer on Features and Labels List:

        face_recognizer.train(features,labels)
        face_recognizer.save('main_face_trained.yml')
        np.save('main_features.npy' , features)
        np.save('main_labels.npy' , labels)    