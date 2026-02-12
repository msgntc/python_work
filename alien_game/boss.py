import pygame
import random
from pygame.sprite import Sprite
class Boss(Sprite):
    """a boss for the first level"""
    def __init__(self, ai_game):

        super().__init__()
        # get atrabutes from other files
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # get the rects and images
        self.boss_image = pygame.image.load('images/alien_boss.bmp')
        w, h = self.boss_image.get_size()
        scale = 2.0
        new_size = (int(w * scale), int(h * scale))
        self.boss_image = pygame.transform.smoothscale(self.boss_image, new_size)
        self.rect = self.boss_image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # add boss movment
        self.speed_x = self.settings.boss_speed_x
        self.jitter_y = self.settings.boss_jitter_y 
        self.dodge_chance = self.settings.boss_dodge_chance 
        self.direction_x = 1
        self.next_dodge_time = 0
        self.dodge_cooldown_ms = 250
        self.burst_hits = 0
        self.burst_window_ms = 1200
        self.burst_threshold = 4
        self.burst_window_start = pygame.time.get_ticks()
        self.teleport_cooldown_ms = 1500
        self.next_teleport_time = 0

        # spawn the boss
        self.rect.midtop = self.screen_rect.midtop
        self.rect.y += 20
        self.hitbox = self.rect.inflate(-200, -160)
        self.hitbox.center = self.rect.center
        
        # initalize boss helth
        self.max_health = self.settings.boss_health
        self.current_health = self.max_health

        # add boss attacks
        self.next_rain_time = pygame.time.get_ticks()
        self.rain_active = False
    
    def blitme(self):
        """draw the boss"""
        self.screen.blit(self.boss_image, self.rect)

    def boss_hit(self, damage=1):
        """handle damage"""
        now = pygame.time.get_ticks()
        if now - self.burst_window_start > self.burst_window_ms:
            self.burst_hits = 0
            self.burst_window_start = now
        self.burst_hits += 1
        if self.burst_hits >= self.burst_threshold and now >= self.next_teleport_time:
            self.teleport_top()
            self.burst_hits = 0
            self.burst_window_start = now
            self.next_teleport_time = now + self.teleport_cooldown_ms
            return False
        self.current_health -= 1
        if self.current_health <= 0:
            return True
        else:
            return False
    
    def teleport_top(self):
        """teleprt the boss if he gets hit to much"""
        min_x = 0
        max_x = self.screen_rect.width - self.rect.width
        new_x = random.randint(min_x, max_x)
        self.rect.x = new_x
        self.rect.y = 20
        self.hitbox.center = self.rect.center
    
    def update_boss(self):
        self.rect.x += self.speed_x * self.direction_x
        now = pygame.time.get_ticks()
        if now >= self.next_dodge_time:
            self.rect.y += random.randint(-self.jitter_y, self.jitter_y)
            self.next_dodge_time = now + self.dodge_cooldown_ms
            if random.random() < self.dodge_chance:
                self.direction_x *= -1
        if self.rect.top < 20:
            self.rect.top = 20
        if self.rect.bottom > self.screen_rect.height // 3:
            self.rect.bottom = self.screen_rect.height // 3
        self.hitbox.center = self.rect.center
        if self.rect.left <= 0 or self.rect.right >= self.screen_rect.right:
            self.direction_x *= -1

    def spawn_rain_attacks(self):
        "spawns a shower of bullets"
        rain_x_positions = []
        w = self.screen_rect.width
        left_x = w // 6
        mid_x = w // 2
        right_x = (w * 5) // 6
        lane_centers = [left_x, mid_x, right_x]
        for center_x in lane_centers:
            for _ in range(self.settings.boss_rain_bullets_per_side):
                offset = random.randint(-self.settings.boss_rain_spread_px, self.settings.boss_rain_spread_px)
                spawn_x = center_x + offset
                spawn_x = max(0, min(spawn_x,
                    self.screen_rect.width)) 
                rain_x_positions.append(spawn_x)
        return rain_x_positions
    