import cv2 as cv
import numpy as np

# Create A Blank Image:

blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow('Blank', blank)

# 1. Paint The Image Of Certain Colour:

#blank[100:250, 300:350] = 0,200,300
#cv.imshow("Green", blank)

#img = cv.imread('Images/jacj Sparrow.jpeg')
#cv.imshow("JK" , img)



# 2. Draw A Rectangle:

cv.rectangle(blank, (0,0) , (250,250), (0,255,255), thickness= -1) #cv.FILLED is same as -1
#cv.imshow('Rectangle', blank)

# 3. Draw A Circle:

cv.circle(blank, (250,250), (40), (0,0,255), thickness= -1)
#cv.imshow("Cicle",blank)

# 4. Draw A Line:

cv.line(blank, (300,300), (250,250), (255,255,255), thickness= 3)
#cv.imshow("Line", blank)

# 5. Write A Text:

cv.putText(blank, "Hello World!!!", (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,100), thickness = 1)
cv.imshow("Text", blank)


# Always At Last:
cv.waitKey(0)