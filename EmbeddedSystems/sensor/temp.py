import time
import board
import adafruit_bmp280
import random


# Create BMP280 sensor object
i2c = board.I2C()  # Uses the default SDA and SCL pins
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)


def get_temperature():
    temperature = bmp280.temperature
    return temperature


if __name__ == "__main__":
    temperature = get_temperature()
    print(f"Temperature: {temperature} °C")

def get_temperature_simulation():
    temperature = random.uniform(225.0, 240.0)
    return temperature
