import pygame

def handle_events(event, current_state, close_x, close_y, close_width, close_height):
    if event.type == pygame.QUIT:
        return False, current_state
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if close_x <= mouse_x <= close_x + close_width and close_y <= mouse_y <= close_y + close_height:
            return False, current_state
        if current_state == "home":
            # 버튼 클릭 처리 (예: 시작 버튼, 설명 버튼)
            pass
    return True, current_state