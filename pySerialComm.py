import serial

# open serial port
print(ser.name)
### Flow Control is a problem ###
#http://www.tldp.org/HOWTO/Text-Terminal-HOWTO-11.html
#DTR-Data Terminal Ready 
#DSR-Data Set Ready 
#RTS-Request To Send 
#CTS-Clear To Send 
#Xoff is used to stop the overflow 

ser = serial.Serial('COM3', 19200, timeout= 1,parity= NONE,rtscts=1) as ser: 
	# check which port was really used
	#Writing on a serial port 
	ser.write(b'hello')     
	#Reading on a serial port 
	x=ser.read()
	a= ser.read(10)
	line= ser.readline()
	         

# write a string
ser.close()
