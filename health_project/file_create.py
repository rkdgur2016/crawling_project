import os
import requests

def folder_create(folder_name):
    try:
        # 폴더 경로 생성 (폴더가 없으면 생성)
        path = f"image/{folder_name}"
        os.makedirs(path, exist_ok=True)  # 이미 폴더가 있으면 예외 발생하지 않도록 처리
    except Exception as e:
        print(f"폴더 생성 중 오류 발생: {e}")
        

def save_image(folder_name, image_name, content, file_extension):
    try:
        # 이미지 저장 경로 생성
        file_path = f"image/{folder_name}/{image_name}{file_extension}"
        
        # 바이너리 형식으로 파일 저장
        with open(file_path, "wb") as file:
            file.write(content)
        print(f"이미지가 저장됐습니다 : '{file_path}'")
    except Exception as e:
        print(f"이미지 저장 중 오류 발생: {e}")