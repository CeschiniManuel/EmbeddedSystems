import time
import board
import busio
import adafruit_vl6180x

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vl6180x.VL6180X(i2c)

def measure_distance():
    # Read distance from the sensor
    distance = sensor.range

    return distance

# Main program loop
if __name__ == "__main__":
    try:
        while True:
            # Measure distance from the sensor
            distance = measure_distance()

            # Print the distance
            print("Distance: {} mm".format(distance))

            # Delay between readings
            time.sleep(1)

    except KeyboardInterrupt:
        # Exit program on keyboard interrupt (Ctrl+C)
        print("Exiting...")
