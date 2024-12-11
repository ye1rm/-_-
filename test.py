import pygame
import random

# Pygame 초기화
pygame.init()

# 고정 화면 크기
CELL_SIZE = 45
GRID_WIDTH = 20
GRID_HEIGHT = 20
WIDTH = CELL_SIZE * GRID_WIDTH
HEIGHT = CELL_SIZE * GRID_HEIGHT

# 화면 초기화
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Fixed Frame TALA Game")

# 이미지 로드 및 크기 조정
normal_face = pygame.transform.scale(pygame.image.load("C:/Users/user/Desktop/TALA/TALA/assets/Icon/normal_face.png"), (80, 80))
alphabet_face = pygame.transform.scale(pygame.image.load("C:/Users/user/Desktop/TALA/TALA/assets/Icon/alphabet_face.png"), (80, 80))
collision_face = pygame.transform.scale(pygame.image.load("C:/Users/user/Desktop/TALA/TALA/assets/Icon/colllision_face.png"), (80, 80))
body_image = pygame.transform.scale(pygame.image.load("C:/Users/user/Desktop/TALA/TALA/assets/Icon/body.png"), (CELL_SIZE, CELL_SIZE))  # 몸통 이미지 로드 및 크기 조정

# 색상 정의
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 스네이크 초기 설정
snake = [{"x": 5 * CELL_SIZE, "y": 5 * CELL_SIZE}]  # 스네이크 초기 위치
direction = "RIGHT"  # 초기 이동 방향
current_face = normal_face  # 초기 머리 상태

# 먹이 (알파벳) 초기 설정
alphabet = {"x": random.randint(0, GRID_WIDTH - 1) * CELL_SIZE, "y": random.randint(0, GRID_HEIGHT - 1) * CELL_SIZE}

# 점수 및 상태
score = 0

# 폰트 설정
font = pygame.font.Font(None, 36)

# 프레임 속도 설정
clock = pygame.time.Clock()
FPS = 60  # 프레임은 일정하게 유지

# 이동 속도 조정 (시간 기반)
MOVE_DELAY = 200  # 밀리초 단위로 스네이크 이동 간격 설정
last_move_time = pygame.time.get_ticks()  # 마지막으로 이동한 시간 기록

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

# 게임 루프
running = True
while running:
    current_time = pygame.time.get_ticks()  # 현재 시간

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리 (방향 전환)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != "RIGHT":
        direction = "LEFT"
    if keys[pygame.K_RIGHT] and direction != "LEFT":
        direction = "RIGHT"
    if keys[pygame.K_UP] and direction != "DOWN":
        direction = "UP"
    if keys[pygame.K_DOWN] and direction != "UP":
        direction = "DOWN"

    # 스네이크 이동 (시간 기반)
    if current_time - last_move_time > MOVE_DELAY:
        last_move_time = current_time  # 마지막 이동 시간 갱신

        # 머리 이동
        head = snake[0].copy()
        if direction == "LEFT":
            head["x"] -= CELL_SIZE
        if direction == "RIGHT":
            head["x"] += CELL_SIZE
        if direction == "UP":
            head["y"] -= CELL_SIZE
        if direction == "DOWN":
            head["y"] += CELL_SIZE

        # 새로운 머리를 추가
        snake.insert(0, head)

        # 먹이와 충돌 확인
        if head["x"] == alphabet["x"] and head["y"] == alphabet["y"]:
            score += 1
            current_face = alphabet_face  # 얼굴 변경
            alphabet["x"] = random.randint(0, GRID_WIDTH - 1) * CELL_SIZE
            alphabet["y"] = random.randint(0, GRID_HEIGHT - 1) * CELL_SIZE
        else:
            snake.pop()  # 먹이를 먹지 않았으면 꼬리 제거

        # 충돌 판정
        if (
            head["x"] < 0 or head["x"] >= WIDTH or head["y"] < 0 or head["y"] >= HEIGHT
            or head in snake[1:]  # 자기 몸과 충돌
        ):
            current_face = collision_face
            running = False

        # 얼굴 복구
        if current_face != collision_face and current_face != alphabet_face:
            current_face = normal_face

    # 화면 갱신
    screen.fill(WHITE)  # 배경 색상

    # 먹이 그리기
    pygame.draw.rect(screen, GREEN, (alphabet["x"], alphabet["y"], CELL_SIZE, CELL_SIZE))

    # 스네이크 그리기 (머리는 이미지, 몸통도 이미지)
    for i, segment in enumerate(snake):
        if i == 0:  # 머리
            rotated_face = rotate_face(current_face, direction)
            offset = (80 - CELL_SIZE) // 2  # 머리 이미지 위치 조정
            screen.blit(rotated_face, (segment["x"] - offset, segment["y"] - offset))
        else:  # 몸통
            screen.blit(body_image, (segment["x"], segment["y"]))

    # 점수 표시
    score_text = font.render(f"Score: {score}", True, RED)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)  # 프레임 고정
