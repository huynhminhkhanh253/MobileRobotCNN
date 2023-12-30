import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
"""
class Sensor():
    def __init__(self,TRIG=23,ECHO=24):
        self.TRIG = TRIG
        self.ECHO = ECHO
    def sensordata(self):
        GPIO.setup(self.TRIG,GPIO.OUT)
        GPIO.setup(self.ECHO,GPIO.IN)
        GPIO.output(self.TRIG,False)
        #print('waiting for sensor to settle')
        #time.sleep(0.1)
        GPIO.output(self.TRIG,True)
        #time.sleep(0.00001)
        GPIO.output(self.TRIG,False)
        while GPIO.input(self.ECHO)==0:
            pulse_start=time.time()
        while GPIO.input(self.ECHO)==1:
            pulse_end=time.time()
        pulse_duration=pulse_end-pulse_start
        sensordata =pulse_duration*17150
        sensordata =round(sensordata,2)
        print('distance:',sensordata)
        return sensordata

def main():
    sensor_data = Sensor(23,24)
    sensordata = sensor_data.sensordata()
    return sensordata
    #print(sensordata)
if __name__ == '__main__':
    main()
"""
def sensordata(TRIG,ECHO):
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG,False)
        #print('waiting for sensor to settle')
        #time.sleep(0.05)
        GPIO.output(TRIG,True)
        #time.sleep(0.05)
        GPIO.output(TRIG,False)
        while GPIO.input(ECHO)==0:
            pulse_start=time.time()
        while GPIO.input(ECHO)==1:
            pulse_end=time.time()
        pulse_duration=pulse_end-pulse_start
        sensordata =pulse_duration*17150
        sensordata =round(sensordata,2)
        print(sensordata)
        return sensordata

while True:
    sensordata(24,23)
    time.sleep(1)