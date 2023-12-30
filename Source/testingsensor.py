
from gpiozero import DistanceSensor
from time import sleep

d_sensor = DistanceSensor(echo=24,trigger = 23)
#d_sensor = sensor.distance

while True:
    print('distance=',(d_sensor.distance)*100,'cm')
    sleep(0.1)