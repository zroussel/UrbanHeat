import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

sleepTime = .1

#GPIO Pins
lightpin = 18
buttonpin = 21

GPIO.setup(lightpin, GPIO.OUT)
GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.output(lightpin, GPIO.input(buttonpin))
    #sleep(.1)