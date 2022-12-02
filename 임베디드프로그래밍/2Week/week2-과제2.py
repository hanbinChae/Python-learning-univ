# 마우스 클릭 이벤트 결과값을 지속적으로 출력하는 과제
import cv2
dispW=640
dispH=480
fps=20

# window에서 좌클릭: circle + 좌표 표기
evt = -1
coord = []

def lClick(event,x,y,flags,params):
    # event: mouse event의 종류
    # x,y: mouse event 위치
    # flags: event 발생 조건 (ctrl,shift.. 조합 등)
    # params: setMouseCallback에서 전달한 paramter
    global clickPos
    global evt
    if event==cv2.EVENT_LBUTTONDOWN:
        clickPos = (x,y)
        coord.append(clickPos)
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

    for c in coord:
        cv2.circle(frame,c,4,(0,0,255),2)
        fnt=cv2.FONT_HERSHEY_PLAIN
        posText=str(c)
        cv2.putText(frame,posText,c,fnt,1,(0,255,0),2)

        if cv2.waitKey(1) == ord('c'):
            coord = []
    if cv2.waitKey(1) == ord('q'):
        break
    
    
    cv2.imshow('cam',frame)

cam.release()
cv2.destroyAllWindows()