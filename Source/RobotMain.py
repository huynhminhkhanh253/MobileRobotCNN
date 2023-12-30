from MotorModule import Motor
import KeyboardModule as kp
#from CameraModule import piCam
from time import sleep
import JoyStickModule as js
motor = Motor(2,3,4,17,22,27)
#runCamera = False
movement = 'Joystick'
kp.init()
def main():
    if movement == 'Joystick':
        jsVal= js.getJS()
        motor.move(jsVal['axis2'],jsVal['axis1'],0.1)

    if kp.getKey('UP'):
        motor.move(0.6,0,0.1)
    elif kp.getKey('DOWN'):
        motor.move(-0.6,0,0.1)
    elif kp.getKey('RIGHT'):
        motor.move(0.5,0.3,0.1)
    elif kp.getKey('LEFT'):
        motor.move(0.5,-0.3,0.1)
    else:
        motor.stop(0.1)

if __name__ == '__main__':
    while True:
        main()