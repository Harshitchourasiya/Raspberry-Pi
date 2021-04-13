# import the library that allows us to logically access the GPIO pins
# refer to the library as G, it is like an alias
import RPi.GPIO as G

#import the sleep module from time library that allow us to provide delay
from time import sleep

#To disable warning of channel is already in use
G.setwarnings(False)

# use the BCM numbering scheme or we can use BOARD scheme also
G.setmode(G.BCM)

# set pin 18 in input mode in direction IN
IR_INPUT= 18
G.setup(IR_INPUT,G.IN)

# set pin 16,12,13 to be in output mode in direction OUT
G.setup(16, G.OUT)
G.setup(12,G.OUT)
G.setup(13,G.OUT)

#intialize count variable as c with 0
c = 0

#store output pins in list named a
a=[16,12,13]

#main loop starts
try:
	while(True):
        #read input of IR sensor and store it in status variable 
		status = G.input(IR_INPUT)

		#if there is no input is recieved from IR then just continue
		if not status:
			continue

		#when input is recieved again
		while status:
			status = G.input(IR_INPUT)
			sleep(0.1)

			#increment in c variable
			c = c + 1

                        #check if value of c is between 0 to 90 then glow led one by one
			if( c<30 and c>=0):
				G.output(16,True)
			if( c<60 and c>=30):
				G.output(12,True)
			if( c<90 and c>=60):
				G.output(13,True)

                #for each led in list "a" off all of them 
		for i in  a:
			G.output(i,False)

                #set the value of c to 0 
		c = 0

# end program cleanly
except Exception as ex:
	print str(ex)

#finally set all the led off
finally:
	G.output(16,False)
	G.output(12,False)
	G.output(13,False)
	G.cleanup()
