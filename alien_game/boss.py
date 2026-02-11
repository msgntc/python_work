import pygame
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
        self.boss_image =pygame.transform.smoothscale(self.boss_image, new_size)
        self.rect = self.boss_image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # spawn the boss
        self.rect.midtop = self.screen_rect.midtop
        self.rect.y += 20
        self.hitbox = self.rect.inflate(-200, -160)
        self.hitbox.center = self.rect.center
        
        # initalize boss helth
        self.max_health = self.settings.boss_health
        self.current_health = self.max_health
    
    def blitme(self):
        """draw the boss"""
        self.screen.blit(self.boss_image, self.rect)

    def boss_hit(self, damage=1):
        """handle damage"""
        self.current_health -= 1
        if self.current_health <= 0:
            return True
        else:
            return False
    
    def update_boss(self):
        pass
