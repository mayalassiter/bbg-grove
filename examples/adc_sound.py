import time
#from logo import print_seeedstudio
import grove_i2c_adc
import Adafruit_BBIO.GPIO as GPIO

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
#        print "sensor_value = ", sensor_value
        total_value += sensor_value
        time.sleep(0.01)
#    print "total_value = ", total_value
 average_value = float(total_value / 5)

    voltage_value = average_value / 4095 * ADC_REF * 2
    return voltage_value

# Function: If the sound sensor senses a sound that is up to the threshold you set in the code, the LED is on for 1s.
# Hardware: Grove - I2C ADC, Grove - Sound Sensor, Grove - LED(You can also replace Grove - LED with Grove - Buzzer.)
# Note: Use P9_22(UART2_RXD) as GPIO.
# Connect the Grove LED to UART Grove port of Beaglebone Green.
# Connect the Grove - I2C ADC to I2C Grove port of Beaglebone Green, and then connect the Grove - Sound Sensor to Grove - I2C ADC.

if __name__== '__main__':
    #print_seeedstudio()
    while True:
        try:
            # Read voltage values from Grove Sound Sensor
            sensor_voltage_value = read_sound_sensor_values()
            print "sensor_voltage_value = ", sensor_voltage_value
#            time.sleep(2)
        except IOError:
            print "Error"


