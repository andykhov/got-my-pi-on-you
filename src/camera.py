import cv2
import numpy

def takePicture(device, imgPath):
    webcam = cv2.VideoCapture(device)
    
    while (webcam.isOpened() == False):
        webcam.open(device)

    cv2.imwrite(imgPath, frame)
    webcam.release()
