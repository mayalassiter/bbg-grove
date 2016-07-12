mport Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_22", GPIO.OUT)
 
while True:
    try:
	GPIO.output("P9_22", GPIO.HIGH)
    	time.sleep(0.5)
    	GPIO.output("P9_22", GPIO.LOW)
    	time.sleep(0.5)
    except IOError:
    	GPIO.output("P9_22", GPIO.LOW)
	break
