import cv2
import numpy as np
dispW=320
dispH=240
fps = 20

cam = cv2.VideoCapture(0,cv2.CAP_V4L)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cam.set(cv2.CAP_PROP_FPS,fps)

cv2.namedWindow('cam')
blank = np.zeros([dispH,dispW,1],np.uint8)

while True:
    ret,frame = cam.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #cv2.split : BGR 채널 분리
    b,g,r = cv2.split(frame)
    #cv2.merge : 채널 결합 (3개 채널)
    bImg = cv2.merge((b,blank,blank))
    gImg = cv2.merge((blank,g,blank))
    rImg = cv2.merge((blank,blank,r))
    
    merge1 = cv2.merge((g,b,r))
    b[:]=b[:]*1.2
    merge2 = cv2.merge((b,g,r))

    cv2.imshow('cam',frame)
    cv2.moveWindow('cam',0,0)

    cv2.imshow('blue',bImg)
    cv2.moveWindow('blue',375,0)

    cv2.imshow('green',gImg)
    cv2.moveWindow('green',0,292)

    cv2.imshow('red',rImg)
    cv2.moveWindow('red',375,292)

    cv2.imshow("merge1",merge1)
    cv2.moveWindow('merge1',700,0)

    cv2.imshow("merge2",merge2)
    cv2.moveWindow("merge2",700,300)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

