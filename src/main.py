import RPi.GPIO as GPIO
import time
from mail import email
from camera import Webcam

def main():
    sensor = 16 #PIR sensor set at GPIO pin 16
    sensorState = 0 #sensorState refers to signal sent from 
    videoDevice = 0 #0 is the default videoDevice
    fps = 30 #fps of video device

    print("preparing sensor")

    #setup Pi's GPIO
    GPIO.setmode(GPIO.BOARD) #sets up GPIO's pin numbering to BOARD
    GPIO.setup(sensor, GPIO.IN) #inits pin of sensor as input

    print("preparing webcam")

    cam = Webcam(videoDevice, fps)

    print("preparing email")

    #setup email, see "mail.py" for more information
    myEmail = email("myemail", "mypassword") #return an email object
    myEmail.initSMTP("smtp.gmail.com", 587) #connect to gmail's SMTP on port 587
    subject = "Intruder Alert"
    recipient = "recipient@email"

    #image file path for webcam screen capture
    imgPath = "images/intruder.jpg"

    print("listening to sensor...")

    try:
        while True:
            time.sleep(2)
            sensorState = GPIO.input(sensor)
            print(sensorState)
            if sensorState == GPIO.HIGH: #check if sensor sends a signal
                date = time.strftime("Date: %x Time(24Hour): %X")
                print("taking pic")
                cam.takePicture(imgPath)
                print("sending email")
                myEmail.sendEmail(recipient, subject, date, imgPath)
                print("sent")
                time.sleep(60) 

    except KeyboardInterrupt:
        pass
    finally:
        print("exiting...")
        GPIO.cleanup() #exit GPIO cleanly
        cam.closeWebcam()
        myEmail.closeSMTP() #close connection to SMTP server

if __name__ == '__main__':
    main()
