import random
import sys
from pydoc_data.topics import topics

import pygame.display
from pygame import Rect

from code.Const import COLOR_WHITE, WINDOW_HEIGHT, COLOR_ORANGE, EVENT_ENEMY, SPAWN_TIME
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator


class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        self.timeout = 20000 # 20 seconds

    def run(self):
        pygame.mixer_music.load('./assets/Sounds/Battle Music WAV.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity((choice)))

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout /1000 :.1f}s', COLOR_ORANGE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WINDOW_HEIGHT -35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WINDOW_HEIGHT - 20))
            pygame.display.flip()

            # collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Gentium Book Basic", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)



