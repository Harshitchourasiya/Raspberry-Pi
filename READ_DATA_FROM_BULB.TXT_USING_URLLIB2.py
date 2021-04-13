#import the library that allows us to logically access the given URL over internet
# refer to the library as br, it is like an alias
import urllib2 as br

#import the library that allows us to logically access the GPIO pins
# refer to the library as G, it is like an alias
import RPi.GPIO as G

# use the BCM numbering scheme or we can use BOARD scheme also
G.setmode(G.BCM)

# set pin 18 in output mode in direction OUT
G.setup(18,G.OUT)

# do for every input
while True:
	#to get a webpage and read the data from bulb.txt file using urlopen() function
	con = br.urlopen("http://class.aarmontech.com/7/bulb.txt")
	p=con.read()
	print con.read(),"a"

	#if the obtain data is equa to 1 then write true and glow the led otherwise off the led
	if (p=='1'):
		print "true"
		G.output(18,True)
	else:
		print "false"
		G.output(18,False)
 