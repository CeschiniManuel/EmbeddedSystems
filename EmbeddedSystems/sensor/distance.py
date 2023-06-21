import time
import board
import busio
import adafruit_vl6180x

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vl6180x.VL6180X(i2c)


def measure_distance():
    distance = sensor.range
    return distance


def check_distance_threshold(thres):
    distance = measure_distance()
    if distance < thres:
        print("Below threshold")
    else:
        print("Above threshold")


def continuous_measurement(inter):
    while True:
        distance = measure_distance()
        print("Distance: ", distance)
        delay(inter)


def delay(seconds):
    time.sleep(seconds)
