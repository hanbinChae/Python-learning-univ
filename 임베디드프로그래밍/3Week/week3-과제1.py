#box 크기 안에서 img 움직이기 

import cv2
dispW=640
dispH=480
fps = 20

img_list = ['doughnut.jpeg','pl.jpg','dogeCoin.jpeg','Hermes_logo.png']
img = 'img/'+img_list[0]

cam = cv2.VideoCapture(0,cv2.CAP_V4L)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cam.set(cv2.CAP_PROP_FPS,fps)

# size of box
boxW = 50
boxH = 50
# initial position of box
posX = 20
posY = 100
# frame 당 이동 pixel
dx = 2
dy = 2


waterM = cv2.imread(img)
# change water to boxsize
waterM = cv2.resize(waterM,(boxW,boxH))
cv2.imshow('waterM',waterM)
cv2.moveWindow('waterM',0,0)
# change water to gray
waterGray = cv2.cvtColor(waterM,cv2.COLOR_BGR2GRAY)
cv2.imshow('waterGray',waterGray)
cv2.moveWindow('waterGray',143,0)
# making BG mask (bitwisze and를 통해 BG영역에만 img 통과)
ret, BGMask = cv2.threshold(waterGray,235,255,cv2.THRESH_BINARY)
cv2.imshow("BGMask",BGMask)
cv2.moveWindow("BGMask",223,0)
# FG Mask 만들기 (bitwisze and를 통해 FG영역에만 img 통과)
ret, FGMask = cv2.threshold(waterGray,235,255,cv2.THRESH_BINARY_INV)
cv2.imshow('FGMask',FGMask)
cv2.moveWindow("FGMask",513,0)
# Python logo image의 FG영역은 original color, BG는 0
waterFG = cv2.bitwise_and(waterM,waterM,mask=FGMask)
cv2.imshow('waterFG',waterFG)
cv2.moveWindow("waterFG",513,0)

while True:
    ret,frame = cam.read()
    
    # 좌우반전
    frame = cv2.flip(frame,1)

    # roi(bounding box 내부)
    roi = frame[posY:posY+boxH, posX:posX+boxW].copy()

    # roi 영역에서 BG만 frame 통과
    roiBG = cv2.bitwise_and(roi,roi,mask=BGMask)
    cv2.imshow("roiBG",roiBG)
    cv2.moveWindow("roiBG",0,203)
    roiBlended = cv2.add(roiBG,waterFG)
    cv2.imshow("roiBlended",roiBlended)
    cv2.moveWindow("roiBlended",213,203)

    frame[posY:posY+boxH, posX:posX+boxW] = roiBlended

    if posX<=0 or posX+boxW >= dispW:
        dx = dx*(-1)
    if posY<=0 or posY+boxH >= dispH:
        dy = dy*(-1)

    posX+=dx
    posY+=dy
    
   

    cv2.imshow('cam',frame)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

