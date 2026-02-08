import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to repersent one alien"""

    def __init__(self, ai_game):
        """initalize tha alien"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.settings.helth
        self.helth = self.settings.helth

        # Load the alien imadge and set a rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien nere the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alians horasontal position
        self.x = float(self.rect.x)

        # alien helth
        self.settings.helth

    def check_edges(self):
        """retern true if alien isat the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return(self.rect.right >= screen_rect.right) or (self.rect.left <= 0)    
    
    def update(self):
        """move alein to the right or left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x