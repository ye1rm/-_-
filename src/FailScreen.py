# FailScreen.py
import pygame
from constants import *

def render_fail_screen(screen, font, score):
    # 검은색 내부 화면 설정
    PADDING = 20  # 여백 크기
    black_surface = pygame.Surface((GAME_AREA_WIDTH - 2 * PADDING - 120, GAME_AREA_HEIGHT - 2 * PADDING - 120))
    black_surface.fill(BLACK)

    # 검은 화면
    pygame.draw.rect(screen, LIGHT_GREEN, (game_area_x, game_area_y, GAME_AREA_WIDTH, GAME_AREA_HEIGHT))
    screen.blit(black_surface, (game_area_x + PADDING + 60, game_area_y + PADDING + 70))

    # 게임 클리어 텍스트
    instructions = [
        "GAME Over",
        f"최종 Score : {score} "
    ]

    # 텍스트를 화면에 렌더링 (중앙에 표시)
    line_height = 80
    y_pos = HEIGHT // 2 - (len(instructions) * line_height) // 2  # 텍스트를 중앙에 배치
    for line in instructions:
        text_surface = font.render(line, True, TEXT_COLOR)  # 지정된 폰트로 렌더링
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y_pos))
        screen.blit(text_surface, text_rect)
        y_pos += line_height

    button_y = y_pos -20
    # 게임 시작 버튼
    start_button_width = 200
    start_button_height = 60
    start_button_rect = pygame.Rect(WIDTH // 2 - start_button_width // 2, button_y + 80, start_button_width, start_button_height)
    pygame.draw.rect(screen, LIGHT_GREEN, start_button_rect)
    start_text = font.render("Game Start", True, TEXT_COLOR)
    start_text_rect = start_text.get_rect(center=start_button_rect.center)
    screen.blit(start_text, start_text_rect)

    return start_button_rect