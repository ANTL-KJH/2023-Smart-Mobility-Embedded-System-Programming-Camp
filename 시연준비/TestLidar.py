"""
* Project : 2023 Smart Mobility Embedded System Programming Camp Lidar Test
* Description : get distance from TF-mini Lidar
* Author : JH KIM
* ======================================================================
* Program history
* ======================================================================
* Author        Date        Version         Modifications
* JH KIM        2023.02.10  v1.0            First Write
"""
import serial
import time


def Get_Dist_From_Lidar(ser):
    while True:
        count = ser.in_waiting
        if count > 8:
            recv = ser.read(9)
            ser.reset_input_buffer()
            if recv[0] == 0x59 and recv[1] == 0x59:
                distance = recv[2] + recv[3] * 256
                strength = recv[4] + recv[5] * 256
                ser.reset_input_buffer()
                return distance


ser = serial.Serial("/dev/ttyUSB0", 115200) # serial

# ser=serial.Serial("/dev/serial0", 115200)

def main():
    while True:
        try:
            dist = Get_Dist_From_Lidar(ser)
            print("distance = {}".format(dist)) # printout distance
            time.sleep(1)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
