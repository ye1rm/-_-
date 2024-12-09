import pygame
from constants import *

def render_how_screen(screen, font):
    # 화면 배경 색상 설정
    screen.fill(BLACK)

    # 게임 설명 텍스트
    instructions = [
        "방향키로 아나콘다 TALA를 조종하여",
        "오른쪽 상단에 제시된 단어의 스펠링 순으로 알파벳을 획득하세요!!",
        "스펠링 순서와 다른 알파벳을 먹는다면",
        "해당 레벨이 초기화 되어 재시작 되니 주의해 주세용~!",
        "벽이나 TALA의 몸통 혹은 꼬리에 부딪히면 완전히 GAME OVER!",
        "Level 5 까지 클리어 할 경우",
        "다시 Level 1 부터 시작되어 계속해서 Score를 올릴 수 있어요!",
        "클리어한 단어들은 도장판에 칭찬도장이 꽝!",
        "도장판을 도장으로 전부 채워보세요!",
        "도장판에서 클리어한 단어의 뜻과 발음을 다시 보고 들을 수 있어요!",
        "도장판의 단어로 게임을 시작할 수 있어요!"
    ]

    # 각 줄의 텍스트를 화면에 렌더링
    line_height = 40
    y_pos = HEIGHT // 6  # 텍스트 시작 Y 위치
    for line in instructions:
        text_surface = font.render(line, True, TEXT_COLOR)  # 지정된 폰트로 렌더링
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y_pos))
        screen.blit(text_surface, text_rect)
        y_pos += line_height

    # 게임 시작 버튼 
    pygame.draw.rect(screen, LIGHT_GREEN, (start_button_x, start_button_y+150, button_width, button_height))
    start_text = font.render("Game Start", True, TEXT_COLOR)
    start_text_rect = start_text.get_rect(center=(start_button_x + button_width // 2, start_button_y+150 + button_height // 2))

    return start_text, start_text_rect
