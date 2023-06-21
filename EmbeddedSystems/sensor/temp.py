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


actual_temperature = get_temperature()
print("Actual Temperature:", actual_temperature)

simulated_temperature = get_temperature_simulation()
print("Simulated Temperature:", simulated_temperature)
