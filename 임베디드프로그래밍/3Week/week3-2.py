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

    # cv2.inRange(img,lower bound, upper bound): 범위에 포함되는 경우, 255, 포함되지 않으면 0
    FGmask1=cv2.inRange(hsv,lowB1,upB1)
    FGmask2=cv2.inRange(hsv,lowB2,upB2)
    FGmask=cv2.add(FGmask1,FGmask2)
    cv2.imshow('FGmask',FGmask)

    contours,_=cv2.findContours(FGmask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.findContours(img,mode,method)
    # mode: RETR_EXTERNAL(외곽선만 추출), RETR_LIST(안쪽 모든 외곽선), RETR_CCOMP/RETR_TREE(계층구조포함)
    # method: CHAIN_NONE(외곽선의 모든 좌표), CHAIN_APPROX_SIMPLE(좌표 최소화)

    # contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    for cnt in range(len(contours)):
        if cv2.contourArea(contours[cnt])>50:
            cv2.drawContours(frame,contours,cnt,(0,255,0),2)
            # cv2.drawContours(img,contours,contour index,color,thickness)
            (x,y,w,h)=cv2.boundingRect(contours[cnt])
            # cv2.boundingRect(contours[index]
            # contours[index]의 좌측끝 x좌표,최상단 y좌표, 너비,높이
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow('cam',frame)
    cv2.moveWindow('cam',0,0)
    
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()