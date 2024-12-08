# assets.py
import pygame

# 에셋 경로
assets_paths = {
    "close" : "C:/Users/shrew/OneDrive/바탕 화면/t/team1/assets/Icon/close.png",
    "soundON" : "C:/Users/shrew/OneDrive/바탕 화면/t/team1/assets/Icon/soundON.png",
    "soundOFF" : "C:/Users/shrew/OneDrive/바탕 화면/t/team1/assets/Icon/soundOFF.png",
    "bigScreen": "C:/Users/shrew/OneDrive/바탕 화면/t/team1/assets/Icon/bigScreen.png",
    "smallScreen": "C:/Users/shrew/OneDrive/바탕 화면/t/team1/assets/Icon/smallScreen.png",
    "stampBoard": "C:/Users/shrew/OneDrive/바탕 화면/t/team1/assets/Icon/stampBoard.png",
    "home" : "C:/Users/shrew/OneDrive/바탕 화면/t/team1/assets/Icon/home.png",
    "voice" : "C:/Users/shrew/OneDrive/바탕 화면/t/team1/assets/Icon/voiceSupport.png",
    "font" : "C:/Users/shrew/OneDrive/바탕 화면/t/team1/assets/fonts/Ramche.ttf",
    "bgm" : "C:/Users/shrew/OneDrive/바탕 화면/t/team1/assets/Bgm/sound-k-117217.mp3"
}

# 이미지 로딩 및 크기 조정 함수
def load_and_scale_image(image_path, scale_factor):
    image = pygame.image.load(image_path)
    rect = image.get_rect()
    new_width = int(rect.width * scale_factor)
    new_height = int(rect.height * scale_factor)
    image = pygame.transform.scale(image, (new_width, new_height))
    return image, new_width, new_height
