#object detection with jetson.inference

import cv2
import jetson_inference
import jetson_utils
import time
import numpy as np

width=1280
height=720
cam=jetson_utils.gstCamera(width,height,'/dev/video0')
disp=jetson_utils.glDisplay()
# dtectNet: object detection, image로부터 인식된 객체의 위치와 객체명을 알려줌
net=jetson_inference.detectNet('ssd-mobilenet-v2',threshold=0.5)
# threshold: 해당 객체일 확률의 기준
# ex> 위의 경우, 0.5이상일 경우만 해당 object로 간주
timeMark=time.time()
fpsFilter=0

while disp.IsOpen():
    frame,frameW,frameH=cam.CaptureRGBA()
    detections=net.Detect(frame,frameW,frameH)
    disp.RenderOnce(frame,frameW,frameH)
    dt=time.time()-timeMark
    timeMark=time.time()
    fps=1/dt
    fpsFilter=fpsFilter*0.95+fps*0.05
    print(fpsFilter)

