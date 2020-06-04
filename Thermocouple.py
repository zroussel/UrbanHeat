# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:00:15 2020

@author: rouss
"""

import time
import board
import busio
import digitalio
import adafruit_max31855
from tabulate import tabulate
import csv

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)

max31855 = adafruit_max31855.MAX31855(spi, cs) 
while True:
    TempC = max31855.temperature
    TempF = TempC*9/5 +32

T=(TempC,TempF)   
print(tabulate(T, headers=["TempC", "TempF"]))

with open ('TemperatureData.csv', mode='w') as csv_file:
    fieldnames = ['Time', 'TempC', 'TempF']
    writer=csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    startrepeat(writer.writerow({time,TempC,TempF}))