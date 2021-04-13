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

# set pin 24 in output mode in direction OUT
Led = 24
G.setup(24,G.OUT)

#main loop starts 
try:
	#whenever there input is recieved from IR sensor
	while(True):
		#store input in status variable
		status = G.input(IR_INPUT)

		#if input is true then glow the led 
		if (status == True):
			G.output(Led,True)
			sleep(0.1)
		G.output(Led,False)


#end program cleanly
except Exception as ex:
	G.cleanup()

#finally off the led
finally:
	G.output(Led,Falsse)

