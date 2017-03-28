import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","agri" )

# prepare a cursor object using cursor() method
cursor = db.cursor()# Open database connection

moist = 17 # GPIO17 : 11 Pin on Board (Moisture Sensor)
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(moist, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(24, GPIO.OUT)    # set GPIO24 as an output : 18th Pin on board  


moistStatus = "Dry"
motorStatus = "OFF"

#GPIO.setup(moist, GPIO.IN)
while True:
	
	
	humidity, temperature = Adafruit_DHT.read_retry(11, 4) # GPIO4 : 7th Pin on Board (DHT Temp/Hum Sensor)

	print 'Temp: {0:0.1f} C  Humidity: {1:0.1f}%'.format(temperature, humidity)
		
	if GPIO.input(17):
    		print("Dry")
		moistStatus = "Dry"
		GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True 
		motorStatus = "ON"  
		print("Motor is ON") 

	else:
    		print("Wet")
		moistStatus = "Wet"
		
		if temperature >= 38 and humidity <= 40:
			GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True
			motorStatus = "ON" 
			print("Motor is ON") 
		else:
			GPIO.output(24, 0)         # set GPIO24 to 1/GPIO.HIGH/True
			motorStatus = "OFF" 
			print("Motor is OFF")
    	
	# Prepare SQL query to INSERT a record into the database.
	sql = "INSERT INTO data(temp,hum,moist,motor) VALUES (%s, %s, %s, %s)",(float(format(temperature)), float(format(humidity)), str(moistStatus), str(motorStatus)) 
	
   	# Execute the SQL command
   	cursor.execute(*sql)
   	# Commit your changes in the database
   	db.commit()
	
	time.sleep(5)
