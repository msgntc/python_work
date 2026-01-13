import sys

import pygame

class AlienInvasion:
    """
    Docstring for AlienInvasion
    """
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Description
        """
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = (160, 44, 43)

    def run_game(self):
        """
        Docstring for run_game
        
        :param self: Description
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
