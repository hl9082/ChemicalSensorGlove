'''
@author Huy Le (hl9082)
This module provides functionality to read analog sensor values using the MCP3008 ADC.
Functions:
    read_sensor_value(channel=0):

'''

import busio
import digitalio
import board
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn

def read_sensor_value(channel=0):
    """
    Read the analog sensor value from the specified channel using the MCP3008 ADC.

    Args:
        channel (int): The ADC channel to read from (0-7).

    Returns:
        int: The sensor value (0-1023).
    """
    # Create the SPI bus
    spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)

    # Create the CS (chip select)
    cs = digitalio.DigitalInOut(board.D5)  # Use GPIO pin 5 for CS

    # Create the MCP3008 object
    mcp = MCP3008(spi, cs)

    # Create an analog input channel on the specified channel
    chan = AnalogIn(mcp, channel)

    # Return the sensor value
    return chan.value