# GameScreen.py
import pygame
from constants import *

# TALAconda 초기 설정
talaconda = [{"x": 5 * CELL_SIZE, "y": 5 * CELL_SIZE}] # 초기 위치
current_face = normal_face_image
direction = "RIGHT"

last_move_time = 0

# 게임 화면에 그리드 그리기
def draw_grid(game_surface):
    for y in range(GAME_AREA_HEIGHT // CELL_SIZE + 1):
        for x in range(GAME_AREA_WIDTH // CELL_SIZE + 1):
            color = LIGHT_GREEN if (x + y) % 2 == 0 else DARK_GREEN
            pygame.draw.rect(
                game_surface,
                color,
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

# 방향 회전 함수
def rotate_face(face, direction):
    if direction == "UP":
        return pygame.transform.rotate(face, 90)
    elif direction == "DOWN":
        return pygame.transform.rotate(face, -90)
    elif direction == "LEFT":
        return pygame.transform.rotate(face, 180)
    else:  # RIGHT
        return face

# 스네이크 이동
def move(talaconda, direction):
    # 머리 이동
    head = talaconda[0].copy()
    if direction == "LEFT":
        head["x"] -= CELL_SIZE
    if direction == "RIGHT":
        head["x"] += CELL_SIZE
    if direction == "UP":
        head["y"] -= CELL_SIZE
    if direction == "DOWN":
        head["y"] += CELL_SIZE
    
    # 새로운 머리 추가
    talaconda.insert(0, head)
    talaconda.pop()

def render_talaconda(game_surface, talaconda, current_face, direction):
    for i, segment in enumerate(talaconda):
        if i == 0:  # 머리
            rotated_face = rotate_face(current_face, direction)
            offset = (CELL_SIZE) # 머리 이미지 위치 조정
            game_surface.blit(rotated_face, (segment["x"] - offset, segment["y"] - offset))
        else:  # 몸통
            game_surface.blit(body_image, (segment["x"], segment["y"]))

# 게임 화면에 캐릭터 추가
def game_start(game_surface):
    current_time = pygame.time.get_ticks() # 현재 시간

    global last_move_time
    global direction
    global current_face

    draw_grid(game_surface)

    # 키보드 입력 처리 (방향 전환)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != "RIGHT":
        direction = "LEFT"
    if keys[pygame.K_RIGHT] and direction != "LEFT":
        direction = "RIGHT"
    if keys[pygame.K_UP] and direction != "DOWN":
        direction = "UP"
    if keys[pygame.K_DOWN] and direction != "UP":
        direction = "DOWN"

    # 스네이크 이동
    if current_time - last_move_time > MOVE_DELAY:
        last_move_time = current_time
        move(talaconda, direction)

    # 캐릭터 그리기
    render_talaconda(game_surface, talaconda, current_face, direction)

