import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_game):

        # Make a bullet in the ship position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Bullet rect
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Save bullet value as a float
        self.y = float(self.rect.y)

    def update(self):
        """Push bullet to the top"""

        # Update  bullet position
        self.y -= self.settings.bullet_speed

        # Update rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw a bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
