import cv2 as cv
import main_recogniser

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width , height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
                     

capture = cv.VideoCapture(0)


while True:

    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.8)
    
    main_recogniser.Recognise(frame)

    if cv.waitKey(1) & 0xFF==ord('d'):
        break
capture.release() 
cv.destroyAllWindows() 




