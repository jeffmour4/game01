import random

from code.Background import Background
from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT, ENEMY_Y_START, ENEMY_Y_END
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                list_bg.append(Background(f'Level1Bg0', (0, 0)))
                for i in range(3):
                    if i > 0:
                        list_bg.append(Background(f'Level1Bg{i}', (0,-95)))
                        list_bg.append(Background(f'Level1Bg{i}', (WINDOW_WIDTH, -95)))
                return list_bg
            case 'Player':
                return Player('Player', (10, WINDOW_HEIGHT/2))
            case 'Enemy1':
                return Enemy('Enemy1', (WINDOW_WIDTH + 10, random.randint(ENEMY_Y_START, ENEMY_Y_END)))
            case 'Enemy2':
                return Enemy('Enemy2', (WINDOW_WIDTH + 10, random.randint(ENEMY_Y_START, ENEMY_Y_END)))