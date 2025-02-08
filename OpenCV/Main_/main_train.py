# This  Function Updates YML File:    
#Starts From Label Zero:

def train_images(list):
    
    
    print(list)
    import os
    import cv2 as cv
    import numpy as np

    DIR = r"F:\Kshitij Folder\Python\Open CV\Kshitij\OpenCV\Main_\Image_DB"

    haar_cascade = cv.CascadeClassifier("F:\Kshitij Folder\Python\Open CV\Kshitij\OpenCV\Main_\haar_face.xml")
    
    people = list

    features = []
    labels = []

    def create_train():
        for person in people:
           path = os.path.join(DIR , person)
           label = people.index(person)

           for img in os.listdir(path):
               img_path = os.path.join(path,img)
               print(img_path)
               img_array = cv.imread(img_path)
               gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
        
               faces_rect = haar_cascade.detectMultiScale( gray , scaleFactor=1.1 , minNeighbors=4 )

               for (x,y,w,h) in faces_rect:
                   faces_roi = gray[ y:y+h , x:x+w ]
                   features.append(faces_roi)
                   labels.append(label)   
    create_train()
    
    features = np.array(features , dtype='object')
    labels = np.array(labels)


    #print(f'Lenght of the Features = {len(features)}')
    #print(f'Lenght of the Labels = {len(labels)}')

    face_recognizer = cv.face.LBPHFaceRecognizer_create()

    # Train The Recognizer on Features and Labels List:
    face_recognizer.train(features,labels)

    face_recognizer.save(r'F:\Kshitij Folder\Python\Open CV\Kshitij\OpenCV\Main_\Main_face_trained.yml')

    np.save(r'F:\Kshitij Folder\Python\Open CV\Kshitij\OpenCV\Main_\Main_features.npy' , features)
    np.save(r'F:\Kshitij Folder\Python\Open CV\Kshitij\OpenCV\Main_\Main_labels.npy' , labels)





