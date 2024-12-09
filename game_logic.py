#game_logic.py
import pygame
from constants import *

def handle_events(event, current_state, sound_status, screen_status):
    if event.type == pygame.QUIT:
        return False, current_state, sound_status
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # 엑스 버튼 클릭 시 종료
        if close_x <= mouse_x <= close_x + close_width and close_y <= mouse_y <= close_y + close_height:
            return False, current_state, sound_status
        
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

    return True, current_state, sound_status, screen_status