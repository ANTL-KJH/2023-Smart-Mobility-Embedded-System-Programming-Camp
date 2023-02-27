"""
* Project : 2023 Smart Mobility Embedded System Programming Camp Photo Sensor
* Description : Brighten and Dimming LED
* Author : JH KIM
* ======================================================================
* Program history
* ======================================================================
* Author        Date        Version         Modifications
* JH KIM        2023.02.13  v1.0            First Write
"""

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 50) # channel 12, frequency 50Hz


def main():
    p.start(0)  # initial duty_cycle = 0
    try:
        while True:
            for dc in range(0, 101, 5):
                p.ChangeDutyCycle(dc)  # dc : 0, 5, 10, 15, . . . ~ 95, 100
                time.sleep(0.1)
            for dc in range(100, -1, -5):
                p.ChangeDutyCycle(dc)  # dc : 100, 95, 90, . . . 5, 0
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    p.stop()


if __name__ == "__main__":
    main()
