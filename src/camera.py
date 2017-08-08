import cv2
import numpy
import time

def takePicture(device, imgPath):
    webcam = cv2.VideoCapture(device)

    while (webcam.isOpened()):
        webcam.open(device)
        time.sleep(1)

    ret, frame = webcam.read()
    cv2.imwrite(imgPath, frame)

    webcam.release()
