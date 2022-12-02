# 인물 여러명이 모인 사진에서 각각의 인물 인식하여 빨간 박스와, 이름으로 표시
import face_recognition
import cv2
import os
import pickle

# encoding vector와 name 저장 list
encodings = []
names = []

# 등록된 사람의 사진이 저장된 directory
imgDir = "/home/chaehanbin/다운로드/Chaehanbin_Jetson/id/"

# os.walk(Dir): Dir이 포함하고 있는 root(현재 directory), directory, files을 반환
for root, dirs, files in os.walk(imgDir): # root 내부의 dirs는 없음
    for file in files:
        imgPath = os.path.join(root,file) #각각의 파일 경로 추출
        regFace = face_recognition.load_image_file(imgPath) # 위의 경로를 통해 이미지 로드
        encoding = face_recognition.face_encodings(regFace)[0] #로드된 이미지 벡터로 인코딩하여 저장
        encodings.append(encoding)
        # path.splitext(file 명) : 파일명과 확장자를 분리, [0]: 파일명, [1]: 확장자
        name = os.path.splitext(file)[0]
        names.append(name)

print(names)

## 2. test image와 match

# test image가 존재하는 directory
testImgDir = "/home/chaehanbin/다운로드/Chaehanbin_Jetson/people"
font = cv2.FONT_HERSHEY_SIMPLEX

for root, dirs, files in os.walk(testImgDir):
    for file in files:
        imgPath = os.path.join(root,file)
        testImg = face_recognition.load_image_file(imgPath) #id 이미지 로드
        facePos = face_recognition.face_locations(testImg)
        testEncoding = face_recognition.face_encodings(testImg,facePos)

        #testImg의 지정된 영역 (facePos)에서만 encoding vector 추출
        #facePos와 testEncodings의 length는 동일
        # testEncodings: testImg의 모든 face에 대한 encoding vector를 반환
        
        # testImg를 BGR color로 변환
        testImgBGR = cv2.cvtColor(testImg,cv2.COLOR_RGB2BGR)
        
        for (top, right, bottom, left), face_encoding in zip(facePos,testEncodings):
            matches = face_recognition.compare_faces(encodings, faceEncoding)
            # 등록된 사람의 encoding vector와 testImg로 부터 추출한 얼굴을 encoding vector 매칭
            # 결과는 True/False
            # matches에 True가 없는 경우, name은 unknown
            name = 'unknown'
            if True in matches:
                idx = matches.index(True)
                name = names[idx]
            cv2.rectangle(testImgBGR,(left,top,right,bottom),(0,0,255),1)
            cv2.putText(testImgBGR,name,(left,top-5),font,0.8,(0,0,0),2)
        cv2.imshow(os.path.splitext(file)[0],testImgBGR)
        # window name: 파일명에서 확장자를 제외한 문자열

        # 'q'를 입력하면, 현재 textImgBGR 창이 닫히고, 다음 file로 이동
        if cv2.waitKey(0)==ord('q'):
            cv2.destroyAllWindows()
