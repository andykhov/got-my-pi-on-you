# got-my-pi-on-you
Raspberry Pi Mini Security System


## Components
* Raspberry Pi 3 Model B
* Logitech C270 USB Webcam (any usb webcam can be used)
* Passive Infrared Sensor (aka PIR)


## How it works
1. run main.py with python3
2. sets up before listening to PIR sensor (setup email, webcam, and GPIO interface)
3. listens to PIR sensor for a signal (1/true/GPIO.High)
4. sends an email to user's email address with time of detection  and .jpg file
5. listens again for the PIR sensor's signal


## Libraries/Modules used
* RPi.GPIO (interface for Pi's GPIO)
* time
* mail
  * smtplib (module to interface with an smtp server)
  * MIMEText, MIMEImage, MIMEMultiport
* camera
  * pygame
