# assets.py
import pygame

# 에셋 경로
assets_paths = {
    "close" : "C:/Users/user/Desktop/TALA/TALA/assets/Icon/close.png",
    "soundON" : "C:/Users/user/Desktop/TALA/TALA/assets/Icon/soundON.png",
    "soundOFF" : "C:/Users/user/Desktop/TALA/TALA/assets/Icon/soundOFF.png",
    "bigScreen": "C:/Users/user/Desktop/TALA/TALA/assets/Icon/bigScreen.png",
    "smallScreen": "C:/Users/user/Desktop/TALA/TALA/assets/Icon/smallScreen.png",
    "stampBoard": "C:/Users/user/Desktop/TALA/TALA/assets/Icon/stampBoard.png",
    "font" : "C:/Users/user/Desktop/TALA/TALA/assets/fonts/Ramche.ttf"
}

# 이미지 로딩 및 크기 조정 함수
def load_and_scale_image(image_path, scale_factor):
    image = pygame.image.load(image_path)
    rect = image.get_rect()
    new_width = int(rect.width * scale_factor)
    new_height = int(rect.height * scale_factor)
    image = pygame.transform.scale(image, (new_width, new_height))
    return image, new_width, new_height
