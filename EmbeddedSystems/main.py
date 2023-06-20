from sensor.temp import get_temperature
from sensor.sonic import measure_distance
import time
from actor.led import control_led
import threading

temperature_value = None
distance_value = None
LED_THRESHOLD = 229 
led_full = False
fire_alarm = False


def measure_temperature():
    global temperature_value
    while True:
        temperature_value = get_temperature()
        print(f"Temperature: {temperature_value} °C")

        if temperature_value >= LED_THRESHOLD:
            control_led("blink")
        else:
            control_led("off")
        time.sleep(3)


def measure_distance_thread():
    global distance_value
    while True:
        distance_value = measure_distance()
        print(f"Distance: {distance_value} mm")

        if distance_value < 20:
            control_led("on")
        else:
            control_led("off")
        time.sleep(3)


if __name__ == "__main__":
    try:
        control_led("on")
        time.sleep(5)
        control_led("off")
        time.sleep(5)

        temperature_thread = threading.Thread(target=measure_temperature)
        temperature_thread.start()

        distance_thread = threading.Thread(target=measure_distance_thread)
        distance_thread.start()

    except KeyboardInterrupt:
        pass
    finally:
        control_led("off")
        temperature_thread.join()
        distance_thread.join()
