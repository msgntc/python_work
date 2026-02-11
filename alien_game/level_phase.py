import pygame
import random
from alien import Alien

class StoryLevel:
    """a class for advancing te story phs = phase"""
    def __init__(self, ai_game):
        """init for StoryLevel"""
        self.ai_game = ai_game
        self.current_phs = 0
        self.phs2_kills = 0
        self.phase_order = [1, 2, 1, 1, 2, 1, 2, 2]
        self.phase_index = -1

    def start_story(self):
        """start the story and load the first phase"""
        self.phase_index = -1
        return self.start_next_phase()

    def start_next_phase(self):
        """advance to the next configured phase"""
        self.phase_index += 1
        if self.phase_index >= len(self.phase_order):
            return False

        next_phase = self.phase_order[self.phase_index]
        if next_phase == 1:
            self.start_phs_one()
        else:
            self.start_phs_two()
        return True

    def start_phs_one(self):
        """progress the story"""
        self.current_phs = 1
        pygame.mouse.set_visible(False)
        self.ai_game.bullets.empty()
        self.ai_game.alien_bullets.empty()
        self.ai_game.aliens.empty()
        self.ai_game.ship.center_ship()
        self.ai_game._create_fleet()
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("song/song.mp3")
            pygame.mixer.music.play(-1)

    def start_phs_two(self):
        """make super fast aliens fall from the top off the screen"""
        self.current_phs = 2
        self.phs2_kills = 0
        self.ai_game.bullets.empty()
        self.ai_game.alien_bullets.empty()
        self.ai_game.aliens.empty()
        self.ai_game.settings.alien_speed = self.ai_game.settings.phs2_alien_speed
        self._make_phs2_alien()
    
    def _make_phs2_alien(self):
        """spawn a phs2 alien"""
        edge = 250
        phs2_alien = Alien(self.ai_game)
        phs2_alien.helth = 5
        min_x = edge
        max_x = self.ai_game.settings.screen_width - edge - phs2_alien.rect.width
        if max_x < min_x:
            min_x = 0
            max_x = self.ai_game.settings.screen_width - phs2_alien.rect.width
        random_x = random.randint (min_x, max_x)
        phs2_alien.x = random_x
        phs2_alien.rect.x = random_x
        phs2_alien.rect.y = 0
        self.ai_game.aliens.add(phs2_alien)
    
    def phs2_alien_killed(self):
        """tracks if an alien has been killed"""
        self.phs2_kills += 1
        if self.phs2_kills >= self.ai_game.settings.phs2_alien:
            return True
        self._make_phs2_alien()
        return False
