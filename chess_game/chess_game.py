import pygame
import sys
from settings import Settings
from move_rules import MoveRules
from move import Move

class ChessGame():
    """an overall class to manage chess_game"""

    def _starting_board(self):
        """Return a fresh starting chess board."""
        return [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                ["--", "--", "--", "--", "--", "--", "--", "--"],
                ["--", "--", "--", "--", "--", "--", "--", "--"],
                ["--", "--", "--", "--", "--", "--", "--", "--"],
                ["--", "--", "--", "--", "--", "--", "--", "--"],
                ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
    
    def __init__(self):
        """initalize values"""
        self.settings = Settings()
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.selected_square = None
        self.selected_piece = None
        self.white_king_moved = False
        self.black_king_moved = False
        self.white_left_rook_moved = False
        self.white_right_rook_moved = False
        self.black_right_rook_moved = False
        self.black_left_rook_moved = False
        self.board = self._starting_board()
        self.move_rules = MoveRules(self.board, self)
        self.turn = "w"
        self.font = pygame.font.SysFont(None, 36)
        self.title_font = pygame.font.SysFont(None, 88)
        self.button_font = pygame.font.SysFont(None, 44)
        self.legal_moves = []
        self.last_move = None
        self.game_state = "menu"
        self.game_over_message = ""
        self.status_message = ""
        self.status_message_end_time = 0
        self.start_button = pygame.Rect(0, 0, 260, 70)
        self.start_button.center = (
            self.settings.screen_width // 2,
            self.settings.screen_height // 2 + 70,
        )
        self.menu_button = pygame.Rect(0, 0, 290, 70)
        self.menu_button.center = (
            self.settings.screen_width // 2,
            self.settings.screen_height // 2 + 80,
        )
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
                    if self.game_state == "menu":
                        self._check_menu_click(mouse_pos)
                    elif self.game_state == "game_over":
                        self._check_game_over_click(mouse_pos)
                    else:
                        self._check_board_click(mouse_pos)
            self.screen.fill(self.settings.bg_color)
            if self.game_state == "menu":
                self._draw_title_screen()
            else:
                self._draw_board()
                self._highlited_square()
                self._highlited_legal_moves()
                self._draw_pieces()
                self._draw_status_message()
                if self.game_state == "game_over":
                    self._draw_game_over_screen()
            pygame.display.flip()
            self.clock.tick(60)

    def _check_menu_click(self, mouse_pos):
        """Start the game from the title screen."""
        if self.start_button.collidepoint(mouse_pos):
            self._reset_game()
            self.game_state = "playing"

    def _check_game_over_click(self, mouse_pos):
        """Return to the start screen after the game ends."""
        if self.menu_button.collidepoint(mouse_pos):
            self._reset_game()
            self.game_state = "menu"

    def _draw_title_screen(self):
        """Draw a simple title screen with a start button."""
        title_image = self.title_font.render("Chess Masters", True, (245, 245, 245))
        title_rect = title_image.get_rect(center=(
            self.settings.screen_width // 2,
            self.settings.screen_height // 2 - 70,
        ))
        self.screen.blit(title_image, title_rect)

        subtitle_image = self.font.render("Click below to start a new game", True, (210, 210, 210))
        subtitle_rect = subtitle_image.get_rect(center=(
            self.settings.screen_width // 2,
            self.settings.screen_height // 2 - 15,
        ))
        self.screen.blit(subtitle_image, subtitle_rect)

        pygame.draw.rect(self.screen, (80, 150, 105), self.start_button, border_radius=10)
        pygame.draw.rect(self.screen, (235, 235, 235), self.start_button, 3, border_radius=10)

        button_image = self.button_font.render("Start Game", True, (255, 255, 255))
        button_rect = button_image.get_rect(center=self.start_button.center)
        self.screen.blit(button_image, button_rect)

    def _draw_game_over_screen(self):
        """Draw the game-over overlay and back-to-menu button."""
        overlay = pygame.Surface((self.settings.screen_width, self.settings.screen_height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))

        message_image = self.button_font.render(self.game_over_message, True, (255, 255, 255))
        message_rect = message_image.get_rect(center=(
            self.settings.screen_width // 2,
            self.settings.screen_height // 2 - 10,
        ))
        self.screen.blit(message_image, message_rect)

        pygame.draw.rect(self.screen, (80, 110, 170), self.menu_button, border_radius=10)
        pygame.draw.rect(self.screen, (235, 235, 235), self.menu_button, 3, border_radius=10)

        button_image = self.button_font.render("Back To Start", True, (255, 255, 255))
        button_rect = button_image.get_rect(center=self.menu_button.center)
        self.screen.blit(button_image, button_rect)
    
    def _draw_status_message(self):
        """draw a temperary message"""
        if self.status_message and pygame.time.get_ticks() < self.status_message_end_time:
            message_image = self.button_font.render(self.status_message, True, (255, 255, 255))
            message_rect = message_image.get_rect(center=(
                self.settings.screen_width // 2,
                40,
            ))
            self.screen.blit(message_image, message_rect)

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

        if not (board_left <= mouse_x < board_right and board_top <= mouse_y < board_bottom):
            return

        column = (mouse_x - board_left) // self.settings.square_size
        row = (mouse_y - board_top) // self.settings.square_size
        piece = self.board[row][column]

        if self.selected_square is None:
            if piece != "--" and piece.startswith(self.turn):
                self.selected_square = (row, column)
                self.selected_piece = piece
                self.legal_moves = self.move_rules.get_legal_moves_for_piece(row, column)
        elif self.selected_square == (row, column):
            self.selected_square = None
            self.selected_piece = None        
            self.legal_moves = []   
        else:
            if piece != "--" and piece.startswith(self.turn):
                self.selected_square = (row, column)
                self.selected_piece = piece
                self.legal_moves = self.move_rules.get_legal_moves_for_piece(row, column)
            else:
                start_row, start_column = self.selected_square
                move = Move(start_row, start_column, row, column, self.selected_piece)
                if self.move_rules.is_valid_move(move):
                    moved_piece = self.selected_piece
                    castling = False
                    if ((self.selected_piece == "wK" or self.selected_piece == "bK")
                        and abs(column - start_column) == 2):
                        castling = True
                        if column > start_column:
                            rook_piece = self.board[row][7]
                            self.board[row][5] = rook_piece
                            self.board[row][7] = "--"
                        else:
                            rook_piece = self.board[row][0]
                            self.board[row][3] = rook_piece
                            self.board[row][0] = "--"
                    captured_piece = self.board[row][column]
                    en_passant = False
                    en_passant_captured_piece = "--"

                    if (self.selected_piece[1] == "P"
                        and abs(column - start_column) == 1
                        and captured_piece == "--"):
                        en_passant = True
                        en_passant_captured_piece = self.board[start_row][column]
                        self.board[start_row][column] = "--"
                    self.board[row][column] = self.selected_piece
                    self.board[start_row][start_column] = "--"
                    if self.move_rules._promotion(move):
                        self.board[row][column] = self.selected_piece[0] + "Q"
                    if self.move_rules.is_in_check(self.turn):
                        self.board[start_row][start_column] = self.selected_piece
                        if en_passant:
                          self.board[start_row][column] = en_passant_captured_piece
                        self.board[row][column] = captured_piece

                        if castling:
                            if column > start_column:
                                self.board[row][7] = self.board[row][5]
                                self.board[row][5] = "--"
                            else:
                                self.board[row][0] = self.board[row][3]
                                self.board[row][3] = "--"
                        print("illegal move: king is in check")
                        return
                    self._update_move_flags(moved_piece, start_row, start_column)
                    self.selected_square = None
                    self.selected_piece = None
                    self.legal_moves = []
                    self.last_move = move

                    if self.turn == "w":
                        enemy_color = "b"
                    else:
                        enemy_color = "w" 
                    
                    if self.move_rules.is_in_check(enemy_color):
                        self.status_message = "Check"
                        self.status_message_end_time = pygame.time.get_ticks() + 2000

                    enemy_moves = self.move_rules.get_all_legal_moves(enemy_color)
                    if not enemy_moves:
                        if self.move_rules.is_in_check(enemy_color):
                            winner = "White" if self.turn == "w" else "Black"
                            self.game_over_message = f"Checkmate! {winner} wins"
                        else:
                            self.game_over_message = "Stalemate"
                        self.game_state = "game_over"

                    if self.turn == "w":
                        self.turn = "b"
                    else:
                        self.turn = "w"

    def _reset_game(self):
        """Reset the full game state to a fresh game."""
        self.selected_square = None
        self.selected_piece = None
        self.white_king_moved = False
        self.black_king_moved = False
        self.white_left_rook_moved = False
        self.white_right_rook_moved = False
        self.black_right_rook_moved = False
        self.black_left_rook_moved = False
        self.board = self._starting_board()
        self.move_rules.board = self.board
        self.turn = "w"
        self.legal_moves = []
        self.last_move = None
        self.game_over_message = ""

    def _update_move_flags(self, moved_piece, start_row, start_column):
        """Track whether kings and corner rooks have moved."""
        if moved_piece == "wK":
            self.white_king_moved = True
        elif moved_piece == "bK":
            self.black_king_moved = True
        elif moved_piece == "wR" and start_row == 7 and start_column == 0:
            self.white_left_rook_moved = True
        elif moved_piece == "wR" and start_row == 7 and start_column == 7:
            self.white_right_rook_moved = True
        elif moved_piece == "bR" and start_row == 0 and start_column == 0:
            self.black_left_rook_moved = True
        elif moved_piece == "bR" and start_row == 0 and start_column == 7:
            self.black_right_rook_moved = True

    def _highlited_square(self):
        """a methed to show what pies is selected"""
        if self.selected_square is not None:
           row, column = self.selected_square
           x = self.settings.board_x + column * self.settings.square_size
           y = self.settings.board_y + row * self.settings.square_size
           rect = pygame.Rect(x, y, self.settings.square_size,
                         self.settings.square_size)
           pygame.draw.rect(self.screen,self.settings.highlight_color, rect, 4)
    
    def _highlited_legal_moves(self):
        for move in self.legal_moves:
            x = self.settings.board_x + move.end_column * self.settings.square_size
            y = self.settings.board_y + move.end_row * self.settings.square_size
            center_x = x + self.settings.square_size // 2
            center_y = y + self.settings.square_size // 2
            radius = self.settings.square_size // 3
            pygame.draw.circle(
                self.screen,
                self.settings.legal_highlight_color,
                (center_x, center_y),
                radius,
                3
            )
chess = ChessGame()
chess.run_game()
