# trackbar로 백그라운드 조절
import cv2
import numpy as np
dispW=640
dispH=480
fps=20

def nothing(x):
    pass

cam=cv2.VideoCapture(0,cv2.CAP_V4L)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cam.set(cv2.CAP_PROP_FPS,fps)

cv2.namedWindow('cam')

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',600,0)
cv2.createTrackbar('hue1U','Trackbars',100,179,nothing)
cv2.createTrackbar('hue1L','Trackbars',50,179,nothing)
cv2.createTrackbar('hue2U','Trackbars',100,179,nothing)
cv2.createTrackbar('hue2L','Trackbars',50,179,nothing)

cv2.createTrackbar('satU','Trackbars',200,255,nothing)
cv2.createTrackbar('satL','Trackbars',100,255,nothing)

cv2.createTrackbar('valU','Trackbars',200,255,nothing)
cv2.createTrackbar('valL','Trackbars',100,255,nothing)

while True:
    ret,frame=cam.read()
    # frame=cv2.imread('smarties.png')

    cv2.imshow('cam',frame)
    cv2.moveWindow('cam',0,0)
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

    # cv2.inRange(img,lower bound, upper bound): 범위에 포함되는 경우, 255, 포함되지 않으면 0
    FGmask1=cv2.inRange(hsv,lowB1,upB1)
    FGmask2=cv2.inRange(hsv,lowB2,upB2)
    FGmask=cv2.add(FGmask1,FGmask2)
    cv2.imshow('FGmask',FGmask)

    # FGmask의 0이 아닌 영역에 해당하는 hsv
    FGhsv=cv2.bitwise_and(frame,frame,mask=FGmask)
    cv2.imshow('FGhsv',FGhsv)

    # BGmask
    BGmask=cv2.bitwise_not(FGmask)
    cv2.imshow('BGmask',BGmask)
    
    # BGmask를 BGR로 변경
    BG=cv2.cvtColor(BGmask,cv2.COLOR_GRAY2BGR)

    # BG와 FGhsv 결합
    final=cv2.add(BG,FGhsv)
    cv2.imshow('final',final)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()