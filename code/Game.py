import pygame

from code.Level import Level
from code.Menu import Menu
from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTION


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level1')
                level_return = level.run()
            elif menu_return == MENU_OPTION[2]:
                pygame.quit() # Close window
                quit() # end pygame
            else:
                pass




