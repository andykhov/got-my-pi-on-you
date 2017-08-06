# got-my-pi-on-you
This is my raspberry pi mini "security system". I initially created this project
in an effort to let me know whenever my mom entered my room whenever
I'm not home (she's a bit nosy). My project uses a passive infrared sensor
to detect an intruder in my room. The pi will then have my webcam take a 
picture and send an email to me with the date of time and picture attached.

If you have any questions/problems, let me know!

## Components
* [Raspberry Pi 3 Model B](http://i.imgur.com/7inW1bQ.jpg)
* [Logitech C270 USB Webcam](http://i.imgur.com/N0FCvb1.jpg) (any usb webcam can be used)
* [Passive Infrared Sensor](http://i.imgur.com/KFHnsMW.jpg) (aka PIR)

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
