import cv2
import numpy as np
dispW=640
dispH=480
fps=20

cam=cv2.VideoCapture(0,cv2.CAP_V4L)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cam.set(cv2.CAP_PROP_FPS,fps)

img1=np.zeros((480,640,1),np.uint8)
img1[:,:320]=255

img2=np.zeros((480,640,1),np.uint8)
img2[190:290,270:370]=255

bitAnd=cv2.bitwise_and(img1,img2)
bitOr=cv2.bitwise_or(img1,img2)
bitXor=cv2.bitwise_xor(img1,img2)

cv2.namedWindow('cam')

while True:
    ret,frame=cam.read()

    frame=cv2.bitwise_and(frame,frame,mask=bitOr)
    # bitwise_and(img1,img2,mask): mask에서 참인 영역만 img1과 img2의 AND연산 결과 반환
    # 동일한 img를 and 연산할 경우, 해당 img가 반환

    cv2.imshow('cam',frame)
    cv2.moveWindow('cam',0,0)
    cv2.imshow('AND',bitAnd)
    cv2.moveWindow('AND',0,505)
    cv2.imshow('OR',bitOr)
    cv2.moveWindow('OR',705,0)
    cv2.imshow('XOR',bitXor)
    cv2.moveWindow('XOR',705,505)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()