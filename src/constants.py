# constants.py
import pygame
from assets import load_and_scale_image, assets_paths

# 고정 화면 크기
CELL_SIZE = 45
GRID_WIDTH = 20
GRID_HEIGHT = 20
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

# 화면 상태 정의
STATE_HOME = "home"
STATE_GAME = "game"
STATE_HOW = "how"
STATE_STAMP = "stamp"
STATE_FAIL = "fail"
STATE_CLEAR = "clear"
STATE_WORD_CLEAR = "wordClear"
STATE_WORD = "word"


# 텍스트
# 제목
tittle_text = "The Alphabet-Loving Anaconda"
# 게임 이름
Game_text = "TALA"

# 버튼 크기
button_width = 200
button_height = 60

# 스케일링된 이미지와 그 이미지의 새 너비, 높이 값
# 엑스
close_image, close_width, close_height = load_and_scale_image(assets_paths["close"], 0.05)
# 소리 ON
soundON_image, soundON_width, soundON_height = load_and_scale_image(assets_paths["soundON"], 0.07)
# 소리 OFF
soundOFF_image, soundOFF_width, soundOFF_height = load_and_scale_image(assets_paths["soundOFF"], 0.07)
# 화면 확대
bigScreen_image, bigScreen_width, bigScreen_height = load_and_scale_image(assets_paths["bigScreen"], 0.05)
# 화면 축소
smallScreen_image, smallScreen_width, smallScreen_height = load_and_scale_image(assets_paths["smallScreen"], 0.05)
# 도장판
stampBoard_image, stampBoard_width, stampBoard_height = load_and_scale_image(assets_paths["stampBoard"], 0.06)
# 홈
home_image, home_width, home_height = load_and_scale_image(assets_paths["home"], 0.07)
# 음성 지원
voice_image, voice_width, voice_height = load_and_scale_image(assets_paths["voice"], 0.07)

# 버튼 위치
# 엑스 버튼 위치 (고정 화면 상단 우측)
close_x = WIDTH - close_width - 10
close_y = 10
# 소리 버튼 위치 (엑스 버튼 왼쪽)
sound_x = close_x - soundON_width - 10
sound_y = close_y + (close_height - soundON_height) // 2  # 높이 조정
# 화면 버튼 위치 (소리 버튼 왼쪽)
screen_x = sound_x - bigScreen_width - 10
screen_y = 10
# 도장판 버튼 위치 (화면 버튼 왼쪽)
stampBoard_x = screen_x - stampBoard_width - 10
stampBoard_y = close_y + (close_height - stampBoard_height) // 2
# 홈 버튼 위치 (고정 화면 왼쪽 하단)
home_x = 10
home_y = HEIGHT - home_height - 10
# 시작 버튼 위치 (게임 화면 중앙 하단)
start_button_x = game_area_x + (GAME_AREA_WIDTH - button_width) // 2
start_button_y = game_area_y + GAME_AREA_HEIGHT // 2 + 50
# 설명 버튼 위치
explanation_button_y = start_button_y + button_height + 20
