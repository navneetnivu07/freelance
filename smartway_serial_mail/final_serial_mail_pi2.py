 #!/usr/bin/env python

 #Here we use Raspberry Pi 2, and 
 #we connect a RS232/TTL 3-5,5V adapter to pins 4 (5V), 6 (GND) ,8 (TX),10 (RX) 
 #of Raspberry, obviously connect tx with rx and vice versa.

 # Goto https://www.google.com/settings/security/lesssecureapps
 # Access for less secure apps  : Turn On
          

import time
import serial
import smtplib

ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
 )

while 1:
   	x=ser.readline()
   	print x
	#print "sad"
	if x is not None:
	   	server = smtplib.SMTP('smtp.gmail.com', 587)
	   	server.starttls()
	   	server.login("email", "password")
	   	msg = str(x)
	   	server.sendmail("sender mail", "receiver mail", msg)
   		server.quit()




 
