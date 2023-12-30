import Webcam as wM
import DataCollectionModule as dcM

import KeyboardModule as kp
import MotorModule as mM
import cv2
from time import sleep
import pygame

kp.init()
maxThrottle = 0.25
motor = mM.Motor(2, 3, 4, 17, 22, 27)
keyVal = 0
record = 0
while True:
    if kp.getKey('LEFT'):
        keyVal = -0.5
    elif kp.getKey('RIGHT'):
        keyVal = 0.5
    else:
        keyVal = 0
    #joyVal = jsM.getJS()
    #print(jo    yVal)
    steering = keyVal    #joyVal['axis1']
    throttle = kp.getKey('UP')*maxThrottle
    if kp.getKey('SPACE') == 1:
        if record == 0: print('Recording Started ...')
        record +=1
        sleep(0.300)
    if record == 1:
        img = wM.getImg(True,size=[320,240])
        dcM.saveData(img,steering)
    elif record == 2:
        dcM.saveLog()
        record = 0

    motor.move(throttle,steering)
    cv2.waitKey(1)