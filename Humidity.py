# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:22:14 2020

@author: rouss
"""

import time
 
import board
import busio
import adafruit_bme280
import math

b = 17.62
c = 243.12
gamma = (b * bme280.temperature /(c + bme280.temperature)) + math.log(bme280.humidity / 100.0)
dewpoint = (c * gamma) / (b - gamma)
 
# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
 

 
# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1007.6
 
while True:
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Altitude = %0.2f meters" % bme280.altitude)
    print(dewpoint)
    time.sleep(2)
    
    