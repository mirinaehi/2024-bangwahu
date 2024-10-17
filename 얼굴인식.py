import face_recognition
import cv2
import os

# 학습할 사진이 있는 디렉터리
KNOWN_FACES_DIR = 'known_faces'
# 테스트 할 사진파일
IMAGE_TO_TEST = 'test1.jpg'

TOLERANCE = 0.5
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'cnn'

def name_to_color(name):
    return [255, 255, 255]

print('얼굴 학습중')
known_faces = []
known_names = []

# 얼굴 학습
for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
        # 이미지 불러오기
        image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')
        # 이미지 중에서 얼굴만 추출
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(name)

