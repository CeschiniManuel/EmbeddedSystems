import RPi.GPIO as GPIO
import time

# VL6180X sensor constants
VL6180X_DEFAULT_ADDR = 0x29
REG_IDENTIFICATION_MODEL_ID = 0x000
REG_SYSTEM_INTERRUPT_CONFIG = 0x014
REG_SYSRANGE_START = 0x018
REG_RESULT_RANGE_VAL = 0x062
SYSRANGE_MODE_START_STOP = 0x01

# Set GPIO pins
SDA_PIN = 2
SCL_PIN = 3

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SDA_PIN, GPIO.OUT)
GPIO.setup(SCL_PIN, GPIO.OUT)

# Function to start I2C communication
def i2c_start():
    GPIO.output(SDA_PIN, GPIO.HIGH)
    GPIO.output(SCL_PIN, GPIO.HIGH)
    GPIO.output(SDA_PIN, GPIO.LOW)
    GPIO.output(SCL_PIN, GPIO.LOW)

# Function to stop I2C communication
def i2c_stop():
    GPIO.output(SDA_PIN, GPIO.LOW)
    GPIO.output(SCL_PIN, GPIO.HIGH)
    GPIO.output(SDA_PIN, GPIO.HIGH)

# Function to send a byte over I2C
def i2c_send_byte(byte):
    for _ in range(8):
        GPIO.output(SDA_PIN, byte & 0x80)
        GPIO.output(SCL_PIN, GPIO.HIGH)
        GPIO.output(SCL_PIN, GPIO.LOW)
        byte <<= 1

    # Receive ACK bit
    GPIO.setup(SDA_PIN, GPIO.IN)
    GPIO.output(SCL_PIN, GPIO.HIGH)
    ack = GPIO.input(SDA_PIN)
    GPIO.output(SCL_PIN, GPIO.LOW)
    GPIO.setup(SDA_PIN, GPIO.OUT)

    return ack

# Function to read a byte over I2C
def i2c_read_byte():
    byte = 0x00
    GPIO.setup(SDA_PIN, GPIO.IN)
    for _ in range(8):
        GPIO.output(SCL_PIN, GPIO.HIGH)
        byte = (byte << 1) | GPIO.input(SDA_PIN)
        GPIO.output(SCL_PIN, GPIO.LOW)
    GPIO.setup(SDA_PIN, GPIO.OUT)
    return byte

# Function to write a byte to a register on the VL6180X sensor
def write_register(register, value):
    i2c_start()
    i2c_send_byte((VL6180X_DEFAULT_ADDR << 1) | 0)
    i2c_send_byte(register >> 8)
    i2c_send_byte(register & 0xFF)
    i2c_send_byte(value)
    i2c_stop()

# Function to read a word from a register on the VL6180X sensor
def read_register(register):
    i2c_start()
    i2c_send_byte((VL6180X_DEFAULT_ADDR << 1) | 0)
    i2c_send_byte(register >> 8)
    i2c_send_byte(register & 0xFF)
    i2c_start()
    i2c_send_byte((VL6180X_DEFAULT_ADDR << 1) | 1)
    value = (i2c_read_byte() << 8) | i2c_read_byte()
    i2c_stop()
    return value

# Configure VL6180X sensor
write_register(REG_SYSTEM_INTERRUPT_CONFIG, 0x00)
write_register(REG_SYSRANGE_START, SYSRANGE_MODE_START_STOP)

# Function to read distance
def read_distance():
    # Start a single measurement
    write_register(REG_SYSRANGE_START, SYSRANGE_MODE_START_STOP)

    # Wait for measurement to complete
    time.sleep(0.1)

    # Read the measured distance value
    range_val = read_register(REG_RESULT_RANGE_VAL)

    # Calculate distance in millimeters
    distance = (range_val / 10)

    return distance

# Main program loop
try:
    while True:
        # Read distance from the sensor
        distance = read_distance()

        # Print the distance
        print("Distance: {} mm".format(distance))

        # Delay between readings
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt (Ctrl+C)
    GPIO.cleanup()
