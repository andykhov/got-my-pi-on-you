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
    subject = "Intruder Alert"
    recipient = "recipient@email"

    #setup webcam
    myWebcam = Webcam("/dev/video0", [640,480], "RGB")
    imgPath = "images/intruder.jpg"

    print("listening to sensor...\n")

    try:
        while True:
            time.sleep(2)
            sensorState = GPIO.input(sensor)
            if sensorState == GPIO.HIGH: #check if sensor sends a signal
                date = time.strftime("Date: %x Time(24Hour): %X")
                myWebcam.takePicture(imgPath)
                myEmail.sendEmail(recipient, subject, date, imgPath)
                time.sleep(60) #give sensor time to refresh signal & prevent
                #subsequent emails
    except KeyboardInterrupt:
        pass
    finally:
        print("exiting...\n")
        GPIO.cleanup() #exit GPIO cleanly
        myWebcam.stopCam()
        myEmail.closeSMTP() #close connection to SMTP server
        time.sleep(5)

if __name__ == '__main__':
    main()