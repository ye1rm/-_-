#game_logic.py
import pygame
from constants import *
from gtts import gTTS
import os

def handle_events(event, current_state, sound_status, screen_status, scroll_y, next_button_rect, current_word, button_rect):
    if event.type == pygame.QUIT:
        return False, current_state, sound_status, screen_status, scroll_y, current_word
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # 엑스 버튼 클릭 시 종료
        if close_x <= mouse_x <= close_x + close_width and close_y <= mouse_y <= close_y + close_height:
            return False, current_state, sound_status, screen_status, scroll_y, current_word
        
        # 홈 버튼 클릭 시 
        if home_x <= mouse_x <= home_x + home_width and home_y <= mouse_y <= home_y + home_height:
            current_state = STATE_HOME # 상태를 홈으로 변경

        ############예림#############################
        # 소리 버튼 클릭 시 소리 상태 변경
        if sound_x <= mouse_x <= sound_x + soundON_width and sound_y <= mouse_y <= sound_y + soundON_height:
            sound_status = not sound_status  # 소리 상태를 반전시킴 (True -> false, false -> True)
        #############################################

        #############태희############################
        if screen_x <= mouse_x <= screen_x + bigScreen_width and screen_y <= mouse_y <= screen_y + bigScreen_height:
            screen_status = not screen_status
        #############################################

        # 도장판 버튼 클릭 시
        if stampBoard_x <= mouse_x <= stampBoard_x + stampBoard_width and stampBoard_y <= mouse_y <= stampBoard_y + stampBoard_height:
            current_state = STATE_STAMP # 상태를 도장으로 변경
        
        if current_state == STATE_HOME:  # HOME 상태일 때
            # "게임 시작" 버튼 클릭
            if start_button_x <= mouse_x <= start_button_x + button_width and start_button_y <= mouse_y <= start_button_y + button_height:
                current_state = STATE_GAME  # 상태를 게임으로 변경
            # "게임 설명" 버튼 클릭
            elif start_button_x <= mouse_x <= start_button_x + button_width and explanation_button_y <= mouse_y <= explanation_button_y + button_height:
                current_state = STATE_HOW  # 상태를 설명으로 변경
        
        if current_state == STATE_HOW:  # HOW 상태일 때
            # 게임 시작 버튼 클릭 시
            if start_button_x <= mouse_x <= start_button_x + button_width and start_button_y+150 <= mouse_y <= start_button_y+150 + button_height:
                current_state = STATE_GAME  # 상태를 게임으로 변경

        if current_state == STATE_CLEAR:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # next 버튼 클릭 시 다음 단어로 진행
                if next_button_rect.collidepoint(event.pos):
                    current_word = ""
                    current_state = STATE_GAME
                if button_rect.collidepoint(event.pos): # 발음 재생 버튼 클릭 시
                    # TTS 기능
                    tts = gTTS(text=current_word, lang='en')  # 영어로 음성 생성
                    tts.save("tts.mp3")
                    try:
                        sound = pygame.mixer.Sound("tts.mp3")
                        sound.play()

                        # 음성이 재생되는 동안 기다림
                        while pygame.mixer.get_busy():
                            pygame.time.Clock().tick(FPS)
            
                    finally:
                        os.remove("tts.mp3")  # 음성 파일 삭제 (재생이 끝난 후)

        if current_state == STATE_STAMP: # STAMP 상태일 때
            # 마우스 휠을 사용한 스크롤
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # 휠 위로
                    scroll_y -= 15
                    print(f"Scroll Up: {scroll_y}")
                elif event.button == 5:  # 휠 아래로
                    scroll_y += 15
                    print(f"Scroll Down: {scroll_y}")
            # 마우스 드래그로 스크롤
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:  # 왼쪽 마우스 버튼 눌렸을 때
                    scroll_y += event.rel[1]  # 마우스의 수직 이동량만큼 스크롤

            # 스크롤 범위 제한
            scroll_y = max(scroll_y, 0)  # 화면 상단 고정
            scroll_y = min(scroll_y, 400)  # 화면 하단 고정 

    return True, current_state, sound_status, screen_status, scroll_y, current_word