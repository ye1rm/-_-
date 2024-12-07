#main.py
import pygame
from constants import *
from assets import load_and_scale_image, image_paths
from game_logic import handle_events

# 초기화
pygame.init()

# 고정화면 초기화 (프레임 없는 창)
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Fixed Frame TALA Game")

# 이미지 로드
# 엑스 이미지 로드
close_image, close_width, close_height = load_and_scale_image(image_paths["close"], 0.05)
# 소리 ON 이미지 로드
soundON_imgae, soundON_width, soundON_height = load_and_scale_image(image_paths["soundON"], 0.07)
# 소리 OFF 이미지 로드
soundOFF_imgae, soundOFF_width, soundOFF_height = load_and_scale_image(image_paths["soundOFF"], 0.07)
# 화면 확대 이미지 로드
bigScreen_image, bigScreen_width, bigScreen_height = load_and_scale_image(image_paths["bigScreen"], 0.05)
# 화면 축소 이미지 로드
smallScreen_image, smallScreen_width, smallScreen_height = load_and_scale_image(image_paths["smallScreen"], 0.05)
# 도장판 이미지 로드
stampBoard_image, stampBoard_width, stampBoard_height = load_and_scale_image(image_paths["stampBoard"], 0.06)

# 버튼 위치 정의
# 엑스 버튼 위치 (고정 화면 상단 우측)
close_x = WIDTH - close_width - 10
close_y = 10
# 소리 버튼 위치 (엑스 버튼 왼쪽)
sound_x = close_x - soundON_width - 10
sound_y = close_y + (close_height - soundON_height) // 2  # 높이 조정
# 화면 버튼 위치 (소리 버튼 왼쪽)
screen_x = sound_x - bigScreen_width - 10
screen_y = 10
# 도장판 버튼 위치 (화면 버튼 왼쪽)
stampBoard_x = screen_x - stampBoard_width - 10
stampBoard_y = close_y + (close_height - stampBoard_height) // 2

# 초기 상태
current_state = STATE_HOME
running = True

# 게임 루프
while running:
    for event in pygame.event.get():
        running, current_state = handle_events(event, current_state, close_x, close_y, close_width, close_height)
    screen.fill(BLACK)

    # 출력
    # 엑스 버튼
    screen.blit(close_image, (close_x, close_y))
    # 소리 버튼
    screen.blit(soundON_imgae, (sound_x, sound_y))
    # 화면 버튼
    screen.blit(bigScreen_image, (screen_x, screen_y))
    # 도장판 버튼
    screen.blit(stampBoard_image, (stampBoard_x, stampBoard_y))

    pygame.display.update()

pygame.quit()

