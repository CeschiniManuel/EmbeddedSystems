import RPi.GPIO as GPIO
import time

LED_PIN = 25
LED_PIN2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

blink_active = False
led_state_changed = False


def control_led(state):
    global blink_active, led_state_changed
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.output(LED_PIN2, GPIO.LOW)

    if state == "on":
        if blink_active:
            blink_active = False
            led_state_changed = True
        GPIO.output(LED_PIN, GPIO.HIGH)
        GPIO.output(LED_PIN2, GPIO.HIGH)
    elif state == "off":
        if blink_active:
            blink_active = False
            led_state_changed = True
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.output(LED_PIN2, GPIO.LOW)
    elif state == "blink":
        if not blink_active:
            blink_active = True
            led_state_changed = True
            blink_led()
    else:
        print("Invalid state. Please specify 'on', 'off', or 'blink'.")


# Function to blink the LEDs
def blink_led():
    global led_state_changed
    while blink_active:
        GPIO.output(LED_PIN, GPIO.HIGH)
        GPIO.output(LED_PIN2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.output(LED_PIN2, GPIO.HIGH)
        time.sleep(0.5)

        # Check if the LED state has changed
        if led_state_changed:
            led_state_changed = False
            break

