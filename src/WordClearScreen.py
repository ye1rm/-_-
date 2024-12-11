#WordClearScreen.py
import pygame
from constants import *


def render_word_clear_screen(screen, font):

    # 검은색 내부 화면 설정
    PADDING = 20  # 여백 크기
    black_surface = pygame.Surface((GAME_AREA_WIDTH - 2 * PADDING, GAME_AREA_HEIGHT - 2 * PADDING))
    black_surface.fill(BLACK)

    # 검은 화면
    pygame.draw.rect(screen, BLACK, (game_area_x, game_area_y, GAME_AREA_WIDTH, GAME_AREA_HEIGHT))
    screen.blit(black_surface, (game_area_x + PADDING, game_area_y + PADDING))

    # 게임 클리어 텍스트
    instructions = [
        "GAME CLEAR!"
    ]

    # 텍스트를 화면에 렌더링
    line_height = 150
    y_pos = HEIGHT // 4  # 텍스트 시작 Y 위치
    for line in instructions:
        text_surface = font.render(line, True, TEXT_COLOR)  # 지정된 폰트로 렌더링
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y_pos))
        screen.blit(text_surface, text_rect)
        y_pos += line_height

    # 게임 시작 버튼 
    pygame.draw.rect(screen, LIGHT_GREEN, (start_button_x, start_button_y+170, button_width, button_height))
    start_text = font.render("Game Start", True, TEXT_COLOR)
    start_text_rect = start_text.get_rect(center=(start_button_x + button_width // 2, start_button_y+170 + button_height // 2))

    return start_text, start_text_rect
