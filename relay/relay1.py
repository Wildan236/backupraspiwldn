import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

for i in range(10):
  GPIO.output(17,GPIO.HIGH)
  GPIO.output(23,GPIO.HIGH)
  print ("LED ON")
  sleep(0.05)
  
  GPIO.output(17,GPIO.LOW)
  GPIO.output(23,GPIO.LOW)
  print ("LED OFF")
  sleep(0.05)

GPIO.cleanup()