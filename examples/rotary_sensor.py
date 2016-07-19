import Adafruit_BBIO.GPIO as GPIO
import grove_I2C_ADC
import time
import sys

GPIO.setup("P9_22", GPIO.OUT)
potentiometer = 0
full_angle=300

# Reference voltage of ADC is 3.0v
ADC_REF = 3.0

# Vcc of the grove interface is normally 3.3v
GROVE_VCC = 3.3

adc = grove_I2C_ADC.I2cAdc()

def read_rotary_sensor_values():

    "Read voltage values from Grove Rotary Sensor"
    total_value = 0
    for index in range(5):
        sensor_value = adc.read_adc()

    voltage_value = float(sensor_value / 128 * ADC_REF)
    return voltage_value

# Function: If the rotary angle sensor senses rotation that is up to the threshold you set in the code, the LED is on for 0.5s.
# Hardware: Grove - I2C ADC, Grove - Rotary Angle Sensor, Grove - LED(You can also replace Grove - LED with Grove - Buzzer.)
# Note: Use P9_22(UART2_RXD) as GPIO.
# Connect the Grove LED to UART Grove port of Beaglebone Green.
# Connect the Grove - I2C ADC to I2C Grove port of Beaglebone Green, and then connect the Grove - Rotary Angle Sensor to Grove - I2C ADC.

if __name__== '__main__':
    try:
        while True:
            # Read voltage values from Grove Sensor
            sensor_voltage_value = read_rotary_sensor_values()
            degrees = int(sensor_voltage_value *  GROVE_VCC * 2)
            brightness = int(degrees / full_angle * 255)
            print "degrees", degrees
            GPIO.output("P9_22",brightness)
            time.sleep(0.01)
    except SystemExit as e:
        GPIO.output("P9_22", GPIO.LOW)
        print "Exit"
        sys.exit(0)
    except:
        GPIO.output("P9_22", GPIO.LOW)
        print "Exit"
        sys.exit(0)
