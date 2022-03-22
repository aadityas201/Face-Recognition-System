import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIR,GPIO.IN)     
GPIO_PIR = 11
def triggering ():
    Current_State = GPIO.input(GPIO_PIR)
    if(Current_State):
        Current_State=0
        return 1
    else:
        return 0
