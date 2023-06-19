import RPi.GPIO as GPIO
import time
import random

# GPIO-Pins für den Ultraschallsensor festlegen
TRIGGER_PIN = 23
ECHO_PIN = 24
EMULATED_MODE = True  # True, um emulierte Werte zu verwenden, False, um den Ultraschallsensor zu verwenden

def setup():
    # GPIO-Modus (BCM) festlegen
    GPIO.setmode(GPIO.BCM)

    # Ultraschall-Trigger-Pin als Ausgang und Echo-Pin als Eingang festlegen
    GPIO.setup(TRIGGER_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)

def get_distance():
    if EMULATED_MODE:
        # Emulierte Werte generieren, wenn der emulierte Modus aktiviert ist
        distance = random.uniform(0, 100)
    else:
        # Ultraschall-Abstandsmessung ausführen, wenn der emulierte Modus deaktiviert ist

        # Trigger-Pin kurzzeitig auf High setzen
        GPIO.output(TRIGGER_PIN, True)
        time.sleep(0.00001)
        GPIO.output(TRIGGER_PIN, False)

        # Zeitpunkt des Signalanstiegs und -abfalls am Echo-Pin erfassen
        pulse_start = time.time()
        pulse_end = time.time()

        while GPIO.input(ECHO_PIN) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO_PIN) == 1:
            pulse_end = time.time()

        # Zeitdifferenz zwischen Signalanstieg und -abfall berechnen
        pulse_duration = pulse_end - pulse_start

        # Schallgeschwindigkeit (in cm/s) teilen, um die Entfernung in Zentimetern zu berechnen
        distance = pulse_duration * 34300 / 2

        # Ergebnis auf zwei Dezimalstellen runden
        distance = round(distance, 2)

    return distance

def cleanup():
    # Aufräumen und GPIO-Pins zurücksetzen
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        setup()

        while True:
            distance = get_distance()
            print(f"Entfernung: {distance} cm")
            time.sleep(1)

    except KeyboardInterrupt:
        cleanup()
