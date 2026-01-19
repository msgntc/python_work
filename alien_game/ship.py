import pygame 

class Ship:
   """A class for our ship"""

   def __init__(self, ai_game):
      """initalize the ship and its starting position"""
      self.screen = ai_game.screen
      self.screen_rect = ai_game.screen.get_rect()

      # Load the ship imige and get its rect
      self.image = pygame.image.load('images/ship.bmp')
      self.rect = self.image.get_rect()

      
      # start each new ship at the bottem center of the screen
      self.rect.midbottom = self.screen_rect.midbottom
      # movment flag; start with a ship thats not moving
      self.moving_right = False

   def update(self):
      """update the ships positoin based on the movment flag"""
      if self.moving_right:
         self.rect.x += 1

   def blitme(self):
       """draw the ship"""
       self.screen.blit(self.image, self.rect)

