import serial
import serial.tools.list_ports
import sys
import glob

#List all the port in windows.
print(list(serial.tools.list_ports.comports()))

###For variuos platforms check !!!!### 
#For Windows 
if sys.platform.startswith('win'):
    ports = ['COM%s' % (i + 1) for i in range(256)]
#For linux 
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    # this excludes your current terminal "/dev/tty"
    ports = glob.glob('/dev/tty[A-Za-z]*')
#For Mac 
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
activeports=[]
result = [] 
for port in ports:
	
	try:  
		ser = serial.Serial(port, 19200, timeout= 1,rtscts=1)
		activeports.append(port)
		#Print the name of the serial port 
		# check which port was really used
		print(ser.name) 
	except (OSError, serial.SerialException):
		pass 
print activeports 
print len(activeports)
for port in activeports:
		
		portRead=activeports[0]
		portWrite=activeports[1]
		
		#Opening a serial port 
		#serRead.open()

		#Trying to open the serial port for writing.. 
		serWrite = serial.Serial(portWrite,19200, timeout = 1, rtscts = 1)
		#Writing on a serial port
		serWrite.write(b'hello')
		print "Hello"     
		serWrite.close()
		#Reading on a serial port
		serRead = serial.Serial(portRead, 19200, timeout= 1,rtscts=1)
		#Print the name of the serial port 
		# check which port was really used
		print(serRead.name)
		x=0
		a=1
		line = "blah" 
		x=serRead.read()
		a= serRead.read(10)
		line= serRead.readline()
		print x 
		print a 
		print line 

		serRead.close()
		
	
