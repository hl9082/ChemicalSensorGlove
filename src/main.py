'''
@author Huy Le (hl9082)
This script is designed to read sensor values from a chemical sensor and provide feedback using an LED.
The LED will turn on if a hazardous material is detected, and turn off otherwise.
Functions:
    setup(): Initializes the LED and sets up the system.
    loop(): Continuously reads sensor values and determines the type of material detected based on predefined thresholds.
Constants:
    LED_PIN (int): GPIO pin number for the LED.
    ORGANIC_THRESHOLD (int): Threshold value for detecting organic materials.
    HAZARDOUS_THRESHOLD (int): Threshold value for detecting hazardous materials.
Usage:
    Run the script to start the system. The system will continuously read sensor values and provide feedback via the LED.
    Press Ctrl+C to exit the program.
'''

import time

from gpiozero import LED
from sensor import read_sensor_value

# Pin definitions
LED_PIN = 17  # GPIO pin for LED

# Threshold values for detecting materials
ORGANIC_THRESHOLD = 300
HAZARDOUS_THRESHOLD = 600

def setup():
    """
    Set up the LED and initialize the system.
    """
    global led
    led = LED(LED_PIN)  # Initialize LED
    led.off()  # Ensure LED is off initially
    print("System initialized.")

def loop():
    """
    Main loop to continuously read sensor values and provide feedback.
    """
    while True:
        # Read the current sensor value
        sensor_value = read_sensor_value()
        print(f"Sensor Value: {sensor_value}")

        # Determine the type of material detected based on thresholds
        if sensor_value > HAZARDOUS_THRESHOLD:
            led.on()  # Turn on LED for hazardous material
            print("Hazardous material detected!")
        elif sensor_value > ORGANIC_THRESHOLD:
            led.off()  # Turn off LED for organic material
            print("Organic material detected.")
        else:
            led.off()  # Ensure LED is off for no detection
            print("No significant material detected.")

        time.sleep(1)  # Delay for stability

if __name__ == "__main__":
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        print("Exiting program.")