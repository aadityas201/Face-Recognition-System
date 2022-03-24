from gpiozero import MotionSensor
import time

pir  = MotionSensor(26)
def triggering():
    while True:
        pir.wait_for_motion()
        return 1
            

