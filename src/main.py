import camera
import RPi.GPIO as GPIO
import time
from mail import email

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

    #image file path for webcam screen capture
    imgPath = "images/intruder.jpg"

    print("listening to sensor...")

    try:
        while True:
            time.sleep(2)
            sensorState = GPIO.input(sensor)
            if sensorState == GPIO.HIGH: #check if sensor sends a signal
                date = time.strftime("Date: %x Time(24Hour): %X")
                camera.takePicture(0, imgPath)
                myEmail.sendEmail(recipient, subject, date, imgPath)
                time.sleep(60) 

    except KeyboardInterrupt:
        pass
    finally:
        print("exiting...")
        GPIO.cleanup() #exit GPIO cleanly
        myEmail.closeSMTP() #close connection to SMTP server

if __name__ == '__main__':
    main()
