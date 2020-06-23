# UrbanHeat
Summer 2020 Barrett Scholarship - Temperature and Humidity Raspberry Pi 4 sensor

This repo contains the code used to power a Raspberry Pi4 with the following sensors:
    - Adafruit Ultimate GPS with USB - 66 channel w/ 10Hz updates
    - Adafruit Thermocouple Amplifier MAX31855 breakout board
    -*NOTE* also using Adafruit Thermocouple Amplifier MAX31856 as it is 
    compatible with different types of thermocouples and others may be more 
    accurate due to smaller ranges
    - Adafruit BME280 I2C or SPI Temperature Humidity Pressure Sensor

The following packages are dependencies and can be found at the following links:
1. Adafruit Circuit Python
    https://github.com/adafruit/circuitpython
    #NOT  SURE IF 1. is ACTUALLY NEEDED, MUST TEST WHEN I GET NEW PI'S
2. Adafruit Bus Device
    https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
3. Adafruit CircuitPython GPS
    https://github.com/adafruit/Adafruit_CircuitPython_GPS
4. Adafruit CircuitPython MAX31855 -    INSTALL THE APPROPRIATE PACKAGE 4
    https://github.com/adafruit/Adafruit_CircuitPython_MAX31855
4. Adafruit CircuitPython MAX31856 -    INSTALL THE APPROPRIATE PACKAGE 4
    https://github.com/adafruit/Adafruit_CircuitPython_MAX31856
5. *OPTIONAL* Adafruit CircuitPython BME280
    https://github.com/adafruit/Adafruit_CircuitPython_BME280

* ALL DEPENDENCIES ARE INSTALLED USING PIP *

Steps to getting you sensors set up.
1. Follow steps 1-3 to set up your raspberryPi with an operating system
    https://magpi.raspberrypi.org/articles/set-up-raspberry-pi-4
2. Follow steps here based on operating system to connect to your raspberryPi
    (You will need an ethernet chord to plug into your router)
    https://www.dexterindustries.com/howto/connecting-raspberry-pi-without-monitor-beginners/
3. Use these instructions to check your python version *NOTE* this software 
    must use atleast python3.X for CircuitPython code to work
4. Install PIP in terminal:
    $ install python3-pip 
5. Download dependencies from above links
    *NOTE* two dependencies are labeled 4, make sure you install the package 
        of the sensor that you used
6. Install all of the packages in terminal:
    $ sudo pip3 install adafruit-blinka
    $ sudo pip3 install adafruit-circuitpython-busdevice 
    $ sudo pip3 install adafruit-circuitpython-gps 
    $ sudo pip3 install adafruit-circuitpython-MAX3185X
        X depends on version
    

