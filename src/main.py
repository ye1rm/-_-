import pygame
from constants import *
from assets import load_and_scale_image
from game_logic import handle_events

# 초기화
pygame.init()

# 고정화면 초기화 (프레임 없는 창)
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Fixed Frame TALA Game")

# 이미지 로드
# 엑스 이미지 로드
close_image, close_width, close_height = load_and_scale_image("C:/Users/user/Desktop/TALA/TALA/assets/Icon/close.png", 0.05)

# 버튼 위치 정의
# 엑스 버튼 위치 (고정 화면 상단 우측)
close_x = WIDTH - close_width - 10
close_y = 10


# 초기 상태
current_state = STATE_HOME
running = True

# 게임 루프
while running:
    for event in pygame.event.get():
        running, current_state = handle_events(event, current_state, close_x, close_y, close_width, close_height)
    screen.fill(BLACK)

    # 엑스 버튼
    screen.blit(close_image, (close_x, close_y))

    pygame.display.update()

pygame.quit()

