# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 16:11:17 2020

@author: rouss
"""


#Very Specific list of commands for using a new RPi for this process

1. Go to Preferences>Raspberry Pi Configuration> Interfaces:
    Enable: SSH, VNC, SPI, I2C, Serial Port
    Disable: Camera, Serial Console, 1-Wire, Remote GPI
    
2. In terminal: 
   $ sudo nano /boot/config.txt
    uncomment line "hdmi_force_hotplug=1"
    save and exit 
    
3. In terminal: 
    $ sudo apt install python3-pip
    $ sudo pip3 install adafruit-blinka
    $ sudo pip3 install adafruit-circuitpython-busdevice 
    $ sudo pip3 install adafruit-circuitpython-gps 
    $ sudo pip3 install adafruit-circuitpython-MAX3185X