# assets.py
import os
import pygame

# 현재 스크립트 위치를 기준으로 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 파일의 디렉토리
PROJECT_DIR = os.path.dirname(BASE_DIR)  # 프로젝트 최상위 디렉토리
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")  # assets 폴더
ICON_DIR = os.path.join(ASSETS_DIR, "Icon")  # Icon 폴더
FONT_DIR = os.path.join(ASSETS_DIR, "fonts")  # fonts 폴더
BGM_DIR = os.path.join(ASSETS_DIR, "Bgm")  # Bgm 폴더
MAIN_FILE = os.path.join(BASE_DIR, "main.py")  # src 폴더의 절대 경로

# 에셋 경로
assets_paths = {
    "close": os.path.join(ICON_DIR, "close.png"),
    "soundON": os.path.join(ICON_DIR, "soundON.png"),
    "soundOFF": os.path.join(ICON_DIR, "soundOFF.png"),
    "bigScreen": os.path.join(ICON_DIR, "bigScreen.png"),
    "smallScreen": os.path.join(ICON_DIR, "smallScreen.png"),
    "stampBoard": os.path.join(ICON_DIR, "stampBoard.png"),
    "home": os.path.join(ICON_DIR, "home.png"),
    "voice": os.path.join(ICON_DIR, "voiceSupport.png"),
    "normal_face": os.path.join(ICON_DIR, "normal_face.png"),
    "alphabet_face": os.path.join(ICON_DIR, "alphabet_face.png"),
    "collision_face": os.path.join(ICON_DIR, "collision_face.png"),
    "body" : os.path.join(ICON_DIR, "body.png"),
    "font": os.path.join(FONT_DIR, "Ramche.ttf"),
    "bgm": os.path.join(BGM_DIR, "sound-k-117217.mp3"),
}

# 이미지 로딩 및 크기 조정 함수
def load_and_scale_image(image_path, scale_factor):
    image = pygame.image.load(image_path)  # 이미지 로드
    rect = image.get_rect()
    new_width = int(rect.width * scale_factor)  # 새로운 너비
    new_height = int(rect.height * scale_factor)  # 새로운 높이
    image = pygame.transform.scale(image, (new_width, new_height))  # 크기 조정
    return image, new_width, new_height
