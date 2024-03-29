class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #Ship setteing
        self.ship_speed = 1.5

        #Bullet setting
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 1000

        self.alien_speed = 1.0
        self.fleet_drop_speed = 100

        self.fleet_direction = 1


