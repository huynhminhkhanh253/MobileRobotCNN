
# Write your code here :-)
import time
from timeit import default_timer as timer
import numpy as np
import cv2
#from tensorflow.keras.models import load_model
import Webcam as wM

from gpiozero import DistanceSensor
import MotorModule as mM

#######################################
#steeringSen = 0.2  # Steering Sensitivity
maxThrottle = 0.19  # Forward Speed %
motor = mM.Motor(2, 3, 4, 17, 22, 27) # Pin Numbers
#sensordata = Se.Sensor(23,24)
#model = load_model('/home/pi/Desktop/MainProject/model2.h5')
h = 5
drive_time_after_stop = 0
x_shift = 300
stop_sign_active = True
stop_flag = True
count = 0
sensor = DistanceSensor(echo=24,trigger = 23)
stop_object = True
d_sensor_data = (sensor.distance)*100
#####################################
def preProcess(img):
    img = img[54:120, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img / 255
    return img
while True:
    d_sensor_data = (sensor.distance)*100
    d_stop_sign = 0
    d = 0
    img = wM.getImg(True,size =[320,240])
    v = wM.detect(img)
    d_stop_sign = wM.calculate(v,h,x_shift,img)

    #print(d)
    #img = np.asarray(img)
    #img = preProcess(img)
    #img = np.array([img])
    #steering = float(model.predict(img))
    #print(steering*steeringSen)
    #if 0 < d_stop_sign < 25: #and stop_sign_active is True:
    if 0 <= d_sensor_data <= 25:
        motor.move(0,0)
        print('stop,obstacle in front')

    if  5 <= d_stop_sign <= 25 and stop_sign_active == True:
        motor.move(0,0)
        print('stop_sign_ahead')
        start_time = time.time_ns()
        stop_flag = False
        stop_sign_active = False
        print(d)

    if stop_flag is False:
            t = time.time_ns()
            dt = t - (start_time)
            c = dt/1000000000
            print(c)
            if c >= 5:
                stop_flag = True
                #stop_sign_active = False
                print('Wait for 5 second')
                start_time = t
    """

        if stop_flag is False:
            stop_start = cv2.getTickCount()
            stop_flag = True
            stop_finish = cv2.getTickCount()
            stop_time = (stop_finish - stop_start) / cv2.getTickFrequency()
            print("Stop time: %.2fs" % stop_time)
        stop_finish = cv2.getTickCount()
        stop_time = (stop_finish - stop_start) / cv2.getTickFrequency()
        #print("Stop time: %.2fs" % stop_time)

        drive_time_after_stop = 0
        """
            #steering = float(model.predict(img))
    if stop_flag == True and d_sensor_data > 25 :
        drive_time_after_stop = time.time_ns()
        """
        count = 0
        if stop_sign_active == False:
            drive_time_after_stop = drive_time_after_stop +1
            if drive_time_after_stop == 60:
                stop_sign_active = True
        """
        motor.move(maxThrottle,0)
        print('foward')

    cv2.waitKey(1)
    """
    end_time = time.time()
    elapsed_time = end_time - start_time
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    """