import RPi.GPIO as R
from time import time,sleep
import paho.mqtt.subscribe as s

R.setwarnings(False)
R.setmode(R.BCM)
R.setup(24,R.OUT)

led = 24
try:
	while True:
		msg = s.simple(topic = "water_level",
				hostname="broker.shiftr.io",
				auth = {"username":'harharhar',"password":'harshit123'})
		print "Message is :"+msg.payload

		i = float(msg.payload)

		if (i <=5):
			R.output(led,False)
		elif(i>=100):
			R.output(led,True)
except Exception as ex:
	R.cleanup(ex)