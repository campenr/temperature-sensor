#!/usr/bin/env python

"""
Simple python script capeable of monitoring a serial port.

"""

import serial


PORT = '/dev/ttyACM0'
BAUD = 9600
TIMEOUT = 2  # should be longer than the time we expect a message to take to be sent.
MESSAGE_WIDTH = 4  # bytes


def main():

    ser = serial.Serial(PORT, BAUD, timeout=TIMEOUT)
    ser.flushInput()
    
    while True:
        try:
            print(f'{ser.read(MESSAGE_WIDTH).decode()}°C')
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
