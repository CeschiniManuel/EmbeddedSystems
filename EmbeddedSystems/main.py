from sensor.temp import get_temperature
import time
from actor import led
import threading

# Shared variable to store the temperature value
temperature_value = None

# Function to continuously measure the temperature
def measure_temperature():
    global temperature_value
    while True:
        temperature_value = get_temperature()
        print(f"Temperature: {temperature_value} °C")
        time.sleep(5)

# Function to control the LED based on temperature
def led_control():
    global temperature_value
    while True:
        if temperature_value is not None:
            if temperature_value > 25:
                led.control_led("blink")
            else:
                led.control_led("off")
        time.sleep(1)

# Main code
if __name__ == "__main__":
    try:
        # Start the temperature measurement thread
        temperature_thread = threading.Thread(target=measure_temperature)
        temperature_thread.start()

        # Start the LED control thread
        led_thread = threading.Thread(target=led_control)
        led_thread.start()

    except KeyboardInterrupt:
        pass  # Allow Ctrl+C to exit the program gracefully
    finally:
        # Cleanup
        led.control_led("off")  # Turn off the LED before exiting
        temperature_thread.join()  # Wait for the temperature thread to finish
        led_thread.join()  # Wait for the LED control thread to finish
