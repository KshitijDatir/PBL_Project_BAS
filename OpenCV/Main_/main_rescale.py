# This Program Is Used To Rescale A Image:

def rescaleFrame(frame, scale=0.75):

    import cv2 as cv

    width = int(frame.shape[1] * scale)

    height = int(frame.shape[0] * scale)

    dimensions = (width , height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)