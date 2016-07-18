import Adafruit_BBIO.GPIO as GPIO
import time
import sys
import grove_i2c_adc

# Reference voltage of ADC is 3.0v
ADC_REF = 3.0

# Vcc of the grove interface is normally 3.3v
GROVE_VCC = 3.3

adc = grove_i2c_adc.I2cAdc()

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
            # Read voltage values from Grove Sound Sensor
            sensor_voltage_value = read_sound_sensor_values()
            print "sensor_voltage_value = ", sensor_voltage_value
    except (KeyboardInterrupt,SystemExit):
            print "Exit"
            sys.exit(0)
    except:
            print "Exit"
            sys.exit(0)


