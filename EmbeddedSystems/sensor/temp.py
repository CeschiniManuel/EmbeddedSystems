import RPi.GPIO as GPIO
import random

import time

# GPIO pin number
PIN_NUMBER = 23

def get_temperature():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_NUMBER, GPIO.IN)

    # Read the raw value from GPIO
    raw_value = GPIO.input(PIN_NUMBER)

    # Convert raw value to voltage
    voltage = raw_value * (3.3 / 1023.0)

    print(voltage)


    # Convert voltage to temperature in degrees Celsius
    temperature = (voltage - 0.5) * 100

    return temperature


def get_temperature_simulation():
    temperature = random.uniform(225.0,  240.0)
    return temperature


