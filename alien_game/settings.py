class Settings:
    """A class for settings. set = settings"""
    def __init__(self):
        """intialize the set"""
        #screen set
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (40, 75, 80)
        
        # ship set 
        self.ship_speed = 1.5

        # Bullet set
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_hight = 15
        self.bullet_color = (255, 0, 0)
        