import time
import picamera
import pigpio
import os

camera = picamera.PiCamera()

# set the pins - names are based on the colours of the wires connecting to the LEDs
# NOTE: Both the visible and ir LEDs are active LOW, hence 0 is ON and vice versa
# Active LOW is due to NPN transistors
switch = 4

# Some constants
time_stamp = time.time()

# pi is initialized as the pigpio object
pi = pigpio.pi()

pi.set_mode(switch ,pigpio.INPUT)
pi.set_pull_up_down(switch, pigpio.PUD_UP)

while True:
    print pi.read(switch)
    time.sleep(0.01)
