import time
import picamera
import pigpio
import os

# set the pins - names are based on the colours of the wires connecting to the LEDs
# NOTE: Both the orangeyellow and bluegreen LEDs are active LOW, hence 0 is ON and vice versa
orangeyellow = 2
bluegreen  = 3

# pi is initialized as the pigpio object
pi=pigpio.pi()

pi.set_mode(orangeyellow,pigpio.OUTPUT)
pi.set_mode(bluegreen,pigpio.OUTPUT)
# Defining functions for putting off each LED
def normalON():
    # orangeyellow is ON and the other is OFF
    pi.write(orangeyellow,0)
    pi.write(bluegreen,1)

def secondaryON():
    # toggle
    pi.write(orangeyellow,1)
    pi.write(bluegreen,0)

normalON()

def take_a_pic(pr_tx):
    camera.capture('images/' + pr_tx + '/' + str(i) + '_1.jpg', use_video_port=False)
    secondaryON()
    camera.capture('images/'+pr_tx+'/' + str(i) + '_2.jpg', use_video_port=False)
    normalON()
    camera.stop_preview()
    i=i+1

take_a_pic('blah')
