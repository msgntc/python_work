import pygame

class StoryLevel:
    """a class for advancing te story phs = phase"""
    def __init__(self, ai_game):
        """init for StoryLevel"""
        self.ai_game = ai_game
        self.phs2_kills = 0

    def start_phs_one(self):
        """progress the story"""
        pygame.mouse.set_visible(False)
        self.ai_game.ship.center_ship()
        self.ai_game._create_fleet()
        self.ai_game._fire_alien_bullet()
        pygame.mixer.music.load("song/song.mp3")
        pygame.mixer.music.play(-1)

    def start_phs_two(self):
        """make super fast aliens fall from the top off the screen"""
        self.phs2_kills = 0
        self.ai_game.aliens.empty()
        
