import RPi.GPIO as G
from time import sleep

G.setwarnings(False)
G.setmode(G.BCM)
IR_INPUT =18
Led = 24
G.setup(18,G.IN)
G.setup(24,G.OUT)
try:
    count = 0
    while(True):
        status = G.input(IR_INPUT)
        if(status == True):     
            G.output(Led,True)
            sleep(0.1)
            count = count +1
            print count 
        G.output(Led,False)
except Excepion as ex:
    G.cleanup(ex)
finally:
    G.output(Led,False)

#or
#while(True):
#    status = G.input(IR_INPUT)
#    status = status+count
#    if(status == True):
#           print count
#          sleep(0.1)
#     G.output(Led,False)
