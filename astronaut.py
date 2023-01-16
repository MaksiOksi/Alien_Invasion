import pygame

class Astronaut:

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Download an astronaut img and take it 'rect'
        self.image = pygame.image.load('img/cute_astro.bmp')
        self.rect = self.image.get_rect()

        # Create a hero in the screen center
        self.rect.center = self.screen_rect.center

    def blitme(self) -> object:
        self.screen.blit(self.image, self.rect)