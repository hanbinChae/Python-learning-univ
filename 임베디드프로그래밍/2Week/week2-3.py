# 마우스 클릭 이벤트로 여러가지 색상의 창 만들기
import cv2, numpy as np
dispW=640
dispH=480
fps=20

# window에서 좌클릭: circle + 좌표 표기
coord = []
img = np.zeros((200,200,3),np.uint8)

def lClick(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        clickPos = (x,y)
        coord.append(clickPos)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = int(frame[y,x,0]) # numpy 행렬의 특성으로 x,y값 순서 바뀜
        green = int(frame[y,x,1])
        red = int(frame[y,x,2])
        img[:,:,:] = [blue,green,red]
        
        fnt=cv2.FONT_HERSHEY_SIMPLEX
        textB = 255-blue
        textG = 255-green
        textR = 255-red
        colorText = str(blue)+','+str(green)+','+str(red)
        cv2.putText(img,colorText,(5,110),fnt,0.8,(textB,textG,textR),2)

        cv2.imshow('color',img)
        
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