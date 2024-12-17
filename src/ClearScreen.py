#ClearScreen.py
import pygame
from constants import *

def render_clear_screen(screen, font, score, current_word, current_mean):
    # 검은색 내부 화면 설정
    PADDING = 20  # 여백 크기
    black_surface = pygame.Surface((GAME_AREA_WIDTH - 2 * PADDING - 120, GAME_AREA_HEIGHT - 2 * PADDING - 120))
    black_surface.fill(BLACK)

    # 검은 화면
    pygame.draw.rect(screen, LIGHT_GREEN, (game_area_x, game_area_y, GAME_AREA_WIDTH, GAME_AREA_HEIGHT))
    screen.blit(black_surface, (game_area_x + PADDING + 60, game_area_y + PADDING + 70))

    # 게임 클리어 텍스트
    instructions = [
        "GAME CLEAR",
        f"현재 Score : {score} ",
        f"{current_word}",
        f"뜻 : {current_mean}"
    ]

    # 텍스트를 화면에 렌더링 (중앙에 표시)
    line_height = 80
    y_pos = HEIGHT // 2 - (len(instructions) * line_height) // 2  # 텍스트를 중앙에 배치
    for line in instructions:
        text_surface = font.render(line, True, TEXT_COLOR)  # 지정된 폰트로 렌더링
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y_pos))
        screen.blit(text_surface, text_rect)
        y_pos += line_height

    # 발음 재생 버튼 (텍스트와 아이콘 함께 표시)
    button_width = 300
    button_height = 60
    button_x = WIDTH // 2 - button_width // 2
    button_y = y_pos + 20
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    pygame.draw.rect(screen, LIGHT_GREEN, button_rect)

    # 텍스트 그리기
    voice_text = font.render("발음 재생", True, TEXT_COLOR)
    voice_text_rect = voice_text.get_rect(midleft=(button_x + 20, button_y + button_height // 2))
    screen.blit(voice_text, voice_text_rect)

    # 아이콘 그리기 (스피커 이모지)
    voice_image_rect = voice_image.get_rect(midright=(button_x + button_width - 20, button_y + button_height // 2))
    screen.blit(voice_image, voice_image_rect)

    # 다음 게임 버튼
    next_button_width = 200
    next_button_height = 60
    next_button_rect = pygame.Rect(WIDTH // 2 - next_button_width // 2, button_y + 80, next_button_width, next_button_height)
    pygame.draw.rect(screen, LIGHT_GREEN, next_button_rect)
    next_text = font.render("NEXT GAME", True, TEXT_COLOR)
    next_text_rect = next_text.get_rect(center=next_button_rect.center)
    screen.blit(next_text, next_text_rect)

    return button_rect, next_button_rect