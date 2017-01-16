"""
parse_serial.py

This module will contain helper functions and classes for:
- Connecting to serial devices
- Parsing sensor data

Last updated: 2017-01-15
"""

import serial
from serial.tools import list_ports
import time
import json


class serial_device:
    """
    A wrapper class for serial devices for the BTI.

    Parameters:
        name (string) - an identifier for the device (e.g. "GPS")
        ser (Serial) - a pySerial object connected to a serial port
        parser (function(Serial, string) -> dictionary) - a function called
            with ser which reads and parses incoming text

    Other Fields:
        packet_fragment (string) - the last incomplete data packet read from
            ser; this happens because readline() is called with timeout=0 in
            order to not block the thread
    """

    def __init__(self, name, ser, parser):
        self.name = name
        self.ser = ser
        self.parser = parser
        self.packet_fragment = ""

    # Wrapper function for convenience
    def parse(self):
        self.parser(self.ser, self.packet_fragment)

## Parser functions

def parse_pyra(ser):
    return({})

def parse_gps(ser):
    return({})


## Testing

if __name__ == "__main__":

    # An example of loading device ports from a list of preferences
    # Format: {name: [port, parser]}

    # Startup

    ports = {"pyra": ["COM3", "parse_pyra"]}
    devices = []
    data = {}

    for port in ports.keys():
        try:
            # Long timeout to check if device is working
            ser = serial.Serial(ports[port][0], timeout = 5)
            # Get function from function name
            parser = locals()[ports[port][1]]
            device = serial_device(port, ser, parser)
            if(device.parse() != {}): # Valid result
                device.ser.timeout = 0 # Set actual timeout
                devices.append(device)
        except:
            print("Device", port, "is not connected to port", ports[port][0])

    print("Devices:", devices)

    # Running

    for i in range(10): # While BTI is running
        for device in devices:
            new_data = device.parse()
            data.update(new_data)
        # Could display and save data here
        print(data)
        time.sleep(0.5)

    # Closing

    for device in devices:
        # Format preferences - could write to storage here
        print({device.name: [device.ser.port, device.parser.__name__]})
        device.ser.close()
