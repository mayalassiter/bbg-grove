import Adafruit_BBIO.GPIO as GPIO
import time
import sys
import grove_i2c_adc

GPIO.setup("P9_22", GPIO.OUT)

# Reference voltage of ADC is 3.0v
ADC_REF = 3.0

# Vcc of the grove interface is normally 3.3v
GROVE_VCC = 3.3

adc = grove_i2c_adc.I2cAdc()

def read_light_sensor_values():
    "Read voltage values from Grove Light Sensor"
    total_value = 0
    for index in range(5):
        sensor_value = adc.read_adc()
        total_value += sensor_value
        time.sleep(0.01)
    average_value = float(total_value / 5)

    voltage_value = average_value / 4095 * ADC_REF * 2
    return voltage_value

# Function: If the light sensor senses light that is up to the threshold you set in the code, the LED is on for 0.5s.
# Hardware: Grove - I2C ADC, Grove - Light Sensor, Grove - LED(You can also replace Grove - LED with Grove - Buzzer.)
# Note: Use P9_22(UART2_RXD) as GPIO.
# Connect the Grove LED to UART Grove port of Beaglebone Green.
# Connect the Grove - I2C ADC to I2C Grove port of Beaglebone Green, and then connect the Grove - Light Sensor to Grove - I2C ADC.

if __name__== '__main__':
    try:
        while True:
            # Read voltage values from Grove Light Sensor
            sensor_voltage_value = read_light_sensor_values()
            print "sensor_voltage_value = ", sensor_voltage_value
            if sensor_voltage_value > 1.5:
             GPIO.output("P9_22", GPIO.HIGH)
             time.sleep(0.5)
             GPIO.output("P9_22", GPIO.LOW)
            else:
             GPIO.output("P9_22", GPIO.LOW)
    except (KeyboardInterrupt,SystemExit):
         GPIO.output("P9_22", GPIO.LOW)
         print "Exit"
         sys.exit(0)
    except:
         GPIO.output("P9_22", GPIO.LOW)
         print "Exit"
         sys.exit(0)
