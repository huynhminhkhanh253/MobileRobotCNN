import cv2
import numpy as np
import os

Folder = 'p1'
if not os.path.exists(Folder):
    print('a',Folder)
    os.makedirs(Folder)
cap = cv2.VideoCapture(0)
x1, y1 = 150,40
x2, y2 = 250,150
count = 0
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(320,240))
    if ret == False:break
    imAux = frame.copy()
    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)
    object = imAux[y1:y2,x1:x2]

    k = cv2.waitKey(1)
    if k == ord('s'):
        cv2.imwrite(Folder + '/object_{}.jpg'.format(count),object)
        print('img: '+'/object_{}.jpg'.format(count))
        count = count + 1
    if k == ord('c'):
        break
    cv2.imshow('frame',frame)

cap.release()
cv2.destroyAllWindows()