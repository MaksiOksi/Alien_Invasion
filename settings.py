class Settings:

    def __init__(self):

        # Screen settings
        self.screen_width = 1500
        self.screen_height = 900
        self.bg_color = (150, 150, 150)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 100, 170)
        self.bullets_allowed = 5

        # Alien setting
        self.alien_speed = 1.0
        self.fleet_drop_speed = 50

        # Fleet direction <- -1  1 ->
        self.fleet_direction = 1
