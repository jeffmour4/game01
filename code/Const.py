# C
import pygame

COLOR_ORANGE = (209, 72, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (227, 219, 25)

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENEMY_Y_START = 200
ENEMY_Y_END = 500

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Player' : 4,
    'Enemy1' : 2,
    'Enemy2' : 3,
    'PlayerShot' : 7,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Player': 300,
    'PlayerShot': 25,
    'Enemy1': 75,
    'Enemy2': 50,
}

ENTITY_SHOT_DELAY = {
    'Player': 20,
}

# M
MENU_OPTION = ('NEW GAME', 'SCORE', 'EXIT')

# P
PLAYER_KEY_SHOOT = {
    'Player': pygame.K_LCTRL
}

# S
SPAWN_TIME = 2000

# W
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600