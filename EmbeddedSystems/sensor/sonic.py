import time
import board
import busio
import adafruit_vl6180x


i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vl6180x.VL6180X(i2c)

def measure_distance():

    distance = sensor.range

    return distance

# Main program loop
if __name__ == "__main__":
    try:
        while True:
            distance = measure_distance()

            print("Distance: {} mm".format(distance))

            time.sleep(1)

    except KeyboardInterrupt:
        print("Exiting...")
