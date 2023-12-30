import time
import pygame
import KeyboardModule as kp
import MotorModule as mM
import RPi.GPIO as GPIO
import cv2
from matplotlib import pyplot as plt
import sys
import csv
import Adafruit_DHT
csvfile = "a.csv"
# Initialize Motor HAT library
kp.init()
maxThrottle = 1
motor = mM.Motor(2, 3, 4, 17, 22, 27)
# Initialize pygame (used to read the joystick)
pygame.init()

# Show available joysticks in the system
# In case there are more than 1 joystick connected. Check what
# index is the one you want to use and pass to the joystick.create.
#joystick.showAvailable()
# Initialize selected joystick. By default it uses TANK mode
# and index 0 for the jostick.

# Used to manage how fast the main loop runs
clock = pygame.time.Clock()

tick_count_left = 0
tick_count_right = 0
last_ticks_left = 0
last_ticks_right = 0
start_time = time.time_ns()

def ticksCounterLeft(pin):
    global tick_count_left
    tick_count_left += 1

def ticksCounterRight(pin):
    global tick_count_right
    tick_count_right += 1

# Setup GPIO5 to read left wheel encoder
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.add_event_detect(5, GPIO.BOTH, callback=ticksCounterRight)

# Setup GPIO12 to read right wheel encoder
GPIO.setup(6, GPIO.IN)
GPIO.add_event_detect(6, GPIO.BOTH, callback=ticksCounterLeft)

# Main program loop
###################
try:
    while True:
        throttle = kp.getKey('UP')*maxThrottle
        #joyVal['axis1']
        motor.move(throttle,0)
        # Calculate how many ns passed since last read
        t = time.time_ns()
        dt = t - start_time

        # Calculate the delta for ticks since last read
        delta_ticks_left = tick_count_left - last_ticks_left
        delta_ticks_right = tick_count_right - last_ticks_right

        # Update couunters to next read
        last_ticks_left = tick_count_left
        last_ticks_right = tick_count_right
        start_time = t


        # Calculate the wheel speeds (rpm)
        rpm_left = delta_ticks_left/dt * (60/650) * 10**9
        rpm_right = delta_ticks_right/dt * (60/650) * 10**9
        if rpm_left is not None:
            rpm_left = round(rpm_left, 2)
        # Show data
        print('Delta time', (dt/1000000), 'Left rpm', '{:02.2f}'.format(rpm_left), 'Right rpm', '{:02.2f}'.format(rpm_right))
        # Limit to 10 frames per second.
        clock.tick(10)
        timeC = time.strftime("%I")+':' +time.strftime("%M")+':'+time.strftime("%S")
        data = [rpm_left, timeC]
        #time.sleep(1)
        with open(csvfile, "a")as output:
            writer = csv.writer(output, delimiter=",", lineterminator = '\n')
            writer.writerow(data)
        k = cv2.waitKey(1)
        if k == ord('s'):
            break

except KeyboardInterrupt:
    # Press Ctrl+C to exit the application
    pass
# Existing application (clean up)

GPIO.cleanup()
pygame.quit()
motor.stop(10000)