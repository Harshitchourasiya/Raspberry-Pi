#import post functio from the requests library to set connection
from requests import post

#import sleep function from time library to provide delay in seconds
from time import sleep

#initialize i with 0
i=0

#for every True value do
while True:
	#using post function with broker url send the data "kk" 
	#you can also create your own broker to set up the connection and send the data
	print post("http://try:try@broker.shiftr.io/shaan",data="kk")
	#increment in the value of i by 1
	i= i+1
	#provide delay of 1 sec between two value
	sleep(1)
