import pygame


class Ship:

    def __init__(self, ai_game):
        """Init ship and set it position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Download ship img and tak it 'rect'
        self.image = pygame.image.load('img/rocket-icon.bmp')
        self.rect = self.image.get_rect()

        # Create a new ship in bottom of the screen in middle
        self.rect.midbottom = self.screen_rect.midbottom

        # Save float for ship place
        self.x = float(self.rect.x)

        # Movement indicator
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Update the ship's current position
        based on the motion indicator
        """
        # Update value ship.x but not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update object 'rect' from self.x
        self.rect.x = self.x

    def blitme(self) -> object:
        # Draw a ship
        self.screen.blit(self.image, self.rect)

    def center_ship(self):

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
