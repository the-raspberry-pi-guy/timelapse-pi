# Timelapse-Pi
# A backpack-mounted all-day timelapse project with the Raspberry Pi Zero
# Author: Matthew Timmons-Brown (The Raspberry Pi Guy)
# 19/03/2017

import picamera
import time
import os
from gpiozero import PWMLED, Button

image_path = "/home/pi"
pic_count = 0
shutdown = "sudo shutdown now"

led = PWMLED(14, True, 0, 100)
button = Button(15, False, None, 3, False)
camera = picamera.PiCamera()

camera.vflip = True

def starting_flash(light):
    light.blink(0.3, 0.3, 0, 0, 5, False)

def off_pulse(light):
    light.pulse(0.5, 0.5, 5, False)

def when_held():
    off_pulse(led)
    os.system(shutdown)

def when_pressed():
    stop = True

button.when_pressed = when_pressed
button.when_held = when_held

def main():
    stop = False
    while True:
        # Code start
        starting_flash(led)
        button.wait_for_press(None)
        stop = False
        while not stop:
            new_path = path + "image%s.jpg" % pic_count
            while os.path.exists(new_path):
                pic_count += 1
                new_path = path + "image%s.jpg" % pic_count

            camera.capture(new_path)
