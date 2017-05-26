from picamera import PiCamera
from time import sleep
import subprocess

#camera = PiCamera()

subprocess.call(['bash', 'a.sh'])

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
perviousState = 2
while True:
       i=GPIO.input(11)
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
             GPIO.output(3, 0)  #Turn OFF LED
             #camera.stop_preview()
             if perviousState != i:
                        subprocess.call(['bash','stop.sh'])
                        previousState = i
             time.sleep(2)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             GPIO.output(3, 1);  #Turn ON LED
             # camera.start_preview()
             if previousState != i:
                        subprocess.call(['bash', 'start.sh'])
                        previousState = i
             time.sleep(2)
