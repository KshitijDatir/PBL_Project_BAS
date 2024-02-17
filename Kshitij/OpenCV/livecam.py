import os
import cv2 as cv

# Set The Directory Where You Want To Save  Your Images

livecam = "Faces Trainer\LiveCam"

# Initiate the Webcam

cap = cv.ViceoCapture(0)

image_count = 0

while True:
    # Capture Freame By Frame
    ret, frame = cap.read()

    # Display The resulting Frame
    cv.imshow('Webcam', frame)

    # Save the image when 's' Ke Is Pressed
    key = cv.waitkey(1) & 0xFF
    if key ==ord('s'):
        image_count +=1
        image_path = os.path.join(livecam,f"image_{image_count}.png")
        cv.imwrite(image_path, frame)
        print(f"Image {image_count} Saved At {image_path}")

    # Break The Loop When "q" Key Is  Pressed
    elif key == ord('q'):
        break    

# Realease The Webcam And Close The Opencv Window
cap.release()
cv.destroyAllWindows()    










