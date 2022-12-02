#202263020 채한빈 과제
#box 크기 안에서 사각형 움직이기 

import cv2
dispW=640
dispH=480
fps = 20

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


while True:
    ret,frame = cam.read()

    #rectangle(img, upper_left, bottom_right, color(b,g,r), line_width) : 사각형
    cv2.rectangle(frame,(posX,posY),(posX+boxW,posY+boxH),(0,0,255),2)
 
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

