#main.py
import pygame
from constants import *
from assets import load_and_scale_image, assets_paths
from game_logic import handle_events
from HomeScreen import render_home_screen

# 초기화
pygame.init()

# 고정화면 초기화 (프레임 없는 창)
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Fixed Frame TALA Game")

# 고정화면 안에 띄울 게임화면
game_surface = pygame.Surface((GAME_AREA_WIDTH, GAME_AREA_HEIGHT))

# 폰트 로드
font = pygame.font.Font(assets_paths["font"], 24)
game_font = pygame.font.Font(assets_paths["font"], 36)
game_font.set_bold(True)

# 이미지 로드
# 엑스 이미지 로드
close_image, close_width, close_height = load_and_scale_image(assets_paths["close"], 0.05)
# 소리 ON 이미지 로드
soundON_imgae, soundON_width, soundON_height = load_and_scale_image(assets_paths["soundON"], 0.07)
# 소리 OFF 이미지 로드
soundOFF_imgae, soundOFF_width, soundOFF_height = load_and_scale_image(assets_paths["soundOFF"], 0.07)
# 화면 확대 이미지 로드
bigScreen_image, bigScreen_width, bigScreen_height = load_and_scale_image(assets_paths["bigScreen"], 0.05)
# 화면 축소 이미지 로드
smallScreen_image, smallScreen_width, smallScreen_height = load_and_scale_image(assets_paths["smallScreen"], 0.05)
# 도장판 이미지 로드
stampBoard_image, stampBoard_width, stampBoard_height = load_and_scale_image(assets_paths["stampBoard"], 0.06)
# 홈 이미지 로드
home_image, home_width, home_height = load_and_scale_image(assets_paths["home"], 0.07)

# 버튼 위치
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
# 홈 버튼 위치 (고정 화면 왼쪽 하단)
home_x = 10
home_y = HEIGHT - home_height - 10

# 초기 상태
current_state = STATE_HOME
running = True

# 게임 루프
while running:
    for event in pygame.event.get():
        running, current_state = handle_events(event, current_state, close_x, close_y, close_width, close_height)
    screen.fill(BLACK)

    # 게임 영역 렌더링
    if current_state == STATE_HOME:

        # 화면에 버튼 그리기
        start_text, start_text_rect, explanation_text, explanation_text_rect, game_text_surface, game_text_rect = render_home_screen(
            screen, font, game_font
        )
        screen.blit(start_text, start_text_rect)
        screen.blit(explanation_text, explanation_text_rect)
        screen.blit(game_text_surface, game_text_rect)

    elif current_state == STATE_GAME:
        game_surface.fill(LIGHT_GREEN)  # 게임 상태 배경 색상
        screen.blit(game_surface, (game_area_x, game_area_y))

    # 홈 버튼 생성   
    if current_state != STATE_HOME:
        screen.blit(home_image, (home_x, home_y))

    # 게임화면 초기화
    game_surface.fill(LIGHT_GREEN)

    # 상단 버튼 출력
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