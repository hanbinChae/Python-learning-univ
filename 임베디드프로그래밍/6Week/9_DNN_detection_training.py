import cv2
import jetson.inference
import jetson.utils
import time
import numpy as np

dispW=800
dispH=600

timeStamp=time.time()
fpsFilter=0

net=jetson.inference.detectNet(argv=['--model=/home/cheon/Downloads/jetson-inference/python/training/detection/ssd/myModel/ssd-mobilenet.onnx','--labels=/home/cheon/Downloads/jetson-inference/myTrain2/labels.txt','--input_blob=input_0','--output-cvg=scores','--output-bbox=boxes'],threshold=0.5)
font=cv2.FONT_HERSHEY_SIMPLEX
# check & change path of --model and --labels

cam=cv2.VideoCapture('/dev/video0')
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    _,img=cam.read()
    
    # detecting rectangle
    # put name of items

    cv2.imshow('detectCam',img)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()