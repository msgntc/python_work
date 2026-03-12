import pygame
import sys
from settings import Settings
from move_rules import MoveRules
from move import Move

class ChessGame():
    """an overall class to manage chess_game"""
    
    def __init__(self):
        """initalize values"""
        self.settings = Settings()
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.selected_square = None
        self.selected_piece = None
        self.board = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN","bR"],
                      ["bP", "bP", "bP", "bP", "bP", "bP", "bP","bP"],
                      ["--", "--", "--", "--", "--", "--", "--","--"],
                      ["--", "--", "--", "--", "--", "--", "--","--"],
                      ["--", "--", "--", "--", "--", "--", "--","--"],
                      ["--", "--", "--", "--", "--", "--", "--","--"],
                      ["wP", "wP", "wP", "wP", "wP", "wP", "wP","wP"],
                      ["wR", "wN", "wB", "wQ", "wK", "wB", "wN","wR"]]
        self.move_rules = MoveRules(self.board)
        self.turn = "w"
        self.font = pygame.font.SysFont(None, 36)
        pygame.display.set_caption("Chess Masters: Thqt0ne6uy")
    def run_game(self):
        """create a loop to run the game and quit"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_board_click(mouse_pos)
            self.screen.fill(self.settings.bg_color)
            self._draw_board()
            self._highlited_square()
            self._draw_pieces()
            pygame.display.flip()
            self.clock.tick(60)

    def _draw_board(self):
        """draw a chess bord"""
        for row in range(self.settings.board_size):
            for column in range(self.settings.board_size):
                if (row + column) % 2 == 0:
                    square_color = self.settings.light_square
                else:
                    square_color = self.settings.dark_square
                x = self.settings.board_x + column * self.settings.square_size
                y = self.settings.board_y + row * self.settings.square_size

                square_rect = pygame.Rect(x, y,
                         self.settings.square_size, self.settings.square_size)
                pygame.draw.rect(self.screen, square_color, square_rect)

    def _draw_pieces(self):
        for row in range(self.settings.board_size):
            for column in range(self.settings.board_size):
                piece = self.board[row][column]
                if piece != "--":
                    piece_text = self.font.render(piece, True, (0, 0, 0))
                    x = self.settings.board_x + column * self.settings.square_size
                    y = self.settings.board_y + row * self.settings.square_size
                    piece_rect = piece_text.get_rect(center=(
                        x + self.settings.square_size // 2,
                        y + self.settings.square_size // 2))
                    self.screen.blit(piece_text, piece_rect)

    def _check_board_click(self, mouse_pos):
        """check if the player clicked on the board"""
        mouse_x, mouse_y = mouse_pos
        board_left = self.settings.board_x
        board_top = self.settings.board_y
        board_right = board_left + self.settings.board_pixels
        board_bottom = board_top + self.settings.board_pixels

        if board_left <= mouse_x < board_right and board_top <= mouse_y < board_bottom:
            column = (mouse_x - board_left) // self.settings.square_size
            row = (mouse_y - board_top) // self.settings.square_size
            piece = self.board[row][column]

        if self.selected_square is None:
            if piece != "--" and piece.startswith(self.turn):
                self.selected_square = (row, column)
                self.selected_piece = piece
        elif self.selected_square == (row, column):
            self.selected_square = None
            self.selected_piece = None
        else:
            if piece != "--" and piece.startswith(self.turn):
                self.selected_square = (row, column)
                self.selected_piece = piece
            else:
                start_row, start_column = self.selected_square
                move = Move(start_row, start_column, row, column, self.selected_piece)
                if self.move_rules.is_valid_move(move):
                    self.board[row][column] = self.selected_piece
                    self.board[start_row][start_column] = "--"
                    self.selected_square = None
                    self.selected_piece = None
                    if self.turn == "w":
                        self.turn = "b"
                    else:
                        self.turn = "w"

    def _highlited_square(self):
        """a methed to show what pies is selected"""
        if self.selected_square is not None:
           row, column = self.selected_square
           x = self.settings.board_x + column * self.settings.square_size
           y = self.settings.board_y + row * self.settings.square_size
           rect = pygame.Rect(x, y, self.settings.square_size,
                         self.settings.square_size)
           pygame.draw.rect(self.screen,self.settings.highlight_color, rect, 4)
    
chess = ChessGame()
chess.run_game()
