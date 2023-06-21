from sensor.temp import get_temperature
from sensor.sonic import measure_distance
import time
from actor.led import control_led
import threading

temperature_value = None
distance_value = None
fire_alarm = False
LED_THRESHOLD = 233

def measure_temperature_and_distance():
    global temperature_value
    global distance_value
    global fire_alarm
    while True:
        temperature_value = get_temperature()
        print(f"Temperature: {temperature_value} °C")
        distance_value = measure_distance()
        print(f"Distance: {distance_value} mm")

        if temperature_value >= LED_THRESHOLD:
            control_led("blink")
            fire_alarm = True
        else:
            control_led("off")
            fire_alarm = False

        if not fire_alarm:
            control_led("off")
            if distance_value < 30:
                control_led("on")
            else:
                control_led("off")

        time.sleep(3)

if __name__ == "__main__":
    try:
        control_led("on")
        time.sleep(3)
        control_led("off")
        time.sleep(3)

        measure_thread = threading.Thread(target=measure_temperature_and_distance)
        measure_thread.start()

    except KeyboardInterrupt:
        pass
    finally:
        control_led("off")
        measure_thread.join()
