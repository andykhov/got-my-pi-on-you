# got-my-pi-on-you
I created a raspberry pi mini security system in an effort to let me know whenever my mom entered my room (she's a bit nosy).


## Components
* Raspberry Pi 3 Model B
* Logitech C270 USB Webcam (any usb webcam can be used)
* Passive Infrared Sensor (aka PIR)

![PIR Sensor](http://i.imgur.com/KFHnsMW.jpg)
![Logitech C270](http://i.imgur.com/N0FCvb1.jpg)
![Raspberry Pi 3 Model B](http://i.imgur.com/7inW1bQ.jpg)


## How it works
1. run main.py with python3
2. sets up before listening to PIR sensor (email, webcam, and GPIO interface)
3. listens to PIR sensor for a signal (1/true/GPIO.High)
4. sends an email to my email address with time of detection and image
5. listens again for the PIR sensor's signal (infinite loop)


## Libraries/Modules used
* RPi.GPIO (interface for Pi's GPIO)
* time
* mail
  * smtplib (module to interface with an smtp server)
  * MIMEText, MIMEImage, MIMEMultiport
* camera
  * pygame
