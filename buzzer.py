import RPi.GPIO as GPIO
import time
buzzPin = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzPin, GPIO.OUT)
try:
  while True:
    time.sleep(.5)
    GPIO.output(buzzPin, GPIO.LOW)
    time.sleep(.5)
    GPIO.output(buzzPin, GPIO.HIGH)
except:
  GPIO.cleanup()