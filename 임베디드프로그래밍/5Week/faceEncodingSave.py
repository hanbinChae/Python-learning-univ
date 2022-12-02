import face_recognition
import cv2
import os
import pickle

# encoding vector와 name 저장 list
encodings=[]
names=[]

# 등록된 사람의 사진이 저장된 directory
imgDir='/home/cheon/Desktop/jetson/id'
# os.walk(Dir): Dir이 포함하고 있는 root(현재 directory), directory, files를 반환 
for root,dirs,files in os.walk(imgDir): # root 내부에 dirs는 없음
    for file in files:
        imgPath=os.path.join(root,file)
        regFace=face_recognition.load_image_file(imgPath)
        encoding=face_recognition.face_encodings(regFace)[0]
        encodings.append(encoding)
        # path.splitext(file): 파일명과 확장자를 분리, [0]:파일명, [1]:확장자
        name=os.path.splitext(file)[0]
        names.append(name)

with open('regID.pkl','wb') as f:
    pickle.dump(names,f)
    pickle.dump(encodings,f)
