import face_recognition
import cv2

trumpFace = face_recognition.load_image_file("/home/chaehanbin/다운로드/Chaehanbin_Jetson/id/Donald_Trump.jpg")
pelosiFace = face_recognition.load_image_file("/home/chaehanbin/다운로드/Chaehanbin_Jetson/id/Nancy_Pelosi.jpg")

trumpEnc = face_recognition.face_encodings(trumpFace)[0]
pelociEnc = face_recognition.face_encodings(pelosiFace)[0]

encodings = [trumpEnc,pelociEnc]
names = ['Donald_Trump', 'Nancy_Pelosi']

testImg = face_recognition.load_image_file("/home/chaehanbin/Desktop/chaehanbin_jetson/people/u11.jpg")
facePos = face_recognition.face_locations(testImg)
candidate = face_recognition.face_encoding(testImg,facePos)

font = cv2.FONT_HERSHEY_SIMPLEX
testImgBGR = cv2.cvtColor(testImg,cv2.COLOR_RGB2BGR)

for (y1, x1, y2, x2), faceEnc in zip(facePos,candidate):
    # (y1,x1,y2,x2) : (top, right, bottom, left)
    matches = face_recognition.compare_faces(encodings,faceEnc)
    # compare_faces : True/False 반환
    # ex) 위의 경우, [False, True]를 반환하면 faceEnc이 Trump와는 매칭되지 않고, Pelosi와 매칭되었음을 의미한다.
    name = 'No ID'
    if True in matches:
        idx = matches.index(True)
        # list.index(value) : list 내부에 있는 요소 중 value와 동일한 요소의 index 반환
        name = names[idx]

    cv2.rectangle(testImgBGR,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.putText(testImgBGR, name, (x2,y1-7),font,0.8,(0,255,0),2)

cv2.imshow('testImg',testImg)
cv2.imshow('testImgBGR',testImgBGR)

if cv2.waitKey[0] == ord('q'):
    cv2.destroyAllWindows()