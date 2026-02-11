import pygame
from pygame.sprite import Sprite

class AlienBullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game, alien=None, spawn_x=None):
        """Create a bullet object at an aliens curent position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.alien_bullet_color

        # Create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_hight)
        if alien:
            self.rect.midbottom = alien.rect.midbottom
        elif spawn_x is not None:
            self.rect.midtop = (spawn_x, 0)
        else:
            raise ValueError("AlienBullet needs alien or spown_x")

        # store the bullets position as a float
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet down the screen"""
        # update the exact position of the bullet
        self.y += self.settings.alien_bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw a bullet onto the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)