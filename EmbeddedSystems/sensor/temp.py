import random
import time

# Function to generate simulated temperature values
def get_temperature():
    temperature = random.uniform(20.0, 30.0)
    return temperature

# Main code
if __name__ == "__main__":
    try:
        while True:
            # Get the temperature
            temperature = get_temperature()

            # Output the temperature
            print(f"Temperature: {temperature} °C")

            # Wait for a second
            time.sleep(5)

    except KeyboardInterrupt:
        pass  # Allow Ctrl+C to exit the program gracefully
