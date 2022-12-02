#object Recognition with openCV

import jetson.inference
import jetson.utils
import time
import cv2
import numpy as np

width,height = 1280,720
cam = jetson.utils.gstCamera(width,height,'/dev/video0')
font = cv2.FONT_HERSHEY_SIMPLEX
net = jetson.inference.imageNet('googlenet') # resnet-18, googlenet
timeMark = time.time()

fpsFilter =0

while True:
    frame,width,height = cam.CaptureRGBA()
    classID, confidence = net.Classify(frame,width,height)
    item = net.GetClassDesc(classID)
    dt = time.time()-timeMark
    fps = 1/dt
    fpsFilter = fpsFilter*0.95+(0.05*fps)
    timeMark = time.time()
    cvFrame = jetson.utils.cudaToNumpy(frame,width,height,4)
    cvFrame = cv2.cvtColor(cvFrame,cv2.COLOR_RGBA2BGR).astype(np.uint8)
    cv2.putText(cvFrame,str(round(fpsFilter,1))+" fps "+item,(0,30),font,1,(0,0,255),2)

    cv2.imshow('cam',cvFrame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()