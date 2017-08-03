import RPi.GPIO as GPIO
import time

sensor = 16
sensorState = 0

GPIO.setmode(GPIO.BOARD) #sets up pin numbering to BOARD
GPIO.setup(sensor, GPIO.IN) #initializes channel of sensor as an input

try:
    while True:
        time.sleep(0.1)
        sensorState = GPIO.input(sensor)
        print(sensorState)
        if sensorState == GPIO.HIGH:
            sensorState = GPIO.LOW
            time.sleep(7)
        time.sleep(0.1)
        
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup();
