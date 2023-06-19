from sensor.temp import get_temperature
import time
from actor.led import control_led
import threading

temperature_value = None
LED_THRESHOLD = 233 # this is the value papaer is considert to burn

def measure_temperature():
    global temperature_value
    while True:
        temperature_value = get_temperature()
        print(f"Temperature: {temperature_value} °C")

        if temperature_value >= LED_THRESHOLD:
            control_led("blink")
        else:
            control_led("off")
        time.sleep(5)


if __name__ == "__main__":
    try:

        #shows programm starts
        control_led("on")
        time.sleep(5)
        control_led("off")
        time.sleep(5)

        #threads:

        temperature_thread = threading.Thread(target=measure_temperature)
        temperature_thread.start()

        led_control_thread = threading.Thread(target=led_control_thread)
        led_control_thread.start()

    except KeyboardInterrupt:
        pass
    finally:
        control_led("off")
        temperature_thread.join()
        led_control_thread.join()
