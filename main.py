from mail import email
from camera import Webcam
import RPi.GPIO as GPIO
import time

def main():
    sensor = 16 #PIR sensor set at GPIO pin 16
    sensorState = 0  #sensorState refers to signal sent from 

    #setup Pi's GPIO
    GPIO.setmode(GPIO.BOARD) #sets up GPIO's pin numbering to BOARD
    GPIO.setup(sensor, GPIO.IN) #inits pin of sensor as input

    #setup email, see "mail.py" for more information
    myEmail = email("myemail", "mypassword") #return an email object
    myEmail.initSMTP("smtp.gmail.com", 587) #connect to gmail's SMTP on port 587

    #setup webcam
    myWebcam = Webcam("/dev/sda0", [1280,720], "RGB")

    print("listening to sensor...\n")

    try:
        while True:
            time.sleep(3)
            sensorState = GPIO.input(sensor)
            if sensorState == GPIO.HIGH: #check if sensor sends a signal
                date = time.strf("Date: %x  Time(24 Hour): %X")
                myEmail.sendEmail("recipientEmail", "Intruder\n"+date)
                myWebcam.takePicture(date + ".jpg")
                time.sleep(60) #give sensor time to refresh signal
    except KeyboardInterrupt:
        pass
    finally:
        print("exiting...\n")
        GPIO.cleanup() #exit GPIO cleanly
        myWebcam.stopCam()
        myEmail.closeSMTP() #close connection to SMTP server

if __name__ == '__main__':
    main()
