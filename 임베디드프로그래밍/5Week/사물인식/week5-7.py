#object detection with openCV

import cv2
import jetson.inference
import jetson.utils
import time
import numpy as np

net=jetson.inference.detectNet('ssd-mobilenet-v2',threshold=0.5)
dispW=640
dispH=480

font=cv2.FONT_HERSHEY_SIMPLEX
cam=cv2.VideoCapture('/dev/video0')
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

timeMark=time.time()
fpsFilter=0

while True:
    ret,frame=cam.read()
    height=frame.shape[0]
    width=frame.shape[1]

    frameRGBA=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA).astype(np.float32)
    frameRGBA=jetson.utils.cudaFromNumpy(frameRGBA)

    detections=net.Detect(frameRGBA,dispW,dispH)
    for object in detections:
        print(object)

    dt=time.time()-timeMark
    fps=1/dt
    fpsFilter=0.9*fpsFilter+0.1*fps
    timeMark=time.time()

    cv2.putText(frame,str(round(fpsFilter,1))+'fps',(0,30),font,1,(0,0,255),2)
    cv2.imshow('cam',frame)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()