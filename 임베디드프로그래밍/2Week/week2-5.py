# 특정 영역만 회색 배경으로 전환

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
    roi = frame[100:300,200:400].copy()
    # frame 영역을 지정하여 새로운 ROI image 생성

    # roi를 gray로 변경
    roiGray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)

    # frame의 roi를 gray로 변경
    # gray 색상은 유지하되, 3채널로 확장
    frame[100:300,200:400] = cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR)

    cv2.imshow('cam',frame)
    cv2.moveWindow('cam',0,0)
    cv2.imshow('roi',roi)
    cv2.moveWindow('roi',705,0)
    cv2.imshow('roiGray',roiGray)
    cv2.moveWindow('roiGray',705,250)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

