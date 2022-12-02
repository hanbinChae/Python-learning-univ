import cv2
import numpy as np
dispW=320
dispH=242
fps = 20

cam = cv2.VideoCapture(0,cv2.CAP_V4L)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cam.set(cv2.CAP_PROP_FPS,fps)

waterM = cv2.imread("img/cv.jpg")
waterM = cv2.resize(waterM,(dispW,dispH))
waterGray = cv2.cvtColor(waterM,cv2.COLOR_BGR2GRAY)

# cv2.threshold(img, threshold, value, option)
# img는 반드시 1채널
# img pixel value가 threshold 이상일 때, value로 변경
# THRESH_BINARY INV (inverse : 반대)

#OpenCV logo의 배경
_,BGMask = cv2.threshold(waterGray, 200, 255,cv2.THRESH_BINARY)
FGMask = cv2.bitwise_not(BGMask)
cv2.imshow('BG',BGMask)
cv2.imshow('FG',FGMask)

cv2.namedWindow("cam")

while True:
    ret,frame = cam.read()
    frame=cv2.flip(frame,1)

    #frame은 OpenCV logo의 배경부분으로만 통과
    BG = cv2.bitwise_and(frame,frame,mask=BGMask)
    FG = cv2.bitwise_and(waterM,waterM,mask=FGMask)

    addImg = cv2.add(BG,FG)
    cv2.imshow('cam',BG)
    cv2.imshow('addImg',addImg)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

