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

import RPi.GPIO as GPIO
import time

servo_pin=18
GPIO.setmode(GPIO.BCM)GPIO.setup(servo_pin,GPIO.OUT)
pwm=GPIO.PWM(servo_pin,50)
pwm.start(3.0)

pwm.ChangeDutyCycle(3.0)  #서보모터 0도 회전
Time.sleep(1.0)
pwm.ChangeDutyCycle(7.5) #서보모터 90도 회전
Time.sleep(1.0)
pwm.ChangeDutyCycle(12.5) #서보 모터 180도회전
time.sleep(1.0)


pwm.ChangeDutyCycle(0.0)
pwm.stop()
GPIO.cleanup()
