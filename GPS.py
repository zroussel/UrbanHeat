# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:16:54 2020

@author: rouss
"""


import time
import board
import busio
import adafruit_gps
#Need to add to list for installs, note whether theyre pip or conda 

import serial
uart=serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=10)

gps = adafruit_gps.GPS(uart,debug=False)

gps.send_command(n"PMTK220,1000")

gps.send_command(b"PMTK220,1000")

last_print=time.monotonic()

while True:
    gps.update()
    current=time.monotonic()
    if current - last_print>=1.0:
        last_print=current
        if not gps.has_fix:
            continue
        print("="*40)
        print("Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}".format(gps.timestamp_utc.tm_mon, gps.timestamp_utc.tm_mday, gps.timestamp_utc.tm_year))