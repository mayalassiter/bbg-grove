import Adafruit_BBIO.GPIO as GPIO
import time
import sys
import grove_I2C_ADC

# Reference voltage of ADC is 3.0v
ADC_REF = 3.0

# Vcc of the grove interface is normally 3.3v
GROVE_VCC = 3.3

GPIO.setup("P9_22", GPIO.OUT)
adc = grove_I2C_ADC.I2cAdc()

def read_sound_sensor_values():
    "Read voltage values from Grove Sound Sensor"
    total_value = 0
    for index in range(5):
        sensor_value = adc.read_adc()
        total_value += sensor_value
        time.sleep(0.01)
    average_value = float(total_value / 5)

    voltage_value = average_value / 4095 * ADC_REF * 2
    return voltage_value

if __name__== '__main__':
    try:
        while True:
            GPIO.output("P9_22", GPIO.LOW)
            # Read voltage values from Grove Sound Sensor
            sensor_voltage_value = read_sound_sensor_values()
            #print "sensor_voltage_value = ", sensor_voltage_value
            if sensor_voltage_value > 0.04:
               print "sound detected"
               GPIO.output("P9_22", GPIO.HIGH)
               time.sleep(0.3)
            else:
               GPIO.output("P9_22", GPIO.LOW)
               time.sleep(0.1)
    except (KeyboardInterrupt,SystemExit):
            print "Exit"
            sys.exit(0)
    except:
            print "Exit"
            sys.exit(0)


