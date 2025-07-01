# C
import pygame

C_ORANGE = (209, 72, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (227, 219, 25)
C_BLUE = (0, 0, 128)
C_CYAN = (0,128, 128)

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
    'Player': 2000,
    'PlayerShot': 25,
    'Enemy1': 75,
    'Enemy2': 50,
}

ENTITY_SHOT_DELAY = {
    'Player': 20,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Player': 1,
    'PlayerShot': 25,
    'Enemy1': 25,
    'Enemy2': 25,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Player': 0,
    'PlayerShot': 0,
    'Enemy1': 100,
    'Enemy2': 100,
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