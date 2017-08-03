import RPi.GPIO as GPIO
import smtplib
import time

sensor = 16 #PIR sensor set at pin 16
sensorState = 0

#setup SMS message via email
emailserver = "smtp.gmail.com"
emailsender = "johndoe@gmail.com"
emailpassword = "password"
emailreceiver = "name@email"#t-mobile: number@tmomail.net
port = 587

message = "intruder alert" #alert message

#settings for Pi's GPIO
GPIO.setmode(GPIO.BOARD) #sets up pin numbering to BOARD
GPIO.setup(sensor, GPIO.IN) #initializes channel of sensor as an input

#enable connection to email server and login
smtpconnection = smtplib.SMTP(emailserver, port) #smtplib.SMTP returns an SMTP object
smtpconnection.ehlo() #says "hello" to the smtp server
smtpconnection.starttls() #enable TLS encryption
smtpconnection.login(emailsender, emailpassword)

print("listening to sensor")

try:
    while True:
        time.sleep(0.1)
        sensorState = GPIO.input(sensor) #sensorState refers to signal sent from sensor
        print(sensorState + "\r")
        if sensorState == GPIO.HIGH: #check if sensor sends a signal
            smtpconnection.sendmail(emailSender, emailReceiver, message + getTime())
            sensorState = GPIO.LOW
            time.sleep(7)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    print("preparing to exit")
    smtpserver.quit()
    GPIO.cleanup();

def getTime():
    return (time.strftime("%m") + "/" + time.strftime("%d") + ", " + time.strftime("%I") + ":" + time.strftime("%M") + ":" + time.strftime("%S"))
