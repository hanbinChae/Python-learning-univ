import face_recognition
import cv2
import os
import pickle

with open('regID.pkl','rb') as f:
    names = pickle.load(f)
    encodings = pickle.load(f)

cam = cv2.VideoCapture(0,cv2.CAP_V4L)
dispW = 640
dispH = 480
fps = 15
resizeRatio = 3

cam.set(cv2.CAP_RPOP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_RPOP_FRAME_HEIGHT,dispH)
cam.set(cv2.CAP_RPOP_FPS,fps)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame == cam.read()
    cv2.imshow('cam',frame)

    frameSmall = cv2.resize(frame, (0,0),fx=1/resizeRatio, fy=1/resizeRatio)

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    facePos = face_recognition.face_locations(frameRGB)
    candidates = face_recognition.face_encodings(frameRGB, facePos)

    for (top,right,bottom,left), canEncod in zip(facePos, candidate):
        matches = face_recognition.compare_faces(encodings,canEncod)
        name = 'unknown'
        if True in matches:
            idx = matches.index(True)
            name = names[idx]
            
        left *= resizeRatio
        right *= resizeRatio
        top *= resizeRatio
        bottom *= resizeRatio

        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),1)
        cv2.putText(frame,name,(left,top-5),font,0.7,(0,0,0),1)
    cv2.imshow('cam',frame)

    if cv2.waitKey(1) == ord('q'):
        break 

    if cv2.waitKey(1) ==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
