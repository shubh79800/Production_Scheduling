import plc
from plc import station
import time


# Initialising station  

OP090 = station("OP090")
ipAdd = OP090.selectIP()


#########################################

"""
output for each tag contains following elements

Element 1: Staion name which is being called
Element 2: Name of Tag
Element 3: Instance number (If more than one i.e. Robot, Safety Door)
Element 4: Value of Tag

"""

######################################
while True:
    print("START MONITORING")
    OP090.lcTag()
    OP090.swipeButton()
    OP090.robotAuto()
    OP090.robotRunning()
    print ("##################")
    time.sleep(5)



