# import the library that allows us to logically access the GPIO pins
# refer to the library as G, it is like an alias
import RPi.GPIO as R

#import the requests library
import requests

#import the time and sleep function from time library that allow us to provide delay
from time import time,sleep

#To disable warning of channel is already in use
R.setwarnings(False)

# use the BOARD numbering scheme or we can use BCM scheme also
R.setmode(R.BOARD)

# set pin 12 in output mode in direction OUT and
# set pin 16 in input mode in direction IN
R.setup(12,R.OUT)
R.setup(16,R.IN)

# Define the trigger pin and echo pin on 12 and 16 pin respectively
Triger_pin = 12
Echo_pin = 16

#define post function which is responsible for sending distance to the broker with the increment of 1 in the value of i
def post_data(distance):
	i = 0
	print requests.post("http://try:try@broker.shiftr.io/himani",data = "distance")
	i +=1
	sleep(1)

#define distance function which gives us the object distance
def distance():
	#we initialize the trigger pin after each 1msec
	R.output(Triger_pin,True)
	sleep(0.00001)
	R.output(Triger_pin,False)

	#using time function from time library record the start and end time of the signal from ultrasonic sensor
	start_time = time()
	end_time = time()

	#when we not recieve any signal at echo pin do 
	while(R.input(Echo_pin) == 0):
		start_time = time()

	#when we recieve signal at the echo pin do
	while(R.input(Echo_pin) == 1):
		end_time = time()

	#calculate the duration by subtracting the start time by the end time
	#now use this duration time to calculate the distance by using the formula for distance calculation
	#i.e. distance = time * speed
	#Here we use the air as the transmission medium so the speed of the wave is 34300 m/sec
	#To calculate the objet distance we will divide the total distance by 2 to get the distnce between sensoor and object
	duration = end_time - start_time
	distance = (duration * 34300)/2

	#now using the post function here we send the calculated distance to the broker
	post_data(distance)

	#return the calculated distance
	return distance

#for each true value
while(True):
	#print the distance by calling the distance function defined above by providing the 1 sec of delay
	print distance()
	sleep(1)
