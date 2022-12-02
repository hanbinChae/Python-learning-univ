# PWM test
import Jetson.GPIO as GPIO
import time

PAN=32
TILT=33
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PAN,GPIO.OUT)
GPIO.setup(TILT,GPIO.OUT)

pwmP=GPIO.PWM(PAN,50)
pwmT=GPIO.PWM(TILT,50)

pwmP.start(3.0)
pwmT.start(3.0)

for pW in range(30,125):
    pwmP.ChangeDutyCycle(pW/10.0)
    pwmT.ChangeDutyCycle(pW/10.0)
    time.sleep(0.02)

for pW in range(125,30,-1):
    pwmP.ChangeDutyCycle(pW/10.0)
    pwmT.ChangeDutyCycle(pW/10.0)
    time.sleep(0.02)

pwmP.ChangeDutyCycle(0.0)
pwmT.ChangeDutyCycle(0.0)
time.sleep(1.0)

pwmP.stop()
pwmT.stop()
GPIO.cleanup()