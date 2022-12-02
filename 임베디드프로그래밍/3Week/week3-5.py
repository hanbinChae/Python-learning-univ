import cv2
import numpy as np
import Jetson.GPIO as GPIO
import time
dispW=640
dispH=480
fps=20

def nothing(x):
    pass

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

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',600,0)
cv2.createTrackbar('hue1U','Trackbars',218,255,nothing)
cv2.createTrackbar('hue1L','Trackbars',147,255,nothing)
cv2.createTrackbar('hue2U','Trackbars',191,255,nothing)
cv2.createTrackbar('hue2L','Trackbars',90,255,nothing)

cv2.createTrackbar('satU','Trackbars',255,255,nothing)
cv2.createTrackbar('satL','Trackbars',182,255,nothing)

cv2.createTrackbar('valU','Trackbars',231,255,nothing)
cv2.createTrackbar('valL','Trackbars',107,255,nothing)

while True:
    ret,frame=cam.read()
    # frame=cv2.imread('smarties.png')
    
    # hsv color로 변경
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    h1U=cv2.getTrackbarPos('hue1U','Trackbars')
    h1L=cv2.getTrackbarPos('hue1L','Trackbars')

    h2U=cv2.getTrackbarPos('hue2U','Trackbars')
    h2L=cv2.getTrackbarPos('hue2L','Trackbars')

    sU=cv2.getTrackbarPos('satU','Trackbars')
    sL=cv2.getTrackbarPos('satL','Trackbars')
    
    vU=cv2.getTrackbarPos('valU','Trackbars')
    vL=cv2.getTrackbarPos('valL','Trackbars')

    # hsv range를 ndarray로 설정
    upB1=np.array([h1U,sU,vU])
    lowB1=np.array([h1L,sL,vL])

    upB2=np.array([h2U,sU,vU])
    lowB2=np.array([h2L,sL,vL])


    FGmask1=cv2.inRange(hsv,lowB1,upB1)
    FGmask2=cv2.inRange(hsv,lowB2,upB2)
    FGmask=cv2.add(FGmask1,FGmask2)
    cv2.imshow('FGmask',FGmask)

    contours,_=cv2.findContours(FGmask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)

    for cnt in contours:
        if cv2.contourArea(cnt)>50:
            # cv2.drawContours(frame,[cnt],0,(0,255,0),2)
            (x,y,w,h)=cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            # center of the object
            objX=int(x+w/2)
            objY=int(y+h/2)
            cv2.circle(frame,(objX,objY),8,(0,255,0),-1)

            cenCamX=int(dispW/2) # 320
            cenCamY=int(dispH/2) # 240

            errP=objX-cenCamX
            errT=objY-cenCamY

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

        break

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