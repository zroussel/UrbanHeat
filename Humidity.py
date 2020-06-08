# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:22:14 2020

@author: rouss
"""

import time
import datetime
import board
import busio
import adafruit_bme280
import math
import csv

b = 17.62
c = 243.12
 
# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

gamma = (b * bme280.temperature /(c + bme280.temperature)) + math.log(bme280.humidity / 100.0)
dewpoint = (c * gamma) / (b - gamma)

 
# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1007.6
t=time.time()
tspec=datetime.datetime.now().time()
Temp=bme280.temperature
H = bme280.humidity
P = bme280.pressure
A = bme280.altitude
print(t,tspec,Temp, H, P, A)

f=open("test1.csv","w",newline="")
wc=csv.writer(f)

wc.writerow([t,tspec,Temp,H,P,A])

f.close()
"""
while True:
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Altitude = %0.2f meters" % bme280.altitude)
    print(dewpoint)
    time.sleep(2)
    
"""