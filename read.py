import cv2 as cv

# Reading Vedios

capture = cv.VideoCapture("Videos/Video 1.mov")

while True:

    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release() 
cv.destroyAllWindows()   