from mail import email
import time
import RPi.GPIO as GPIO

def main():
    sensor = 16 #PIR sensor set at GPIO pin 16
    sensorState = 0  #sensorState refers to signal sent from sensor

    GPIO.setmode(GPIO.BOARD) #sets up GPIO's pin numbering to BOARD
    GPIO.setup(sensor, GPIO.IN) #inits pin of sensor as input

    #setup email, see "mail.py" for more information
    myEmail = email("myemail", "mypassword") #return an email object
    myEmail.initSMTP("smtp.gmail.com", 587) #connect to gmail's SMTP on port 587

    print("listening to sensor")

    try:
        while True:
            time.sleep(3)
            sensorState = GPIO.input(sensor)
            if sensorState == GPIO.HIGH: #check if sensor sends a signal
                myEmail.sendEmail("khovandyak@gmail.com", "Intruder\n"+time.strftime("Date: %x  Time(24 Hour): %X"))
                time.sleep(5) #give sensor time to refresh signal
    except KeyboardInterrupt:
        pass
    finally:
        print("exiting")
        GPIO.cleanup() #exit GPIO cleanly
        myEmail.closeSMTP() #close connection to SMTP server

if __name__ == '__main__':
    main()
