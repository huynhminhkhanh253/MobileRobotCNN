# Write your code here :-)
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import Webcam as wM
import MotorModule as mM
from DetectStop import detect
#######################################
steeringSen = 0.70  # Steering Sensitivity
maxThrottle = 0.13  # Forward Speed %
motor = mM.Motor(2, 3, 4, 17, 22, 27)  # Pin Numbers
model = load_model('/home/pi/Desktop/MainProject/model3.h5')
######################################

def preProcess(img):
    img = img[120:240, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img / 255
    return img

while True:
    img = wM.getImg(True, size=[340, 240])
    img = np.asarray(img)
    img = preProcess(img)
    img = np.array([img])
    steering = float(model.predict(img))
    print(steering * steeringSen)
    motor.move(maxThrottle, steering * steeringSen)
    print(maxThrottle)
    cv2.waitKey(1)