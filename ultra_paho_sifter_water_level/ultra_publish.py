import RPi.GPIO as R
import requests
from time import time,sleep
import paho.mqtt.publish as p

R.setwarnings(False)
R.setmode(R.BCM)
R.setup(23,R.OUT)
R.setup(18,R.IN)

Triger_pin = 23
Echo_pin = 18

try:
	while(True):
		
		R.output(Triger_pin,True)
		sleep(0.001)
		R.output(Triger_pin,False)

		start_time = time()
		end_time = time()

		while(R.input(Echo_pin) == 0):
			start_time = time()


		while(R.input(Echo_pin) == 1):
			end_time = time()

	
		duration = end_time - start_time
		distance = (duration * 34300)/2

		i= distance

		p.single(topic = "water_level",                                   
			payload= str(i),
			hostname="broker.shiftr.io",
			auth={"username":'harharhar',"password":'harshit123'})
		print "distance is : ", + i
		sleep(1)
except Exception as ex:
	R.cleanup(ex)