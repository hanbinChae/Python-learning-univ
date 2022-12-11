# 마우스 드래그 홀드를 통해 원하는 범위의 사각형 그리기
import cv2
dispW=640
dispH=480
fps=20
evt=-1
def drag(event,x,y,flags,params):
    global evt
    global posUL, posBR
    if event==cv2.EVENT_LBUTTONDOWN:
        evt=event
        posUL=(x,y)
    if event==cv2.EVENT_LBUTTONUP:
        evt=event
        posBR=(x,y)

cam=cv2.VideoCapture(0,cv2.CAP_V4L)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cam.set(cv2.CAP_PROP_FPS,fps)

cv2.namedWindow('cam')
cv2.setMouseCallback('cam',drag)

while True:
    ret,frame=cam.read()

    if evt==cv2.EVENT_LBUTTONUP:
        cv2.rectangle(frame,posUL,posBR,(0,0,255),2)
        roi=frame[posUL[1]:posBR[1],posUL[0]:posBR[0]]

        cv2.imshow('ROI',roi)
        cv2.moveWindow('ROI',705,0)

    cv2.imshow('cam',frame)
    cv2.moveWindow('cam',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()