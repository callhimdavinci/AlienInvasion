""""AlienInvasion Class"""
import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """"main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _create_fleet(self):
        """"Create the fleet of aliens"""
        # make an alien
        alien = Alien(self)  # neccesary to extract the physical properties of an alien, like the width in the next line
        alien_width, alien_height = alien.rect.size
        ship_height = self.ship.image_rect.height
        available_space_x = self.settings.screen_width - (2 * alien_width)
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_aliens_x = available_space_x // (2 * alien_width)
        number_aliens_y = available_space_y // (2*alien_width)
        for row_number in range(number_aliens_y):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """Respond if any aliens reach the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_alien(self, alien_number, row_number):
        """"Create alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.pos_x = alien_width + 2 * alien_width * alien_number
        alien.pos_y = alien_height + 2 * alien_height*row_number
        alien.rect.x, alien.rect.y = alien.pos_x, alien.pos_y
        self.aliens.add(alien)

    def _update_aliens(self):
        """"Check if the fleet is at an edge
            Update the position of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """"Update Position of bullets and get rid of old bullets"""
        # update
        self.bullets.update()

        # remove dissapeared bullets
        for bullet in self.bullets.copy():
            if bullet.bullet_rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """"Update images on screen, and flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.draw_ship()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    AI = AlienInvasion()
    AI.run_game()
