# 얼굴 인식
import cv2
dispW=640
dispH=320
fps = 20

cam = cv2.VideoCapture(0,cv2.CAP_V4L)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cam.set(cv2.CAP_PROP_FPS,fps)

cv2.namedWindow('cam')
faceDetect = cv2.CascadeClassifier("/home/chaehanbin/다운로드/Chaehanbin_Jetson/data/frontalface_default.xml")
eyeDetect  = cv2.CascadeClassifier("/home/chaehanbin/다운로드/Chaehanbin_Jetson/data/eye.xml")

while True:
    ret,frame = cam.read()
    frame = cv2.flip(frame,1)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    faces = faceDetect.detectMultiScale(gray,1.3,5)
    # detectMultiScale(img, img축소 비율, 검증 갯수)
    # faces: face 영역의 (좌측상단 x, 좌측상단 y, 너비w, 높이h) (tuple)

    

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        
        roi = gray[y:y+h,x:x+h]
        roiColor=frame[y:y+h,x:x+w]
        eyes = eyeDetect.detectMultiScale(roi)
        
        for (xE,yE,wE,hE) in eyes:
            cv2.circle(roiColor,(int(xE+wE/2),int(yE+hE/2)),5,(0,255,),-1)
            
        frame[y:y+h,x:x+w] = roiColor

    cv2.imshow('cam',frame)
    cv2.moveWindow('cam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

