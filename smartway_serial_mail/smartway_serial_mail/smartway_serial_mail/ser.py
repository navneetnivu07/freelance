 #!/usr/bin/env python

 #Here we use Raspberry Pi 2, and 
 #we connect a RS232/TTL 3-5,5V adapter to pins 4 (5V), 6 (GND) ,8 (TX),10 (RX) 
 #of Raspberry, obviously connect tx with rx and vice versa.

 # Goto https://www.google.com/settings/security/lesssecureapps
 # Access for less secure apps  : Turn On
          

import time
import serial
import smtplib


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("navaneethmalingan@gmail.com", "navaneeth@spatika16")

ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
 )
counter=0


while 1:
   x=ser.readline()
   print x
   msg = "Received Serial Data is : " + string(x)
   server.sendmail("navaneethmalingan@gmail.com", "shrihari.8788@gmail.com", msg)
   server.quit()
   sleep(10)




 
