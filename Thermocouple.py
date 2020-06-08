# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:00:15 2020

@author: rouss
"""

import time
import datetime
import csv
"""
import board
import busio
import digitalio
import adafruit_max31855
#from tabulate import tabulate
#import csv

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)

max31855 = adafruit_max31855.MAX31855(spi, cs) 
TempC=max31855.temperature
TempF = TempC*(9/5) +32
print(TempC)
print(TempF)
"""

t=time.localtime()
current_time=time.strftime("%H:%M:%S", t)
print(current_time)

tspec=datetime.datetime.now().time()
print(datetime.datetime.now().time())



starttime=time.time() 

while True : 
 
    #print(TempC)
    #print(TempF)
    print(datetime.datetime.now().time())
    f=open("test1.csv","w", newline="")
    wc=csv.writer(f)

    wc.writerow([current_time,tspec])

    time.sleep(1.00 -((time.time() -starttime) %1.00))
    
#while  time.time() == 00 :
#    f.close()
"""
while True:
    TempC = max31855.temperature
    TempF = TempC*9/5 +32

T=(TempC,TempF)   
print(tabulate(time,T, headers=["Time", "TempC", "TempF"]))

with open ('TemperatureData.csv', mode='w') as csv_file:
    fieldnames = ['Time', 'TempC', 'TempF']
    writer=csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    startrepeat(writer.writerow({time,TempC,TempF}))"""