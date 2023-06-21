import RPi.GPIO as GPIO
import time
import threading

LED_PIN = 25
LED_PIN2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

blink_active = False
led_state_changed = False
blink_thread = None


def control_led(state):
    global blink_active, led_state_changed, blink_thread
    if state == "on":
        if blink_active:
            blink_active = False
            led_state_changed = False
            if blink_thread is not None:
                blink_thread.join()
                blink_thread = None
        GPIO.output(LED_PIN, GPIO.HIGH)
        GPIO.output(LED_PIN2, GPIO.HIGH)
    elif state == "off":
        if blink_active:
            blink_active = False
            led_state_changed = True
            if blink_thread is not None:
                blink_thread.join()
                blink_thread = None
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.output(LED_PIN2, GPIO.LOW)
    elif state == "blink":
        if not blink_active:
            blink_active = True
            led_state_changed = False  # Reset led_state_changed
            blink_thread = threading.Thread(target=blink_led)
            blink_thread.start()
    else:
        print("Invalid state. Please specify 'on', 'off', or 'blink'.")


def blink_led():
    global blink_active, led_state_changed
    while blink_active and not led_state_changed:
        GPIO.output(LED_PIN, GPIO.HIGH)
        GPIO.output(LED_PIN2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.output(LED_PIN2, GPIO.HIGH)
        time.sleep(0.5)


def led_control_thread():
    while True:
        user_input = input(
            "Enter 'on' to turn the LED on, 'off' to turn it off, 'blink' to make it blink, or 'quit' to exit: ")

        if user_input == "quit":
            control_led("off")
            break
        control_led(user_input)

