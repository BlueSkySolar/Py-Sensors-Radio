import serial
import serial.tools.list_ports
import sys
import glob

#List all the port in windows.
print(list(serial.tools.list_ports.comports()))

###For variuos platforms check !!!! 
#For Windows 
if sys.platform.startswith('win'):
    ports = ['COM%s' % (i + 1) for i in range(256)]
#For linux 
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    # this excludes your current terminal "/dev/tty"
    ports = glob.glob('/dev/tty[A-Za-z]*')
#
elif sys.platform.startswith('darwin'):
    ports = glob.glob('/dev/tty.*')
else:
    raise EnvironmentError('Unsupported platform')
### Flow Control is a problem ###
#http://www.tldp.org/HOWTO/Text-Terminal-HOWTO-11.html
#DTR-Data Terminal Ready 
#DSR-Data Set Ready 
#RTS-Request To Send 
#CTS-Clear To Send 
#Xoff is used to stop the overflow
result = [] 
for port in ports:
	try:  
		ser = serial.Serial(port, 19200, timeout= 1,rtscts=1)
		#Print the name of the serial port 
		# check which port was really used
		print(ser.name) 
		#Opening a serial port 
		ser.open()

		#Writing on a serial port
		ser.write(b'hello')     

		#Reading on a serial port 
		x=ser.read()
		a= ser.read(10)
		line= ser.readline()
		  

		ser.close()
	except (OSError, serial.SerialException):
		pass 
