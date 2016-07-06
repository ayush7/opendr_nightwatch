import time
import picamera
import pigpio
import os

camera = picamera.PiCamera()

# set the pins - names are based on the colours of the wires connecting to the LEDs
# NOTE: Both the visible and ir LEDs are active LOW, hence 0 is ON and vice versa
# Active LOW is due to NPN transistors
visible = 2
ir = 3

# pi is initialized as the pigpio object
pi = pigpio.pi()

pi.set_mode(visible,pigpio.OUTPUT)
pi.set_mode(ir,pigpio.OUTPUT)

# Defining functions for putting off each LED
def visibleON():
    # visible is ON and the other is OFF
    pi.write(visible,0)
    pi.write(ir,1)

def irON():
    # visible is OFF and the other is ON
    pi.write(visible,1)
    pi.write(ir,0)

def bothOFF():
    pi.write(visible, 1)
    pi.write(ir, 1)

def take_a_pic(pr_tx):
    irON()
    camera.capture(pr_tx + '_1.jpg', use_video_port=False)
    visibleON()
    camera.capture(pr_tx + '_2.jpg', use_video_port=False)
    camera.stop_preview()

take_a_pic('blah')
bothOFF()
