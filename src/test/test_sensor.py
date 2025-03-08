'''
@author Huy Le (hl9082)
This module contains a test function for the sensor module.
Functions:
    test_read_sensor_value(): Tests the read_sensor_value function to ensure it returns a value within the valid range.

'''

from sensor import read_sensor_value

def test_read_sensor_value():
    """
    Test the read_sensor_value function to ensure it returns a valid range.
    """
    value = read_sensor_value()
    assert 0 <= value <= 1023, "Sensor value out of range"
    print(f"Test Sensor Value: {value}")

if __name__ == "__main__":
    test_read_sensor_value()