#main.py
import pygame
import os
from constants import *
from assets import assets_paths
from game_logic import handle_events
from HomeScreen import render_home_screen
from GameScreen import game_start, get_current_word, draw_random_letters, render_talaconda
from StampScreen import render_stemp_screen
from ClearScreen import render_clear_screen
###############예림##############
from HowScreen import render_how_screen # 추가된 부분
from WordClearScreen import render_word_clear_screen
################################

# 초기화
pygame.init()

# Mixer 초기화
pygame.mixer.init()

# 고정화면 초기화 (프레임 없는 창)
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Fixed Frame TALA Game")

# 고정화면 안에 띄울 게임화면
game_surface = pygame.Surface((GAME_AREA_WIDTH, GAME_AREA_HEIGHT))

# 폰트 로드
font = pygame.font.Font(assets_paths["font"], 24)
game_font = pygame.font.Font(assets_paths["font"], 36)
game_font.set_bold(True)
stamp_font = pygame.font.Font(assets_paths["font"], 17)
stamp_font.set_bold(True)
stamp_level_font = pygame.font.Font(assets_paths["font"], 22)
stamp_level_font.set_bold(True)
word_font = pygame.font.Font(assets_paths["font"], 26)
word_font.set_bold(True)

# BGM 로드
pygame.mixer.music.load(assets_paths["bgm"])
pygame.mixer.music.set_volume(0.5) # 배경음악 볼륨 50%로 설정

pygame.mixer.music.play(-1)
# 초기 상태
current_state = STATE_HOME
running = True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

game_status = True

# 게임 초기 설정
clock = pygame.time.Clock()
letter_positions = [] # 알파벳의 위치를 저장할 리스트
excluded_positions = [] # tala의 위치를 저장할 리스트
score = 0
level = 1
current_word = ""
current_mean = ""
current_index = 0
setWord = ""
maxScore = 0

# tts효과음 전용 채널 생성
effect_channel = pygame.mixer.Channel(1)  # 채널 1번에 tts효과음을 할당

# 스크롤 초기 설정
scroll_y = 0 

next_button_rect = 0

###########예림###############
sound_status = True
##############################
###########태희#############
screen_status = False
############################ 


# 게임 루프
while running:
    for event in pygame.event.get():
        running, current_state, sound_status, screen_status, scroll_y, current_word = handle_events(
            event, current_state, sound_status, screen_status, scroll_y, next_button_rect, current_word
            )
    screen.fill(BLACK)

    if score > maxScore :
        maxScore = score
    # 게임 영역 렌더링
    # 홈
    if current_state == STATE_HOME:

        # 화면에 버튼 그리기
        start_text, start_text_rect, explanation_text, explanation_text_rect, game_text_surface, game_text_rect = render_home_screen(
            screen, font, game_font
        )
        screen.blit(start_text, start_text_rect)
        screen.blit(explanation_text, explanation_text_rect)
        screen.blit(game_text_surface, game_text_rect)

    # 게임
    elif current_state == STATE_GAME:
        if current_word == "":
            current_word, current_mean = get_current_word(level,current_word,current_mean)
            letter_positions.clear()
 
        setWord, current_word, current_index, level, score, current_state = game_start(
            game_surface, current_word, setWord, level, score, letter_positions,excluded_positions, current_index, word_font, current_state
            )  # 게임 실행
        
        clock.tick(FPS)
        
        # 게임 화면을 메인 화면에 렌더링
        screen.blit(game_surface, (game_area_x, game_area_y))  # game_surface를 screen에 복사

        # 고정화면 좌측 상단에 점수와 레벨 표시
        score_surface = font.render(f"Score: {score}", True, TEXT_COLOR)
        level_surface = font.render(f"Level {level} : {current_word}", True, TEXT_COLOR)
        
        # 점수와 레벨을 화면에 출력
        screen.blit(score_surface, (score_x, score_y))  # 점수 출력
        screen.blit(level_surface, (level_x, level_y))  # 레벨과 단어 출력

        # 밑줄 위치 및 길이 계산
        underline_x = (WIDTH - len(current_word) * 50) // 2  # 화면 중앙 하단 시작점
        underline_y = HEIGHT - 20 # 밑줄을 화면 하단에서 약간 위에 출력
        
        # 각 문자의 위치에 맞게 밑줄과 텍스트 렌더링
        for index in range(len(current_word)):
        # 밑줄 그리기
            pygame.draw.line(
                screen,
                TEXT_COLOR,
                (underline_x + index * 50, underline_y),  # 밑줄 시작점
                (underline_x + index * 50 + 40, underline_y),  # 밑줄 끝점
                3  # 선 두께
            )

            # setWord의 각 알파벳 렌더링 - 위에 올리기
            if index in range(len(setWord)):  # setWord에 현재 인덱스에 대응하는 문자가 있는 경우
                char_surface = font.render(setWord[index], True, TEXT_COLOR)
                # 문자가 밑줄 위에 올 수 있도록 렌더링
                screen.blit(
                    char_surface,
                    (underline_x + index * 50 + (40 - char_surface.get_width()) // 2, underline_y - 30)
                )


    ################예림##############
    # 게임 설명 화면 렌더링
    elif current_state == STATE_HOW:
        start_text, start_text_rect = render_how_screen(screen, font)
        screen.blit(start_text, start_text_rect)

    # 도장판 클리어 단어 화면 렌더링
    elif current_state == STATE_WORD_CLEAR:
        start_text, start_text_rect = render_word_clear_screen(screen, font)
        screen.blit(start_text, start_text_rect)
    ##################################

    # 게임 클리어 시.
    elif current_state == STATE_CLEAR:
        button_rect, next_button_rect = render_clear_screen(screen, font, score, current_word, current_mean)
        setWord = ""
        current_index = 0

    # 홈 버튼 생성   
    if current_state != STATE_HOME:
        screen.blit(home_image, (home_x, home_y))
    
    # 도장판
    if current_state == STATE_STAMP:
        render_stemp_screen(game_surface, stamp_font, stamp_level_font, scroll_y)

        # 최고 점수 출력
        maxScore_text_surface = font.render(f"최고 점수: {maxScore}", True, TEXT_COLOR)
        maxScore_text_width, maxScore_text_height = maxScore_text_surface.get_size()
        maxScore_text_x = WIDTH - maxScore_text_width - 20  # 오른쪽에서 20px 간격
        maxScore_text_y = HEIGHT - maxScore_text_height - 20  # 하단에서 20px 간격

        # 고정 화면에 텍스트 출력
        screen.blit(maxScore_text_surface, (maxScore_text_x, maxScore_text_y))
        screen.blit(game_surface, (game_area_x, game_area_y))  # 화면에 렌더링

    # 고정 화면 상단 버튼 출력
    # 엑스 버튼
    screen.blit(close_image, (close_x, close_y))
    ############예림##########
    # 소리 버튼
    if sound_status:
        screen.blit(soundON_image, (sound_x, sound_y))
        pygame.mixer.music.unpause()
    else:
        screen.blit(soundOFF_image, (sound_x, sound_y))
        pygame.mixer.music.pause()
    ###########################
    #########태희##############
    # 화면 버튼
    if screen_status :
        screen.blit(smallScreen_image, (screen_x, screen_y))
    else:
        screen.blit(bigScreen_image, (screen_x, screen_y))
    ###########################
    # 도장판 버튼
    screen.blit(stampBoard_image, (stampBoard_x, stampBoard_y))

    pygame.display.update()

pygame.quit()