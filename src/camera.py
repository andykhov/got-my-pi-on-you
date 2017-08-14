import cv2
import numpy

class Webcam:

    def __init__(self, device, fps):
        self.cam = cv2.VideoCapture(device)
        self.fps = fps
        while (self.cam.isOpened() == False):
            self.cam.open(device)

    def takePicture(self, imgPath):
        for i in range(self.fps):
            retval, frame = self.cam.read()
        cv2.imwrite(imgPath, frame)

    def closeWebcam(self):
        self.cam.release()
