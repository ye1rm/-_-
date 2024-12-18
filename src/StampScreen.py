from constants import *
from LevelWords import *

# 레벨별 버튼 그리기
def draw_level_buttons(surface, level_words, level_start_x, level_start_y, font, clear_words):
    button_radius = 50  # 동그라미 버튼의 반지름
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

        # 클리어한 단어에 칭찬 도장 표시
        if word in clear_words:
            # 칭찬 도장 이미지를 버튼 중앙에 올리기
            stamp_x = x - stamp_width // 2
            stamp_y = y - stamp_height // 2
            surface.blit(stamp_image, (stamp_x, stamp_y))  # 도장 이미지를 버튼 위에 그리기


# 도장판 화면을 그리기 위한 함수
def render_stemp_screen(surface, stamp_font, font, scroll_y, current_words):
    surface.fill(LIGHT_GREEN)  # 배경 색상 설정
    font.set_bold(True)

    # 레벨별 텍스트 렌더링 함수
    def render_level_text(level_number, x, y):
        level_text = f"Level {level_number}"
        level_surface = font.render(level_text, True, TEXT_COLOR)
        surface.blit(level_surface, (x, y))

    # Level 1
    level_start_x = 140
    level_start_y = 50 - scroll_y  # 스크롤에 맞게 Y 위치 조정
    render_level_text(1, level_start_x - 60, level_start_y - 30)  
    draw_level_buttons(surface, level_1_words, level_start_x, level_start_y + 60, stamp_font, current_words)

    # Level 2
    level_start_y += 300  # LEVEL 1과 LEVEL 2 사이의 간격
    render_level_text(2, level_start_x - 60, level_start_y - 30)  
    draw_level_buttons(surface, level_2_words, level_start_x, level_start_y + 60, stamp_font, current_words)

    # Level 3
    level_start_y += 300  # LEVEL 2와 LEVEL 3 사이의 간격
    render_level_text(3, level_start_x - 60, level_start_y - 30)  
    draw_level_buttons(surface, level_3_words, level_start_x, level_start_y + 60, stamp_font, current_words)

    # Level 4
    level_start_y += 300  # LEVEL 3과 LEVEL 4 사이의 간격
    render_level_text(4, level_start_x - 60, level_start_y - 30)  
    draw_level_buttons(surface, level_4_words, level_start_x, level_start_y + 60, stamp_font, current_words)
    

        # if event.type == pygame.MOUSEBUTTONDOWN:
        # mouse_x, mouse_y = pygame.mouse.get_pos()
        # for button in level_buttons:
        #     x, y, radius, word = button
        #     # 클릭된 버튼이 있는지 확인
        #     if (mouse_x - x) ** 2 + (mouse_y - y) ** 2 <= radius ** 2:
        #         print(f"클릭된 단어: {word}")  # 클릭된 단어를 출력 (여기서 원하는 처리를 할 수 있음)
        #         # 클릭된 단어에 대한 처리를 추가할 수 있음