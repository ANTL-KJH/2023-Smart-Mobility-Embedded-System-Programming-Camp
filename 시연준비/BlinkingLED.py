"""
* Project : 2023 Smart Mobility Embedded System Programming Camp Photo Sensor
* Description : Blinking LED
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
p = GPIO.PWM(12, 0.5)  # channel 12, frequency 0.5Hz


def main():
    p.start(1)  # duty_cycle 1
    input("Press return to stop : ")
    p.stop()
    GPIO.cleanup()


if __name__ == "__main__":
    main()
