# 카메라 화면 여러개, 다른 B,G,R 색상으로 나타내기
import cv2

display_W = 640
display_H = 480
fps = 20

cam = cv2.VideoCapture(0,cv2.CAP_V4L)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, display_W)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, display_H)
cam.set(cv2.CAP_PROP_FPS,fps)

while True:
    ret, frame = cam.read()
    # frame read
    cv2.imshow("cam",frame)
    # frame show
    cv2.moveWindow('cam',0,0)
    # move window

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #convert color (BGR -> GRAY)

    cv2.imshow('gray',gray)
    cv2.moveWindow('gray',640, 480)

    cv2.imshow('gray2',gray)
    cv2.moveWindow('gray2',0, 530)

    frameSmall = cv2.resize(frame,(320,240))

    cv2.imshow('gray3',gray)
    cv2.moveWindow('gray3',705, 530)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()