
import time
import cv2
import Webcam as wM
import MotorModule as mM



motor = mM.Motor(2, 3, 4, 17, 22, 27)

h = 50

x_shift = 300

stop_flag = True
stop_flag2 = True

while True:
    img = wM.getImg(TrueS,size =[420,340])
    v = wM.detect(img)
    if v > 0:
        start_time = time.time_ns()
        a = 1
        break
    cv2.waitKey(1)
while a == 1:
    img = wM.getImg(True,size =[420,340])
    if stop_flag == True:
        motor.move(20,0)
        t = time.time_ns()
        dt = t - (start_time)
        c = dt/1000000000
        #print(c)
        if c >= 5:
            stop_flag = False
            #stop_sign_active = False
            print('Moi vao')
            start_time = t
            a = 2
    if stop_flag == False:
        motor.move(0,0)
    cv2.waitKey(1)
while a == 2:
    img = wM.getImg(True,size =[420,340])
    t = time.time_ns()
    dt = t - (start_time)
    c = dt/1000000000
    #print(c)
    if c > 5:
        motor.move(-25,0)
        t = time.time_ns()
        dt = t - (start_time)
        c = dt/1000000000
        #print(c)
        print('dong cua')
        if c > 10:
            a = 3
            break

    cv2.waitKey(1)
while a == 3:
    img = wM.getImg(True,size =[420,340])
    motor.move(0,0)
    cv2.waitKey(1)






    """
    d_face = 0

    #d_face = wM.calculate(v,h,x_shift,img)
    if v > 0 and stop_flag == True:
        a = 1
        print(v)
    if a == 1:
        motor.move(25,0)
        t = time.time_ns()
        dt = t - (start_time)
        c = dt/1000000000
        print(c)
        if c >= 5:
            stop_flag = False
            #stop_sign_active = False
            print('Wait for 5 second')
            start_time = t

    if stop_flag == False:
        motor.move(0,0)
        t = time.time_ns()
        dt = t - (start_time)
        c = dt/1000000000
        print(c)
        if c >= 5:
            stop_flag2 = False
            #stop_sign_active = False
            print('Wait for 5 second')
            start_time = t

    if  stop_flag2 == False:
        motor.move(0,0)
        t = time.time_ns()
        dt = t - (start_time)
        c = dt/1000000000
        print(c)
        if c >= 5:
            stop_flag = False
            #stop_sign_active = False
            print('Wait for 5 second')
            start_time = t

    cv2.waitKey(1)
    """