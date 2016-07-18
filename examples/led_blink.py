import Adafruit_BBIO.GPIO as GPIO
import time
import sys

def exitfunc():
    GPIO.output("P9_22", GPIO.LOW)
sys.exitfunc = exitfunc

GPIO.setup("P9_22", GPIO.OUT)

try:
   while True:
       GPIO.output("P9_22", GPIO.HIGH)
       time.sleep(0.1)
       GPIO.output("P9_22", GPIO.LOW)
       time.sleep(0.1)
except (KeyboardInterrupt,SystemExit):
     print "Exit"
     sys.exit(1)
except:
     print "Exit"
     sys.exit(1)
