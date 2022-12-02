import face_recognition
import cv2

image=face_recognition.load_image_file('/home/chaehanbin/다운로드/Chaehanbin_Jetson/img/u11.jpg')

faceLocations=face_recognition.face_locations(image)

image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
for (y1,x1,y2,x2) in faceLocations:
    cv2.rectangle(image,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('sample',image)
if cv2.waitKey(0)==ord('q'):
    cv2.destroyAllWindows()