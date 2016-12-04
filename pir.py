import Rpi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
pir=4 
GPIO.setup(pir, GPIO.IN)
While True:
    if GPI0.input(pir):
        print "no motion detected"
    else
        print"motion detected"
        time sleep(5)
  
