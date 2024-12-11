# GameScreen.py
import pygame
from assets import assets_paths
from constants import *

# 게임 화면에 그리드 그리기
def draw_grid(game_surface):
    for y in range(GAME_AREA_HEIGHT // CELL_SIZE):
        for x in range(GAME_AREA_WIDTH // CELL_SIZE):
            color = LIGHT_GREEN if (x + y) % 2 == 0 else DARK_GREEN
            pygame.draw.rect(
                game_surface,
                color,
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )


# TALAconda 캐릭터 클래스
class TALAconda:
    def __init__(self):
        # 초기 위치
        self.body = [(5, 5)]  # 머리와 몸의 좌표 리스트 [(x1, y1), (x2, y2), ...]
        self.direction = "RIGHT"  # 초기 방향
        self.next_direction = "RIGHT"  # 다음 이동 방향 (즉시 반대 방향으로 이동 방지)
        self.last_move_time = 0  # 마지막 이동 시간 (게임 시작 시 0)

        # 이미지 로드 및 크기 조정
        original_head = pygame.image.load(assets_paths["normal_face"])  # 원본 머리 이미지
        original_body = pygame.image.load(assets_paths["body"])  # 원본 몸 이미지

        # 격자 크기에 맞게 이미지를 축소
        self.head_image = pygame.transform.scale(original_head, (CELL_SIZE, CELL_SIZE))
        self.body_image = pygame.transform.scale(original_body, (CELL_SIZE, CELL_SIZE))

    # 캐릭터를 화면에 렌더링
    def render(self, game_surface):
        # 머리 렌더링
        head_x, head_y = self.body[0]  # 머리의 좌표
        rotated_head = self.rotate_head_image()  # 방향에 맞게 머리 회전
        game_surface.blit(rotated_head, (head_x * CELL_SIZE, head_y * CELL_SIZE))

        # 몸 렌더링
        for segment in self.body[1:]:
            segment_x, segment_y = segment
            game_surface.blit(self.body_image, (segment_x * CELL_SIZE, segment_y * CELL_SIZE))

    # 머리 회전
    def rotate_head_image(self):
        # 방향에 따라 머리 이미지를 회전
        if self.direction == "UP":
            return pygame.transform.rotate(self.head_image, 90)
        elif self.direction == "DOWN":
            return pygame.transform.rotate(self.head_image, -90)
        elif self.direction == "LEFT":
            return pygame.transform.rotate(self.head_image, 180)
        elif self.direction == "RIGHT":
            return self.head_image

    # 방향 설정
    def set_direction(self, new_direction):
        # 현재 진행 방향의 반대 방향으로는 이동하지 않음
        opposites = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if new_direction != opposites.get(self.direction):
            self.next_direction = new_direction  # 새로운 방향 설정

    # 캐릭터 이동
    def move(self, current_time):
        MOVE_DELAY = 300  # 밀리초 단위로 스네이크 이동 간격 설정 (속도 조정)

        # 시간 기반 이동 처리
        if current_time - self.last_move_time > MOVE_DELAY:
            self.direction = self.next_direction  # 방향을 업데이트

            head_x, head_y = self.body[0]  # 현재 머리 위치

            # 새로운 머리 위치 계산
            if self.direction == "UP":
                head_y -= 1
            elif self.direction == "DOWN":
                head_y += 1
            elif self.direction == "LEFT":
                head_x -= 1
            elif self.direction == "RIGHT":
                head_x += 1
            
            # 화면 경계를 넘지 않도록 처리
            max_x = GAME_AREA_WIDTH // CELL_SIZE - 1
            max_y = GAME_AREA_HEIGHT // CELL_SIZE - 1

            head_x = max(0, min(head_x, max_x))
            head_y = max(0, min(head_y, max_y))

            # 새로운 머리 위치 추가
            self.body = [(head_x, head_y)] + self.body[:-1]  # 머리를 추가하고 마지막 부분은 삭제

            self.last_move_time = current_time  # 마지막 이동 시간 갱신


# 게임 화면에 캐릭터 추가
def draw_character(game_surface, character, events):
    # 현재 시간
    current_time = pygame.time.get_ticks()

    # 키보드 이벤트 처리
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                character.set_direction("UP")
            elif event.key == pygame.K_DOWN:
                character.set_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                character.set_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                character.set_direction("RIGHT")

    # 스네이크 이동
    character.move(current_time)

    # 캐릭터 그리기
    character.render(game_surface)