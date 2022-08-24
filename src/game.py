import pygame
import sys
from . import constants as cn
from .logger import logger as lg


class Game(object):
    """
    Base Class That Runs The Entire Game
    Other objects will be instantiated and manipulated in here
    """
    def __init__(self) -> None:
        # Initialize pygame and set constants
        pygame.init()
        self.screen = pygame.display.set_mode((cn.WIDTH, cn.HEIGHT))
        pygame.display.set_caption(cn.TITLE, cn.ICON_LOCATION)
        self.running = True

        lg.debug("Game Started")

    def display_game(self) -> None:
        self.screen.fill(cn.WHITE)

    def run(self) -> None:
        # Main Game Loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_ESCAPE:
                        self.running = False

            self.display_game()

            pygame.display.flip()

        pygame.quit()
        lg.debug("Game Exited")
        sys.exit()
