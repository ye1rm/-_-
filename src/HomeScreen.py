# HomeScreen.py
import pygame
from constants import *

def render_home_screen(screen, font, game_font):
    # 게임 화면 영역
    pygame.draw.rect(screen, BLACK, (game_area_x, game_area_y, GAME_AREA_WIDTH, GAME_AREA_HEIGHT))

    # 게임 시작 버튼
    pygame.draw.rect(screen, LIGHT_GREEN, (start_button_x, start_button_y, button_width, button_height))
    start_text = font.render("Game Start", True, TEXT_COLOR)
    start_text_rect = start_text.get_rect(center=(start_button_x + button_width // 2, start_button_y + button_height // 2))

    # 게임 설명 버튼
    pygame.draw.rect(screen, DARK_GREEN, (start_button_x, explanation_button_y, button_width, button_height))
    explanation_text = font.render("게임 설명", True, TEXT_COLOR)
    explanation_text_rect = explanation_text.get_rect(center=(start_button_x + button_width // 2, explanation_button_y + button_height // 2))

    # 게임 제목 텍스트 렌더링
    x_pos = WIDTH // 4
    for char in tittle_text:
        char_surface = font.render(char, True, YELLOW if char.isupper() else TEXT_COLOR)
        screen.blit(char_surface, (x_pos, HEIGHT // 4))
        x_pos += char_surface.get_width()

    # 게임 이름 텍스트 렌더링
    game_text_surface = game_font.render(Game_text, True, YELLOW)
    game_text_rect = game_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))

    return start_text, start_text_rect, explanation_text, explanation_text_rect, game_text_surface, game_text_rect

def draw_grid(game_surface):
    for y in range(GAME_AREA_HEIGHT // CELL_SIZE):
        for x in range(GAME_AREA_WIDTH//CELL_SIZE):
            color = LIGHT_GREEN if (x + y) % 2 == 0 else DARK_GREEN
            pygame.draw.rect(
                game_surface,
                color,
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )