#object Recognition with jetson.inference

import jetson.inference
import jetson.utils
import time

width,height = 1280,720
cam = jetson.utils.gstCamera(width,height,'/dev/video0')
disp = jetson.utils.glDisplay()
font = jetson.utils.cudaFont()
net = jetson.inference.imageNet('resnet-18') # resnet-18, googlenet

timeMark = time.time()
fpsFilter = 0

while disp.IsOpen():
    frame, width, height = cam.CaptureRGBA()
    classID,confidence = net.Classify(frame,width,height)
    item = net.GetClassDesc(classID)
    dt = time.time()-timeMark
    fps = 1/dt # frequency = 1/time
    fpsFilter*=0.9+(0.1*fps)
    timeMark = time.time()
    
    font.OverlayText(frame,width,height,str(round(fpsFilter,1))+"fps "+item,5,5,font.Magenta,font.Black)
    disp.RenderOnce(frame,width,height)


