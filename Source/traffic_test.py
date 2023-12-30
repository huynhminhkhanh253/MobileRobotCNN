import cv2
import os
import Webcam as wM
import numpy as np


stop_cascade = cv2.CascadeClassifier('/home/pi/Desktop/MainProject/stop_sign.xml')

cap = cv2.VideoCapture(0)
_, img = cap.read()
cv2.waitKey(1)
cv2.imshow("Image", img)






