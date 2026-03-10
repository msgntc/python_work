import pygame
import sys
from settings import Settings

class ChessGame:
    """an overall class to manage chess_game"""
    def __init__(self):
        """initalize values"""
        self.settings = Settings()
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Chess Masters: Thqt0ne6uy")
    def run_game(self):
        """create a loop to run the game and quit"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            self._draw_board()
            pygame.display.flip()
            self.clock.tick(60)
    def _draw_board(self):
        """draw a chess bord"""
        for row in range(self.settings.board_size):
            for column in range(self.settings.board_size):
                if (row + column) %2 == 0:
                    square_color = self.settings.light_square
                else:
                    square_color = self.settings.dark_square
                x = self.settings.board_x + column * self.settings.square_size
                y = self.settings.board_y + row * self.settings.square_size

                square_rect = pygame.Rect(x, y,
                         self.settings.square_size, self.settings.square_size)
                pygame.draw.rect(self.screen, square_color, square_rect)

chess = ChessGame()
chess.run_game()
