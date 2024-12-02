# pip install pygame
# pip install gtts

import pygame

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("알파벳을 사랑한 아나콘다")

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # 배경 흰색
    pygame.display.flip()

pygame.quit()
