# getTrackbarPos을 활용하여 Scale로 화면속에서 도형 위치 조절
import cv2
dispW=640
dispH=320
fps = 20

def nothing():
    pass

cam = cv2.VideoCapture(0,cv2.CAP_V4L)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cam.set(cv2.CAP_PROP_FPS,fps)

cv2.namedWindow("cam")
# createTrackbar(name, window, initial_value, maxinum_value, Callback_function)
cv2.createTrackbar('posX','cam',320,dispW, nothing)
cv2.createTrackbar('posY','cam',240,dispH, nothing)
cv2.createTrackbar('width','cam',20,dispW, nothing)
cv2.createTrackbar('height','cam',20,dispH, nothing)

while True:
    ret,frame = cam.read()
    xVal = cv2.getTrackbarPos('posX','cam')
    yVal = cv2.getTrackbarPos('posY','cam')
    width = cv2.getTrackbarPos('width','cam')
    height = cv2.getTrackbarPos('height','cam')


    # frame = cv2.circle(frame, (xVal,yVal),7,(255,0,0),-1)
    #rectangle(img, upper_left, bottom_right, color(b,g,r), line_width) : 사각형
    frame = cv2.rectangle(frame,(xVal,yVal),(xVal+width,yVal+height),(0,0,0),-1)

    cv2.imshow('cam',frame)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

