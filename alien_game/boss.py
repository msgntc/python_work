import pygame
from pygame import sprite
class Boss(sprite):
    """a boss for the first level"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.setting
        self.screen_rect = ai_game.rect

        
