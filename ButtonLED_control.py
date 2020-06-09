import RPi.GPIO as GPIO
#from time import sleep
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

while True:
    if GPIO.input(21)== GPIO.LOW:
        GPIO.output(lightpin, GPIO.LOW)
    if GPIO.input(buttonpin2) == GPIO.LOW:
        GPIO.output(lightpin, GPIO.HIGH)

#while True:
 #   GPIO.output(lightpin, GPIO.input(buttonpin))
  #  sleep(.1)
    
    
