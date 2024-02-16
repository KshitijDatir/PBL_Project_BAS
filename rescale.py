import cv2 as cv

# Rescaling Vedios,Images or Live Vedios

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width , height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
                     

capture = cv.VideoCapture("Videos/Video 1.mov")

while True:

    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.3)


    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release() 
cv.destroyAllWindows()  

# For Live Vedio Only 

def changeRes(width, height):

    capture.set(3, width)
    capture.set(4,height)

    