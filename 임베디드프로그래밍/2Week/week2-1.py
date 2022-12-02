#drawing
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

    #rectangle(img, upper_left, bottom_right, color(b,g,r), line_width) : 사각형
    frame = cv2.rectangle(frame,(140,100),(180,140),(0,0,255),2)
    
    #circle(img, center, radius, color, line_width) : 원
    frame = cv2.circle(frame,(320,240),100,(100,150,0),3)

    # putText(img, str, (x,y), font, size, color, tickness) : 문자열 삽입
    font = cv2.FONT_HERSHEY_DUPLEX
    frame = cv2.putText(frame, "Chaehanbin",(300,440), font, 0.7, (255,0,0), 2)

    #line(img, start, end, color, line_width) : 선 그리기
    frame = cv2.line(frame, (10,10), (630,470), (255,255,255), 2)

    #arrowedLine : 화살표 라인, 라인과 같음
    frame = cv2.arrowedLine(frame, (10,470), (630,10), (255,0,255), 2)

    cv2.imshow('cam',frame)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()