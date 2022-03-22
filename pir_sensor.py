import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIR,GPIO.IN)     
GPIO_PIR = 11
def triggering ():
    while True:
        Current_State = GPIO.input(GPIO_PIR)
        if(Current_State):
            return Current_State
        if(Current_State):
            time.sleep(0.01)
            Current_State=0
        else:
            return 0
