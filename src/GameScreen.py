# GameScreen.py
from constants import*

def draw_grid(game_surface):
    for y in range(GAME_AREA_HEIGHT // CELL_SIZE):
        for x in range(GAME_AREA_WIDTH//CELL_SIZE):
            color = LIGHT_GREEN if (x + y) % 2 == 0 else DARK_GREEN
            pygame.draw.rect(
                game_surface,
                color,
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )