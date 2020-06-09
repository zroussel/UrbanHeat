# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:03:04 2020

@author: rouss
"""
import RPi.GPIO as GPIO
import time
import datetime
import csv

GPIO.setmode(GPIO.BCM)

#sleepTime = .1

#GPIO Pins
lightpin = 18
buttonpin1 = 21
buttonpin2 = 16

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(lightpin, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(18, GPIO.LOW)

starttime=time.time() 
f=open("pitest1.csv","w", newline="")

while True:
    if GPIO.input(21)== GPIO.LOW:
        GPIO.output(lightpin, GPIO.LOW)
        f.close()
        exit()
    if GPIO.input(buttonpin2) == GPIO.LOW:
        while GPIO.input(21) != GPIO.LOW:
            GPIO.output(lightpin, GPIO.HIGH)
            print(datetime.datetime.now().time())
            wc=csv.writer(f)
            current_time=time.strftime("%H:%M:%S", time.localtime())
            tspec=datetime.datetime.now().time()
            wc.writerow([current_time,tspec])
            time.sleep(1.00 -((time.time() - starttime) % 1.00))
