# GameScreen.py
import pygame
import random
import string
from constants import *
from LevelWords import *

# TALAconda 초기 설정
talaconda = [{"x": 5 * CELL_SIZE, "y": 5 * CELL_SIZE}] # 초기 위치
current_face = normal_face_image
direction = "RIGHT"

getWord = ""

last_move_time = 0
collision = False
levelScore = 0

letter_positions = [] # 알파벳의 위치를 저장할 리스트
excluded_positions = [] # tala의 위치를 저장할 리스트

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
    global collision
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

    if collision == False:
        talaconda.pop()

def render_talaconda(game_surface):
    global talaconda
    global current_face
    global direction

    for i, segment in enumerate(talaconda):
        if i == 0:  # 머리
            rotated_face = rotate_face(current_face, direction)
            game_surface.blit(rotated_face, (segment["x"], segment["y"]))
        else:  # 몸통
            game_surface.blit(body_image, (segment["x"], segment["y"]))

def get_current_word(level):
    # level 값에 따라 단어 리스트 선택
    if level == 1:
        current_word = random.choice(level_1_words)[0]  # 영단어만 선택
    elif level == 2:
        current_word = random.choice(level_2_words)[0]
    elif level == 3:
        current_word = random.choice(level_3_words)[0]
    elif level == 4:
        current_word = random.choice(level_4_words)[0]
    return current_word 

# 랜덤한 알파벳 생성 (a부터 z까지 중에서 3개 선택)
def generate_random_letters(num):
    return [random.choice(string.ascii_lowercase) for _ in range(num)]

# 게임 화면에 랜덤 문자 배치
def draw_random_letters(game_surface, font, current_word, current_index, letter_positions, excluded_positions):
    # 이미 알파벳이 배치된 위치를 추적하기 위한 집합(set)
    used_positions = set()

    # "tala"의 머리 및 몸통 위치를 excluded_positions에 추가
    for segment in talaconda:
        head_position = (segment["x"], segment["y"])
        excluded_positions.append(head_position)

    if not letter_positions:  # 새로운 알파벳을 생성
        random_letters = generate_random_letters(3)  # 랜덤으로 알파벳 3개 생성
        all_letters = [current_word[current_index]] + random_letters  # 현재 단어의 i번째 글자 + 랜덤 알파벳

        # 각 알파벳을 랜덤한 위치에 배치
        for letter in all_letters:
            while True:
                # 랜덤 위치 계산 (중복 및 제외된 위치를 피함)
                x = random.randint(0, GAME_AREA_WIDTH // CELL_SIZE - 1) * CELL_SIZE
                y = random.randint(0, GAME_AREA_HEIGHT // CELL_SIZE - 1) * CELL_SIZE
                position = (x, y)

                # 제외된 위치와 중복되지 않으면 위치를 사용
                if position not in used_positions and position not in excluded_positions:
                    letter_positions.append((letter, x, y))  # 알파벳과 위치 저장
                    used_positions.add(position)
                    break  # 중복되지 않는 위치를 찾으면 루프 종료

    # 기존의 알파벳 위치에 그리기
    for letter, x, y in letter_positions:
        # 셀의 중앙 좌표 계산
        center_x = x + CELL_SIZE // 2
        center_y = y + CELL_SIZE // 2

        # 동그라미 배경 그리기
        pygame.draw.circle(game_surface, BTN_COLOR, (center_x , center_y), CELL_SIZE // 2)

        # 알파벳을 셀 가운데에 위치시키기
        letter_surface = font.render(letter, True, TEXT_COLOR)  # 알파벳 렌더링
        x_centered = center_x - letter_surface.get_width() // 2
        y_centered = center_y - letter_surface.get_height() // 2

        # 알파벳을 배경 중앙에 그리기
        game_surface.blit(letter_surface, (x_centered, y_centered))

def check_collision_with_buttons(game_surface, font, letter_positions, current_word, score, setWord, current_index):
    global talaconda
    global getWord
    global levelScore

    head = talaconda[0]
    head_rect = pygame.Rect(head["x"], head["y"], CELL_SIZE, CELL_SIZE)  # 타라콘다 머리를 Rect로 감쌈
    # letter_positions에서 충돌한 알파벳을 찾아 처리
    for i, (letter, x, y) in enumerate(letter_positions):
        letter_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

        if head_rect.colliderect(letter_rect): # 머리와 버튼 위치 비교
            if letter == current_word[current_index]:  # 현재 단어의 i번째 글자와 일치하면
                setWord += letter  # setWord에도 추가 (맞춘 글자 누적)
                score += 1  # 점수 증가
                current_index += 1  # 다음 글자로 이동
                letter_positions.clear()
                if current_index < len(current_word):
                    draw_random_letters(game_surface, font, current_word, current_index, letter_positions, excluded_positions)
                return True, score, setWord, current_index  # 충돌 성공 반환
            else:
                setWord = ""
                score = levelScore
                current_index = 0
                letter_positions.clear()
                draw_random_letters(game_surface, font, current_word, current_index, letter_positions, excluded_positions)

    return False, score, setWord, current_index  # 충돌하지 않은 경우


# 게임 시작
def game_start(game_surface, current_word, setWord, level, score, letter_positions, current_index, font):
    draw_grid(game_surface)
    current_time = pygame.time.get_ticks()

    global last_move_time
    global direction
    global current_face
    global levelScore

    # 방향 전환 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != "RIGHT":
        direction = "LEFT"
    if keys[pygame.K_RIGHT] and direction != "LEFT":
        direction = "RIGHT"
    if keys[pygame.K_UP] and direction != "DOWN":
        direction = "UP"
    if keys[pygame.K_DOWN] and direction != "UP":
        direction = "DOWN"

    # 충돌 처리
    collision, score, setWord, current_index = check_collision_with_buttons(
        game_surface, font, letter_positions, current_word, score, setWord, current_index
    )

    # 충돌 후 알파벳 및 상태 갱신
    if collision:
        if current_word == setWord:  # 모든 글자를 맞춘 경우
            current_index = 0  # 인덱스 초기화
            level += 1
            levelScore = score
            current_word = get_current_word(level)  # 다음 단어 가져오기
            setWord = ""

    # 스네이크 이동
    if current_time - last_move_time > MOVE_DELAY:
        last_move_time = current_time
        move(talaconda, direction)
    
    draw_grid(game_surface)

    return setWord, current_word, current_index, level, score



