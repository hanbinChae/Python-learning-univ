# 마우스 클릭 이벤트
import cv2
dispW=640
dispH=480
fps=20

# window에서 좌클릭: circle + 좌표 표기
evt = -1

def lClick(event,x,y,flags,params):
    # event: mouse event의 종류
    # x,y: mouse event 위치
    # flags: event 발생 조건 (ctrl,shift.. 조합 등)
    # params: setMouseCallback에서 전달한 paramter
    global clickPos
    global evt
    if event==cv2.EVENT_LBUTTONDOWN:
        clickPos = (x,y)
        evt=event

cv2.namedWindow('cam')
cv2.setMouseCallback('cam',lClick)
# setMouseCallback(name of window,callback function,parameter)

cam=cv2.VideoCapture(0,cv2.CAP_V4L)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cam.set(cv2.CAP_PROP_FPS,fps)

while True:
    ret,frame=cam.read()

    if evt==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(frame,clickPos,5,(0,0,255),2)
        fnt=cv2.FONT_HERSHEY_PLAIN
        posStr=str(clickPos)
        cv2.putText(frame,posStr,clickPos,fnt,1,(0,255,0),2)

    cv2.imshow('cam',frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()