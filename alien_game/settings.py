class Settings:
    """A class for settings. set = settings"""
    def __init__(self):
        """intialize the set"""
        #screen set
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (40, 75, 80)
        
        # ship set 
        self.ship_speed = 2.5
        self.ship_limit = 3

        # Bullet set
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_hight = 15
        self.bullet_color = (255, 230, 200)
        self.bullets_allowed = 7

        #alien set
        self.alien_speed = 2
        self.fleet_drop_speed = 10
        # fleet direction of 1 repersents right -1 is left.
        self.fleet_direction = 1