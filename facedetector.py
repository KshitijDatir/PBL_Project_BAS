import cv2 as cv

#img = cv.imread('Images/Dyane Johnson.jpeg')
#cv.imshow("JK" , img)

#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Gray Img", gray)

# Face Detector Code:

# haar_cascade = cv.CascadeClassifier("haar_face.xml")

# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)

# print(f"No. Of Faces Are:{len(faces_rect)}")

# for (x,y,w,h) in faces_rect:
#     cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0),thickness=2)
# cv.imshow("Detected Faces",img)    

#Face Detector Code End.

# cv.waitKey(0)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width , height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
                     

capture = cv.VideoCapture("Videos/samplevedio1.mp4")

while True:

    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.3)
    
    gray = cv.cvtColor(frame_resized, cv.COLOR_BGR2GRAY)

    haar_cascade = cv.CascadeClassifier("haar_face.xml")

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=6)

    # print(f"No. Of Faces Are:{len(faces_rect)}")

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame_resized, (x,y), (x+w,y+h), (0,255,0),thickness=2)
        
    cv.imshow("Detected Faces",frame_resized)

    if cv.waitKey(1) & 0xFF==ord('d'):
        break
capture.release() 
cv.destroyAllWindows() 