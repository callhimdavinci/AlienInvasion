""""AlienInvasion Class"""
import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """"overall class to manage game assets and behaviour"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """"main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """"Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """"Update images on screen, and flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.draw_ship()
        pygame.display.flip()


if __name__ == '__main__':
    AI = AlienInvasion()
    AI.run_game()
