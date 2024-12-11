from constants import *
from LevelWords import *

# 레벨별 버튼 그리기
def draw_level_buttons(surface, level_words, level_start_x, level_start_y, font):
    button_radius = 40  # 동그라미 버튼의 반지름
    offset_x = 40  # 버튼 사이의 X 간격
    offset_y = 40  # 버튼 사이의 Y 간격

    for index, (word, _) in enumerate(level_words):
        # 버튼 위치 계산
        row = index // 5  # 한 줄에 5개의 단어
        col = index % 5
        x = level_start_x + col * (button_radius * 2 + offset_x)
        y = level_start_y + row * (button_radius * 2 + offset_y)

        # 동그라미 버튼 그리기
        pygame.draw.circle(surface, TEXT_COLOR, (x, y), button_radius)
        pygame.draw.circle(surface, TEXT_COLOR, (x, y), button_radius, 2)

        # 단어 텍스트 렌더링
        word_surface = font.render(word.capitalize(), True, BLACK)
        word_width, word_height = word_surface.get_size()
        surface.blit(
            word_surface,
            (x - word_width // 2, y - word_height // 2)
        )

# 도장판 화면을 그리기 위한 함수
def render_stemp_screen(surface, stamp_font, font, scroll_y):
    surface.fill(LIGHT_GREEN)  # 배경 색상 설정
    font.set_bold(True)

    # 레벨별 텍스트 렌더링 함수
    def render_level_text(level_number, x, y):
        level_text = f"Level {level_number}"
        level_surface = font.render(level_text, True, TEXT_COLOR)
        surface.blit(level_surface, (x, y))

    # Level 1
    level_start_x = 135
    level_start_y = 50 - scroll_y  # 스크롤에 맞게 Y 위치 조정
    render_level_text(1, level_start_x - 60, level_start_y - 15)  
    draw_level_buttons(surface, level_1_words, level_start_x, level_start_y + 60, stamp_font)

    # Level 2
    level_start_y += 260  # LEVEL 1과 LEVEL 2 사이의 간격
    render_level_text(2, level_start_x - 60, level_start_y - 15)  
    draw_level_buttons(surface, level_2_words, level_start_x, level_start_y + 60, stamp_font)

    # Level 3
    level_start_y += 260  # LEVEL 2와 LEVEL 3 사이의 간격
    render_level_text(3, level_start_x - 60, level_start_y - 15)  
    draw_level_buttons(surface, level_3_words, level_start_x, level_start_y + 60, stamp_font)

    # Level 4
    level_start_y += 260  # LEVEL 3과 LEVEL 4 사이의 간격
    render_level_text(4, level_start_x - 60, level_start_y - 15)  
    draw_level_buttons(surface, level_4_words, level_start_x, level_start_y + 60, stamp_font)
    