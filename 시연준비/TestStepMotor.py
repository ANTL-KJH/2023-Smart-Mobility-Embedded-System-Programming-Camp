"""
* Project : 2023 Smart Mobility Embedded System Programming Camp Servo Motor Test
* Description : Servo Motor Test
* Author : JH SUN
* ======================================================================
* Program history
* ======================================================================
* Author        Date        Version         Modifications
* JH Sun        2023.02.10  v1.0            First Write
"""
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
StepPins = [12, 16, 20, 21]

for pin in StepPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)
StepCounter = 0
StepCount = 4
Seq = [[1, 0, 0, 0].[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

try:
    while True:
        for pin in range(0, 4):
            xpin = StepPins[pin]
        if Seq[StepCounter][pin] == 1:
            GPIO.output(xpin, True)
        else:
            GPIO.output(xpin, False)
        StepCounter += 1

        if(StepCounter==StepCount):
            StepCounter=0
        if(StepCounter<0):
            StepCounter=StepCount
        time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()
