import pygame
import pygame.camera

class Webcam:

    webcamCount = 0;

    def __init__(self, device, resolution, colorspace):
        pygame.camera.init() #initialize the camera module
        #load specified camera, "device"
        self.cam = pygame.camera.Camera(device, (resolution[0], resolution[1]), colorspace)
        self.cam.start() #webcam opens, initializes and starts capturing

    #captures an image frame and saves it to imageName
    def takePicture(self, imageName):
        self.img = self.cam.get_image()
        pygame.image.save(self.img, imageName)

    #webcam stops, uninitializes, and closes
    def stopCam(self):
        self.cam.stop()
