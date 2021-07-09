""""AlienInvasion Class"""
import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """"overall class to manage game assets and behaviour"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """"main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """"Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullets(self):
        """"Create a new bullet and add it to bullets group"""
        if len(self.bullets) <self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """"Update Position of bullets and get rid of old bullets"""
        #update
        self.bullets.update()

        #remove dissapeared bullets
        for bullet in self.bullets.copy():
            if bullet.bullet_rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _update_screen(self):
        """"Update images on screen, and flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.draw_ship()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    AI = AlienInvasion()
    AI.run_game()
