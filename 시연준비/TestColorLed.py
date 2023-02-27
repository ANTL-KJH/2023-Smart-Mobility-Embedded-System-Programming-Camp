import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
RUNNING = True
red = 13
green = 19
blue = 26
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
Freq = 100
RED = GPIO.PWM(red, Freq)
GREEN = GPIO.PWM(green, Freq)
BLUE = GPIO.PWM(blue, Freq)

try:
    RED.start(1)
    GREEN.start(1)
    BLUE.start(1)
    while RUNNING:
        for x in range(1, 101, 5):
            BLUE.ChangeDutyCycle(101 - x)
            GREEN.ChangeDutyCycle(x)
            time.sleep(0.05)
        for x in range(1, 101, 5):
            GREEN.ChangeDutyCycle(101 - x)
            RED.ChangeDutyCycle(x)
            time.sleep(0.05)
        for x in range(1, 101, 5):
            RED.ChangeDutyCycle(101 - x)
            BLUE.ChangeDutyCycle(x)
            time.sleep(0.05)
except KeyboardInterrupt:
    RUNNING = False
    GPIO.cleanup()
