# 개인 사진 등록 후 ID값으로 반환, 여러명 모인 사진에서 각각의 ID 노출

import face_recognition
import cv2
import os
import pickle

with open('regID.pkl','rb') as f:
    names=pickle.load(f)
    encodings=pickle.load(f)

# test image가 있는 directory
font=cv2.FONT_HERSHEY_SIMPLEX
testImgDir='/home/cheon/Desktop/jetson/people'
for root,dirs,files in os.walk(testImgDir): # root 내부에 dirs는 없음
        for file in files:
                imgPath=os.path.join(root,file)
                testImg=face_recognition.load_image_file(imgPath) # RGB image
                facePos=face_recognition.face_locations(testImg)
                testEncodings=face_recognition.face_encodings(testImg,facePos)
                # testImg의 지정된 영역(facePos)에서만 encoding vector 추출
                # facePos과 testEcodings의 length는 동일
                # testEncodings: testImg의 모든 face에 대한 encoding vector 반환
                
                # testImg를 BGR color로 변환
                testImgBGR=cv2.cvtColor(testImg,cv2.COLOR_RGB2BGR)
                for (top,right,bottom,left),faceEncoding in zip(facePos,testEncodings):
                        matches=face_recognition.compare_faces(encodings,faceEncoding)
                        # 등록된 사람의 encoding vector와 testImg로부터 추출한 얼굴을 encoding vector 매칭
                        # 결과는 True/False
                        # matches에 True가 없는 경우, name은 unknown
                        name='unknown'
                        if True in matches:
                                ind=matches.index(True)
                                name=names[ind]
                        cv2.rectangle(testImgBGR,(left,top),(right,bottom),(0,0,255),2)
                        cv2.putText(testImgBGR,name,(left,top-6),font,0.8,(0,0,0),2)

                cv2.imshow(os.path.splitext(file)[0],testImgBGR)   
                  # window name: 파일명에서 확장자를 제외한 문자열  

                  # q를 입력하면, 현재 testImgBGR창이 닫히고, 다음 file로 진행
                if cv2.waitKey(0)==ord('q'):
                        cv2.destroyAllWindows()                 



