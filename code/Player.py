import pygame.key

from code.Const import ENTITY_SPEED, WINDOW_HEIGHT
from code.Entity import Entity

class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 200:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < 520:
            self.rect.centery += ENTITY_SPEED[self.name]
        pass
