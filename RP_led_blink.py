# import the library that allows us to logically access the GPIO pins
# refer to the library as G, it is like an alias
import RPi.GPIO as G

#import the sleep module from time library that allow us to provide delay
from time import sleep

#To disable warning of channel is already in use
G.setwarnings(False)

# use the BCM numbering scheme or we can use BOARD scheme also
G.setmode(G.BCM)

# set pin 18 to be in output mode in direction IN/OUT
G.setup(18,G.OUT)

#main loop starts
try:
    while(True):
        # set 18 pin to HIGH
        G.output(18,True)
        sleep(2)

        # set 18 pin to LOW after 2 second of delay
        G.output(18,False)
        sleep(2)

#end program cleanly
except Exception as ex:
    G.cleanup(ex)
