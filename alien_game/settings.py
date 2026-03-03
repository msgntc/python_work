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
        self.bullets_allowed = 5

        # alien set
        self.fleet_drop_speed = 10
        self.helth = 100
        self.alien_bullet_speed = 5
        self.alien_bullet_color = (180, 140, 90)
        self.phs2_alien = 5
        self.phs2_alien_speed = 25
        self.phs2_alien_health = 1

        # boss settings
        self.boss_health = 30
        self.boss_speed_x = 12
        self.boss_jitter_y = 3
        self.boss_dodge_chance = 0.25
        self.boss_rain_interval_ms = 300
        self.boss_rain_bullets_per_side = 3
        self.boss_rain_lane_count = 3
        self.boss_rain_spread_px = 50


        # how the game speed up
        self.speedup_scale = 1.25
        # how quckly the alian piont value increase
        self.score_scale = 1.7

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize set that change throught the game"""
        self.ship_speed = 3
        self.bullet_speed = 5
        self.alien_speed = 1.5
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
