## ex27_cv_editor.py
#opencv 사용 이미지 편집기

import cv2
import numpy as np

# 이미지 로드
img = cv2.imread(filename='./day05/cat01.jpg')
if img is None:
    raise FileNotFoundError('이미지 로딩 실패!')

origin = img.copy() # 원본이미지 복사
win_name = 'Editor'

# 3 이미지 변경함수
def update(_=None):
    alpha =cv2.getTrackbarPos('Contrast',win_name)/50 # 이미지 대비
    blur = cv2.getTrackbarPos('Blur','Editor') #트랙바 이름 Blur에서 데이터 가져오기

    #대비/밝기 조절

    edited = cv2.convertScaleAbs(origin,alpha=alpha)

    #블러
    if blur >0:
        k=blur*2+1
        edited = cv2.GaussianBlur(edited,(k,k),0)


    cv2.imshow('Editor',edited)


# 3. 트랙바 윈도우 생성
cv2.namedWindow('Editor')
cv2.createTrackbar('Contrast','Editor',50,150,update)
cv2.createTrackbar('Brightness','Editor',100,200,update)
cv2.createTrackbar('Blur','Editor',0,10,update)
cv2.createTrackbar('Edge','Editor',0,200,update)

update()

#2. 기본동작원리
while True:
    key=cv2.waitKey(1)&0xff
    if key ==ord('r'):
        cv2.imshow('ImageEditor',origin)
        pass
    elif key == ord('q'): #프로그램 종료
        break
    else:
        cv2.imshow('Simple ImageEditor',origin)


cv2.destroyAllWindows()