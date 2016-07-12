import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_22", GPIO.IN)
count=0;

if __name__== '__main__':
 while True:
   if GPIO.input("P9_22"):
      print "Button pressed"
      count=0
      time.sleep(0.5)
   else:
      count=count+1
      print count
      time.sleep(0.5)
