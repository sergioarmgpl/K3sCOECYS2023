import RPi.GPIO as GPIO
import os
import time

color = os.environ['COLOR']

GPIO.setmode(GPIO.BCM)

ledPin1 = 18  #define led pin1
ledPin2 = 23  #define led pin2
GPIO.setup(ledPin1,GPIO.OUT)
GPIO.setup(ledPin2,GPIO.OUT)
GPIO.output(ledPin1,GPIO.LOW)
GPIO.output(ledPin2,GPIO.LOW)
try:
   while True:
      if color == "RED":
         GPIO.output(ledPin1,GPIO.HIGH)  #turn on led1
         GPIO.output(ledPin2,GPIO.LOW)  #turn off led2
         print({"color":"red"})
      elif color == "GREEN":
         GPIO.output(ledPin2,GPIO.HIGH)  #turn on led2
         GPIO.output(ledPin1,GPIO.LOW)  #turn off led1
         print({"color":"green"})
      time.sleep(1)
      GPIO.output(ledPin1,GPIO.LOW)  #turn on led2
      GPIO.output(ledPin2,GPIO.LOW)  #turn off led1
      print({"color":"off"})
      time.sleep(1)
except KeyboardInterrupt:
   GPIO.cleanup()
