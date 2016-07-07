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
switch = 4

# Some constants
time_stamp = time.time()

# pi is initialized as the pigpio object
pi = pigpio.pi()

pi.set_mode(visible, pigpio.OUTPUT)
pi.set_mode(ir, pigpio.OUTPUT)
pi.set_mode(switch, pigpio.INPUT)
pi.set_pull_up_down(switch, pigpio.PUD_UP)

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
    pi.write(visible, 0)
    pi.write(ir, 0)

def take_a_pic(pr_tx):
    irON()
    camera.capture(pr_tx + '_1.jpg', use_video_port=False)
    visibleON()
    camera.capture(pr_tx + '_2.jpg', use_video_port=False)
    camera.stop_preview()

def debounce_switch(gpio, level, tick):
    global time_stamp
    debounce_time = 0.02
    time_now = time.time()
    if (time_now - time_stamp) >= debounce_time:
        print "Taking pic now..."
        take_a_pic('blah')
        bothOFF()
    time_stamp = time_now

callback_button = pi.callback(switch, pigpio.RISING_EDGE, debounce_switch)
bothOFF()

while True:
    time.sleep(0.1)
