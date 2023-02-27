"""
* Project : 2023 Smart Mobility Embedded System Programming Camp Photo Sensor
* Description : Photo Sensor test with spidev module
* Author : JH KIM
* ======================================================================
* Program history
* ======================================================================
* Author        Date        Version         Modifications
* JH KIM        2023.02.13  v1.0            First Write
"""

import time
import RPi.GPIO as GPIO
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 500000
MCP3208_CS_PIN = 13
LED_PIN = 38


def ADC_DAC_Init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(MCP3208_CS_PIN, GPIO.OUT)
    GPIO.setup(LED_PIN, GPIO.OUT)


def MCP3208_read(channel):
    chD2 = (channel & 0x04) >> 2
    chD1 = (channel & 0x02) >> 1
    chD0 = (channel & 0x01)
    octet_0 = 0x01 << 2  # MCP3208_SB
    octet_0 |= 0x01 << 1  # MCP3208_SD
    octet_0 |= chD2 << 0  # MCP3208_D2
    octet_1 = chD1 << 7  # MCP3208_D1
    octet_1 |= chD0 << 6  # MCP3208_D0
    octet_2 = 0x00
    octets = [octet_0, octet_1, octet_2]
    GPIO.output(MCP3208_CS_PIN, GPIO.LOW)
    adc_0, adc_1, adc_2 = spi.xfer(octets)
    GPIO.output(MCP3208_CS_PIN, GPIO.HIGH)
    adc = adc_2
    adc |= (adc_1 & 0x0F) << 0x08
    return adc


def main():
    ADC_DAC_Init()
    pwm = GPIO.PWM(LED_PIN, 100)
    pwm.start(0)
    while True:
        photo_val = MCP3208_read(0)
        # print ("{}, {}".format (4096 - photo_val, photo_val))
        light = float(4096 - photo_val)
        if light > 100:
            light = 100
        pwm.ChangeDutyCycle(light)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
