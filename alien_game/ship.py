import pygame
from pygame.sprite import Sprite 

class Ship(Sprite):
   """A class for our ship"""

   def __init__(self, ai_game):
      """initalize the ship and its starting position"""
      super().__init__()
      self.screen = ai_game.screen
      self.settings = ai_game.settings
      self.screen_rect = ai_game.screen.get_rect()

      # Load the ship imige and get its rect
      self.image = pygame.image.load('images/ship.bmp')
      self.rect = self.image.get_rect()

      # start each new ship at the bottem center of the screen
      self.rect.midbottom = self.screen_rect.midbottom

      # Store a float for the ships exact horizontal position.
      self.x = float(self.rect.x)

      # movment flags; start with a ship thats not moving
      self.moving_right = False
      self.moving_left = False

   def update(self):
      """update the ships positoin based on the movment flags"""
      # Update the ships x value not the rect
      if self.moving_right and self.rect.right < self.screen_rect.right:
         self.x += self.settings.ship_speed
      if self.moving_left and self.rect.left > 0:
         self.x -= self.settings.ship_speed

      # update rect object from self.x.
      self.rect.x = self.x

   def blitme(self):
       """draw the ship"""
       self.screen.blit(self.image, self.rect)

   def center_ship(self):
      """center the ship"""
      self.rect.midbottom = self.screen_rect.midbottom
      self.x = float(self.rect.x)   