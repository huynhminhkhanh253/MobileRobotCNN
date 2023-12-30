import Webcam as wM
import chessboardcollectmodule as cbm
import KeyboardModule as kp
import cv2
from time import sleep
import pygame

kp.init()
keyVal = 0
record = 0
while True:
    if kp.getKey('SPACE') == 1:
        if record == 0: print('Recording Started ...')
        record +=1
        sleep(0.300)
    if record == 1:
        img = wM.getImg(True,size=[240,120])
        cbm.saveData(img)
    if record == 2:
        record = 0
        print('end')
        break
    cv2.waitKey(500)