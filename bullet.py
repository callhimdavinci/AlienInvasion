import pygame
import pygame.draw
from pygame.sprite import Sprite


class Bullet(Sprite):
    """"A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """"Create a bullet object at the ships current position"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.bullet_rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.bullet_rect.midtop = ai_game.image_rect.midtop
        self.pos_y = float(self.bullet_rect.y)

    def update(self):
        """Move the bullet up the screen"""

        self.pos_y -= self.settings.bullet_speed
        self.bullet_rect.y = self.pos_y

    def draw_bullet(self):
        """"Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)
