import cv2

dispW=640
dispH=480
fps=20

cam=cv2.VideoCapture(0,cv2.CAP_V4L)

cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cam.set(cv2.CAP_PROP_FPS,fps)

outVid=cv2.VideoWriter('video/me.avi',cv2.VideoWriter_fourcc(*'DIVX'),fps,(dispW,dispH))
# cv2.VideoWriter('path+filename',codec,fps,(width,height))
# width와 height은 반드시 cam의 dispW와 dispH과 동일해야 함

while True:
    ret,frame=cam.read()
    mirror = cv2.flip(frame,1)
    cv2.imshow('webCam',mirror)
    outVid.write(mirror)
    # outVid(VideoWriter 객체)에 frame을 쌓아서 video를 만든다.

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
outVid.release()
cv2.destroyAllWindows()