#ALL SENSORS
"""
Created on Mon Jun  15 15:12:28 2020

@author: rouss
"""


import time
import board
import adafruit_gps
import serial
import RPi.GPIO as GPIO
import datetime
import csv
import digitalio
import busio
import adafruit_max31855
import adafruit_bme280
import math

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

#Thermocouple
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)
max31855 = adafruit_max31855.MAX31855(spi, cs)


#Humidity + Temp Sensor
b = 17.62
c = 243.12
 
# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)



starttime=time.time() 
f = open("pitest6-16-20-test1WALKING.csv","w")

RX = board.TX
TX = board.RX

uart=serial.Serial('/dev/serial0', baudrate =9600 , timeout = 10)

gps = adafruit_gps.GPS(uart, debug=False)

gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')

gps.send_command(b'PMTK220,1000')

last_print = time.monotonic()

while True:
    if GPIO.input(21)== GPIO.LOW:
        GPIO.output(lightpin, GPIO.LOW)
        f.close()
        exit()
    if GPIO.input(buttonpin2) == GPIO.LOW:
        while GPIO.input(21) != GPIO.LOW:
#            GPIO.output(lightpin, GPIO.HIGH)
            # Make sure to call gps.update() every loop iteration and at least twice
            # as fast as data comes from the GPS unit (usually every second).
            # This returns a bool that's true if it parsed new data (you can ignore it
            # though if you don't care and instead look at the has_fix property).
            gps.update()
            # Every second print out current location details if there's a fix.
            current = time.monotonic()
            if current - last_print >= 1.0:
                last_print = current
                if not gps.has_fix:
                    # Try again if we don't have a fix yet.
                    print('Waiting for fix...')
                    continue
                    # We have a fix! (gps.has_fix is true)
                    # Print out details about the fix like location, date, etc.
                print('=' * 40)  # Print a separator line.
                print(
                    'Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}'.format(
                gps.timestamp_utc.tm_mon,  # Grab parts of the time from the
                gps.timestamp_utc.tm_mday,  # struct_time object that holds
                gps.timestamp_utc.tm_year,  # the fix time.  Note you might
                gps.timestamp_utc.tm_hour,  # not get all data like year, day,
                gps.timestamp_utc.tm_min,  # month!
                gps.timestamp_utc.tm_sec,
                    )
                )
        
                LONG= gps.longitude
                LAT= gps.latitude
                wc=csv.writer(f)
                current_time=time.strftime("%H:%M:%S", time.localtime())
                tspec=datetime.datetime.now().time()
                TempC=max31855.temperature
                TempF = TempC*(9/5) +32
                #gamma = (b * bme280.temperature /(c + bme280.temperature)) + math.log(bme280.humidity / 100.0)
                #dewpoint = (c * gamma) / (b - gamma)
                bme280.sea_level_pressure = 1007.6
                Temp2=bme280.temperature
                Temp2F=Temp2*(9/5)+32
                H = bme280.humidity
                P = bme280.pressure
                A = bme280.altitude
                GPIO.output(lightpin, GPIO.HIGH)
                print(LAT,LONG,current_time, tspec,TempF,Temp2F)
                wc.writerow([current_time, tspec,LAT,LONG,TempC,TempF,Temp2,Temp2F,H,P,A])
                