# C
import pygame

COLOR_ORANGE = (209, 72, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (227, 219, 25)

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENEMY_Y_START = 250
ENEMY_Y_END = 500

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Player' : 4,
    'Enemy1' : 2,
    'Enemy2' : 3,
}

# M
MENU_OPTION = ('NEW GAME', 'SCORE', 'EXIT')

# S
SPAWN_TIME = 2000

# W
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600