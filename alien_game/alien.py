import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to repersent one alien"""

    def __init__(self, ai_game):
        """initalize tha alien"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien imadge and set a rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien nere the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alians horasontal position
        self.x = float(self.rect.x)
