import cv2
dispW=640
dispH=320
fps = 20

cam = cv2.VideoCapture(0,cv2.CAP_V4L)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cam.set(cv2.CAP_PROP_FPS,fps)

while True:
    ret,frame = cam.read()
    frame = cv2.flip(frame,1)
    
    cv2.imshow('cam',frame)
    cv2.moveWindow('cam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

