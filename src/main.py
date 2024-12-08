#main.py
import pygame
from constants import *
from assets import assets_paths
from game_logic import handle_events
from HomeScreen import render_home_screen, draw_grid
###############예림##############
from HowScreen import render_how_to_play_screen # 추가된 부분
################################

# 초기화
pygame.init()

# Mixer 초기화
pygame.mixer.init()

# 고정화면 초기화 (프레임 없는 창)
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Fixed Frame TALA Game")

# 고정화면 안에 띄울 게임화면
game_surface = pygame.Surface((GAME_AREA_WIDTH, GAME_AREA_HEIGHT))

# 폰트 로드
font = pygame.font.Font(assets_paths["font"], 24)
game_font = pygame.font.Font(assets_paths["font"], 36)
game_font.set_bold(True)

# BGM 로드
pygame.mixer.music.load(assets_paths["bgm"])

pygame.mixer.music.play(-1)
# 초기 상태
current_state = STATE_HOME
running = True

###########예림###############
sound_status = True
##############################

# 게임 루프
while running:
    for event in pygame.event.get():
        running, current_state, sound_status = handle_events(event, current_state, sound_status)
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
        draw_grid(game_surface)
        screen.blit(game_surface, (game_area_x, game_area_y))
        ################예림##############
    # 게임 설명 화면 렌더링
    elif current_state == STATE_HOW:
        start_text, start_text_rect = render_how_to_play_screen(screen, font)
        screen.blit(start_text, start_text_rect)

    # 홈 버튼 생성   
    if current_state != STATE_HOME:
        screen.blit(home_image, (home_x, home_y))

    # 상단 버튼 출력
    # 엑스 버튼
    screen.blit(close_image, (close_x, close_y))
    ############예림##########
    # 소리 버튼
    if sound_status:
        screen.blit(soundON_image, (sound_x, sound_y))
        pygame.mixer.music.unpause()
    else:
        screen.blit(soundOFF_image, (sound_x, sound_y))
        pygame.mixer.music.pause()
    ###########################
    # 화면 버튼
    screen.blit(bigScreen_image, (screen_x, screen_y))
    # 도장판 버튼
    screen.blit(stampBoard_image, (stampBoard_x, stampBoard_y))

    pygame.display.update()

pygame.quit()