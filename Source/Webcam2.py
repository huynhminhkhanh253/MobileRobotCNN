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
h = 5
x_shift = 600

###########
"""
def calculate(v,h,x_shift,img):
    d = 0
    alpha = 8.0 * math.pi / 180  # degree measured manually
    v0 = 119.865631204  # from camera matrix
    ay = 332.262498472  # from camera matrix
    # compute and return the distance from the target point to the camera
    d = h / math.tan(alpha + math.atan((v - v0) / ay))
    if d > 0:
        cv2.putText(img, "%.1fcm" % d,(img.shape[1] - 150, img.shape[0] - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    return d

def detecthumandoremon(img):
    a = 0
    human_doremon_cascade = cv2.CascadeClassifier('/home/pi/Desktop/MainProject/human_1.xml')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    human_1 = human_doremon_cascade.detectMultiScale(imgGray, 1.3,20 )
    for (x, y, w, h) in human_1:
        """
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.rectangle(img, (x, y), (x + 100, y + 40), (255, 0, 0), -1)
        cv2.putText(img, 'HUMAN', (x + 10, y + 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        a = y + h - 5
        a = y + h - 5
        """
        cv2.rectangle(img, (x-20, y), (x + w, y + h), (255, 0, 0), 2)
        #cv2.rectangle(img, (x, y), (x + 110, y + 50), (255, 0, 0), -1)
        cv2.putText(img, 'HUMAN', (x + 1, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        a = y + h - 5
        #cx = x + w // 2
        #cy = y + h // 2
        #area = w * h
        #cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        #print(v)
    return a

def detect(img):
    d = 0
    v = 0
    stopcascade = cv2.CascadeClassifier('/home/pi/Desktop/MainProject/stop_sign.xml')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    stop = stopcascade.detectMultiScale(imgGray, 1.2, 8)
    for (x, y, w, h) in stop:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)
        cv2.putText(img, 'STOP', (x, y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        v = y + h - 5
        #cx = x + w // 2
        #cy = y + h // 2
        #area = w * h
        #cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        #print(v)
    return v
"""
def getImg(display=True,size =[480,240]): #size=[480,240]):
    _, img = cap.read()
    img = cv2.resize(img,(size[0],size[1]))
    #v = detect(img)
    #a = detecthumandoremon(img)
    #imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #d = calculate(v,h,x_shift,img)
    """
    if d != 0:
        cv2.putText(img, "%.1fcm" % d,(img.shape[1] - 450, img.shape[0] - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    """
    #detect(img)
    #detecthumandoremon(img)
    """
    if d > 0:
        cv2.putText(img, '==',(img.shape[1] - 500, img.shape[0] - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    """
    if display:
        cv2.imshow('IMG',img)
        #cv2.imshow('gray',imgGray)
    return img

if __name__ == '__main__':
    while True:
        d = 0
        img = getImg(True,size =[480,320])
        cv2.waitKey(1)