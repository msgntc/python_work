import pygame 

class Ship:
   """A class for our ship"""

   def __init__(self, ai_game):
      """initalize the ship and its starting position"""
      self.screen = ai_game.screen
      self.screen_rect = ai_game.screen.get_rect()

      self.image = pygame.image.load('images/ship.bmp')
      width = self.image.get_rect().width
      height = self.image.get_rect().height
      self.rect = self.image.get_rect()

      self.image = pygame.transform.scale(self.image, (width/5, height/5))

      self.rect.midbottom = self.screen_rect.midbottom

   def blitme(self):
       """draw the ship"""
       self.screen.blit(self.image, self.rect)

