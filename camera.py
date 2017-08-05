import pygame
import pygame.camera

class Webcam:

    webcamCount = 0;

    def __init__(self, device, resolution, colorspace):
        pygame.camera.init()
        self.cam = pygame.camera.Camera(device, (resolution[0], resolution[1]), colorspace)
        self.cam.start()

    def takePicture(self, imageName):
        self.img = self.cam.get_image()
        pygame.image.save(self.img, imageName)

    def stopCam(self):
        self.cam.stop()