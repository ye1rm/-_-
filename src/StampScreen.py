from constants import*

# StampScreen.py
def render_stemp_screen(screen, font, maxScore):
    # 게임 화면 영역
    pygame.draw.rect(screen, BLACK, (game_area_x, game_area_y, GAME_AREA_WIDTH, GAME_AREA_HEIGHT))

    maxScore_text_surface = font.render("최고 점수 : ", True, TEXT_COLOR)