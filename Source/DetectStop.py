import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def detect(img):
    stopcascade = cv2.CascadeClassifier('/home/pi/Desktop/MainProject/stop_sign.xml')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    stop = stopcascade.detectMultiScale(imgGray, 1.2, 8)
    for (x, y, w, h) in stop:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

#def main():

#if __name__ == '__main__':
   # while True:
    #    main()