"""
-This module gets an image through the webcam
using the opencv package
-Display can be turned on or off
-Image size can be defined
"""
import cv2
import math
###########

###########

d = 0
cap = cv2.VideoCapture(0)
h2 = 9.98
h = 6.55
x_shift = 600

###########

def calculate(v,h,x_shift,img):
    d = 0
    alpha = 15 * math.pi / 180  # degree measured manually
    v0 = 119.865631204   # from camera matrix
    ay = 332.262498472  # from camera matrix
    # compute and return the distance from the target point to the camera
    d = h / math.tan(alpha + math.atan((v - v0) / ay))
    """
    if d > 0:
        cv2.putText(img, 'd to Stop_Sign',(img.shape[1] - 125, img.shape[0] - 30),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.putText(img, "%.1fcm" % d,(img.shape[1] - 80, img.shape[0] - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    """
    return d

def calculate2(a,h,x_shift,img):
    d = 0
    alpha = 15 * math.pi / 180  # degree measured manually
    v0 = 119.865631204   # from camera matrix
    ay = 332.262498472  # from camera matrix
    # compute and return the distance from the target point to the camera
    d = h2 / math.tan(alpha + math.atan((a - v0) / ay))
    if d > 0:
        cv2.putText(img,'d to Obstacle',(img.shape[1] -315, img.shape[0] - 30),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.putText(img,"%.1fcm" % d,(img.shape[1] -315, img.shape[0] - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    return d
"""
def detect(img):
    d = 0
    v = 0
    stopcascade = cv2.CascadeClassifier('/home/pi/Desktop/MainProject/stop_sign.xml')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    stop = stopcascade.detectMultiScale(imgGray, 1.2, 6)
    for (x, y, w, h) in stop:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img, 'Stop', (x, y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        v = y + h
        #cx = x + w // 2
        #cy = y + h // 2
        #area = w * h
        #cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        #print(v)
    return vb
"""
def detect(img):
    d = 0
    v = 0
    stopcascade = cv2.CascadeClassifier('/home/pi/Desktop/MainProject/haarcascade_frontalface_default.xml')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    stop = stopcascade.detectMultiScale(imgGray, 1.1, 1)
    for (x, y, w, h) in stop:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, 'Khanh', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        v = y + h
        #cx = x + w // 2
        #cy = y + h // 2
        #area = w * h
        #cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        #print(v)
    return v

def detect2(img):
    d = 0
    a = 0
    stopcascade = cv2.CascadeClassifier('/home/pi/Desktop/MainProject/object_4.xml')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    stop = stopcascade.detectMultiScale(imgGray, 1.04, 1)
    for (x, y, w, h) in stop:
        cv2.rectangle(img, (x, y), (x + w+80, y + h+55), (0, 255, 255), 2)
        cv2.putText(img, 'Obstacle', (x, y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        a = y + h
        #cx = x + w // 2
        #cy = y + h // 2
        #area = w * h
        #cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        #print(v)
    return a

def getImg(display=True,size =[3000,2500]): #size=[480,240]):
    _, img = cap.read()
    img = cv2.resize(img,(size[0],size[1]))
    v = detect(img)
    #a = detect2(img)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    d = calculate(v,h,x_shift,img)
    #d2 = calculate2(a,h,x_shift,img)
    """
    if d != 0:
        cv2.putText(img, "%.1fcm" % d,(img.shape[1] - 450, img.shape[0] - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    if d2 != 0:
        cv2.putText(img, "%.1fcm" % d,(img.shape[1] - 450, img.shape[0] - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    """
    """
    if d > 0:
        cv2.putText(img, '==',(img.shape[1] - 500, img.shape[0] - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    """
    """
    """
    if display:
        cv2.imshow('IMG',img)
        #cv2.imshow('gray',imgGray)
    return img

if __name__ == '__main__':
    while True:
        d = 0
        img = getImg(True,size =[420,340])
        #img = getImg(True,size =[320,240])
        cv2.waitKey(10)