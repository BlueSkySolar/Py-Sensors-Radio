# Py-Sensors-Radio
A proof-of-concept demonstration of how USB-based serial devices might be integrated into the Blue Sky Telemetry Interface (BTI). Data must be read, parsed, displayed and saved in a reliable, fault-tolerant way. If all goes well, most of this code will be integrated into the BTI.

### Setup
In order to differentiate between devices in a scalable way, users will need to go through a setup step when the BTI starts up where it will prompt the user to plug in specific devices one by one. Since this can get tedious, an option to use the same ports as the last session may be implemented.
