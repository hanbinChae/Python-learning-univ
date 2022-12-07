#얼굴인식 + 모터 움직임
import cv2
import numpy as np
import Jetson.GPIO as GPIO
import time

dispW=640
dispH=480
fps=20

PAN=32
TILT=33

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PAN,GPIO.OUT)
GPIO.setup(TILT,GPIO.OUT)

pwmP=GPIO.PWM(PAN,50)
pwmT=GPIO.PWM(TILT,50)

pan = 3.0
tilt = 3.0

pwmP.start(pan)
pwmT.start(tilt)

cam=cv2.VideoCapture(0,cv2.CAP_V4L)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cam.set(cv2.CAP_PROP_FPS,fps)

cv2.namedWindow('cam')

faceDetect = cv2.CascadeClassifier('/home/chaehanbin/다운로드/Chaehanbin_Jetson/data/face.xml')
eyeDetect = cv2.CascadeClassifier('/home/chaehanbin/다운로드/Chaehanbin_Jetson/data/eye.xml')

while True:
    ret,frame=cam.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5)

    if len(faces) != 0:
        (x,y,w,h)=faces[0]
        # center of the object
        objX=int(x+w/2)
        objY=int(y+h/2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

        cenCamX=int(dispW/2) # 320
        cenCamY=int(dispH/2) # 240

        errP=objX-cenCamX
        errT=cenCamY-objY

        if abs(errP)>50:
            pan=pan-errP/1000

        if abs(errT)>50:
            tilt=tilt-errT/1000
        
        if pan>12.5:
            pan=12.5
        if pan<3.0:
            pan=3.0

        if tilt>12.5:
            tilt=12.5
        if tilt<3.0:
            tile=3.0

        pwmP.ChangeDutyCycle(pan)
        pwmT.ChangeDutyCycle(tilt)
        time.sleep(0.02)

    cv2.imshow('cam',frame)
    cv2.moveWindow('cam',0,0)
    
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

pwmP.ChangeDutyCycle(0.0)
pwmT.ChangeDutyCycle(0.0)
time.sleep(1.0)

pwmP.stop()
pwmT.stop()
GPIO.cleanup()