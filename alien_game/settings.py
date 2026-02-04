class Settings:
    """A class for settings. set = settings"""
    def __init__(self):
        """intialize the games static set"""
        #screen set
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (40, 75, 80)
        
        # ship set 
        self.ship_limit = 3

        # Bullet set
        self.bullet_width = 3
        self.bullet_hight = 15
        self.bullet_color = (255, 230, 200)
        self.bullets_allowed = 7

        # alien set
        self.fleet_drop_speed = 10

        # how the game speed up
        self.speedup_scale = 1.3
        # how quckly the alian piont value increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize set that change throught the game"""
        self.ship_speed = 2.5
        self.bullet_speed = 5
        self.alien_speed = 2
        # fleet direction of 1 repersents right -1 is left.
        self.fleet_direction = 1

        # score set
        self.alien_points = 50

    def increase_speed(self):
        """increes speed set and alian points"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)