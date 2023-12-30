import cv2
import numpy as np
import os

Folder = 'n'
if not os.path.exists(Folder):
    print('b',Folder)
    os.makedirs(Folder)
cap = cv2.VideoCapture(0)
x1, y1 = 0,0
x2, y2 = 320,240
count = 0
size =[320,240]
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(size[0],size[1]))
    if ret == False:break
    k = cv2.waitKey(1)
    if k == ord('s'):
        cv2.imwrite(Folder + '/object_{}.jpg'.format(count),frame)
        print('img: '+'/object_{}.jpg'.format(count))
        count = count + 1
    if k == 27:
        break
    cv2.imshow('frame',frame)

cap.release()
cv2.destroyAllWindows()