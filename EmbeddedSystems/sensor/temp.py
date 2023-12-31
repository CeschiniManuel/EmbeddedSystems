import smbus2
import bme280
import random

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)


def get_temperature():
    data = bme280.sample(bus, address, calibration_params)
    temperature = data.temperature
    return temperature


def get_temperature_simulation():
    temperature = random.uniform(225.0, 240.0)
    return temperature


def get_humidity():
    data = bme280.sample(bus, address, calibration_params)
    humidity = data.humidity
    return humidity


