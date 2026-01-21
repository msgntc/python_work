import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to repersent one alien"""

    def __init__(self, ai_game):
        """initalize tha alien"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien imadge and set a rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien nere the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alians horasontal position
        self.x = float(self.rect.x)
    
    def update(self):
        """move alein to the right"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x