#import the requests library 
import requests

# import the library that allows us to logically access the GPIO pins
# refer to the library as G, it is like an alias
import RPi.GPIO as G

#To disable warning of channel is already in use
G.setwarnings(False)

# use the BCM numbering scheme or we can use BOARD scheme also
G.setmode(G.BCM)

# set pin 18 in output mode in direction OUT
G.setup(18,G.OUT)

# do for every input 
while True:

	#take the user input for temprature as raw input
	var=raw_input("enter temp :")

	#to get a webpage and append the value of temprature input into temprature label
	p=requests.get("http://class.aarmontech.com/7/?tempreture="+var)

	#print the content i.e. temprature
	print p.content

	#to get a webpage and read the data from bulb.txt file using request library
	a=requests.get("http://class.aarmontech.com/7/bulb.txt")
	
	#store content of bulb.txt into X variable
	X=a.content

	#if bulb.txt has 1 then glow the led otherwise off the led
	if(X=='1'):
		G.output(18,True)
	else:
		G.output(18,False)
