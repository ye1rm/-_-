# constants.py
import pygame

# 고정 화면 크기
CELL_SIZE = 20
GRID_WIDTH = 40
GRID_HEIGHT = 40
WIDTH = CELL_SIZE * GRID_WIDTH
HEIGHT = CELL_SIZE * GRID_HEIGHT

# 게임 화면 크기 (실제 게임 영역)
GAME_AREA_WIDTH = WIDTH - 150  # 양 옆 여백
GAME_AREA_HEIGHT = HEIGHT - 150  # 위 아래 여백
game_area_x = (WIDTH - GAME_AREA_WIDTH) // 2
game_area_y = (HEIGHT - GAME_AREA_HEIGHT) // 2

# 색상
BLACK = (0, 0, 0)
TEXT_COLOR = (255, 255, 255) # 흰색
LIGHT_GREEN = pygame.Color("#aad750")
DARK_GREEN = pygame.Color("#a2d148")
YELLOW = pygame.Color("#ffd400")

# 상태 정의
STATE_HOME = "home"
STATE_GAME = "game"
STATE_HOW = "how"


# 텍스트
# 제목
tittle_text = "The Alphabet-Loving Anaconda"
# 게임 이름
Game_text = "TALA"

# 버튼 크기
button_width = 200
button_height = 60