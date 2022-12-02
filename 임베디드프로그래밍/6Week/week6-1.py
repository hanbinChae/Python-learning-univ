# jetson-inference/python/training <- Classification model 생성하고 Recognition (사진인식)
import cv2
import jetson.inference
import jetson.utils
import time
import numpy as np

dispW=800
dispH=600

timeStamp=time.time()
fpsFilter=0

net=jetson.inference.imageNet('googlenet',['--model=/home/chaehanbin/다운로드/jetson-inference/python/training/classification/myModel/resnet18.onnx','--input_blob=input_0','--output_blob=output_0','--labels=/home/cheon/Downloads/jetson-inference/myTrain/labels.txt'])
font=cv2.FONT_HERSHEY_SIMPLEX

cam=cv2.VideoCapture('/dev/video0')
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    _,img=cam.read()
    height=img.shape[0]
    width=img.shape[1]

    frame=cv2.cvtColor(img,cv2.COLOR_BGR2RGBA).astype(np.float32)
    frame=jetson.utils.cudaFromNumpy(frame)

    classID,confidences=net.Classify(frame,dispW,dispH)
    item=''
    item=net.GetClassDesc(classID)
    dt=time.time()-timeStamp 
    timeStamp=time.time() 
    fps=1/dt
    fpsFilter=.9*fpsFilter+.1*fps
    cv2.putText(img,str(round(fpsFilter,1))+'fps '+item,(0,30),font,1,(0,0,255),2)
    cv2.imshow('detectCam',img)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

# jetson.inference만으로는 detection 결과를 다루기 어려움
# cv2를 이용하여, grabbing information