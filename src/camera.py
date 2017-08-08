import cv2
import numpy
import time

def takePicture(device, imgPath):
    webcam = cv2.VideoCapture(device) #returns a VideoCapture obj

    #poll until webcam is opened and ready
    while (webcam.isOpened()):
        webcam.open(device)
        time.sleep(1)

    ret, frame = webcam.read() #reads current fram from webcam
    cv2.imwrite(imgPath, frame) #save frame to imgPath

    webcam.release()
