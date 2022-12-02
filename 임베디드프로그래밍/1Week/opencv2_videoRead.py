import cv2

myVid=cv2.VideoCapture('video/me.avi')

# video file을 그대로 load함 (set이 필요없음, 있어도 무시함)

while True:
    ret,frame=myVid.read()

    if cv2.waitKey(30)==ord('q') or ret==False:        
        break
    
    cv2.imshow('video',frame)

myVid.release()
cv2.destroyAllWindows()

