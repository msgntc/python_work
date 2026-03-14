class MoveRules():
    """a class for the rules in chess"""

    def __init__(self, board, game):
        """ initalize all my atrabutes"""
        self.board = board
        self.game = game
    def is_valid_move(self, move):
        """check wich piese was selected"""
        if move.piece == "--":
            return False
        piece_tipe = move.piece[1]
        if piece_tipe == "P":
            return self._pawn_move(move)
        if piece_tipe == "R":
            return self._rook_move(move)
        if piece_tipe == "B":
            return self._bishop_move(move) 
        if piece_tipe == "Q":
            return self._queen_move(move)
        if piece_tipe == "N":
            return self._knight_move(move)
        if piece_tipe == "K":
            return self._king_move(move)
        return False
    
    def _pawn_move(self, move):
        """check if a pawn move is valid"""
        if move.piece.startswith("w"):
            direction = -1
            start_pawn_row = 6
        else:
            direction = 1
            start_pawn_row = 1
        target_piece = self.board[move.end_row][move.end_column]
        middle_row = move.start_row + direction 
        middle_piece = self.board[middle_row][move.start_column]
        if move.start_column == move.end_column:
            if move.end_row == move.start_row + direction and target_piece == "--":
                return True
            elif (move.start_row == start_pawn_row and move.end_row == move.start_row + 2 * direction
                   and target_piece == "--" and middle_piece == "--"):
                return True
            else:
                return False
        if (abs(move.end_column - move.start_column) == 1 and move.end_row == move.start_row + direction
             and target_piece != "--" and target_piece[0] != move.piece[0]):
            return True
        return False
    
    def _rook_move(self, move):
        """check if a rook move is valid"""
        if move.start_column == move.end_column and move.start_row == move.end_row:
            return False
        elif move.start_column != move.end_column and move.start_row != move.end_row:
            return False
        else:
            if move.start_column == move.end_column:
                if move.end_row > move.start_row:
                    row_step = 1
                else:
                    row_step = -1
                for row in range(move.start_row + row_step, move.end_row, row_step):
                    if self.board[row][move.start_column] != "--":
                        return False

            if move.start_row == move.end_row:
                if move.end_column > move.start_column:
                    column_step = 1
                else:
                    column_step = -1 
                for column in range(move.start_column + column_step, move.end_column, column_step):
                            if self.board[move.start_row][column] != "--":
                                return False
            target_piece = self.board[move.end_row][move.end_column]
            if  target_piece != "--" and target_piece[0] == move.piece[0]:
                return False
            else:
                return True
    
    def _bishop_move(self, move):
        """check if a bishop move is valid"""
        if move.start_column == move.end_column and move.start_row == move.end_row:
            return False
        elif abs(move.start_row - move.end_row) != abs(move.start_column - move.end_column):
            return False
        else:
            if move.end_row > move.start_row:
                row_step = 1
            else:
                row_step = -1
            if move.end_column > move.start_column:
                column_step = 1
            else:
                column_step = -1
            for step in range(1, abs(move.end_row - move.start_row)):
                row = move.start_row + step * row_step
                column = move.start_column + step * column_step
                if self.board[row][column] != "--":
                    return False
        target_piece = self.board[move.end_row][move.end_column]
        if  target_piece != "--" and target_piece[0] == move.piece[0]:
             return False
        else:
            return True    
    
    def _queen_move(self, move):
        """check if a queen move is valid"""
        if move.start_row == move.end_row or move.start_column == move.end_column:
            return self._rook_move(move)
        elif abs(move.start_row - move.end_row) == abs(move.start_column - move.end_column):
            return self._bishop_move(move)
        else:
            return False
        
    def _knight_move(self, move):
        """check if a knigt move is valid"""
        target_piece = self.board[move.end_row][move.end_column]
        row_diff = abs(move.start_row - move.end_row)
        column_diff = abs(move.start_column - move.end_column)
        if not ((row_diff == 2 and column_diff == 1) or (row_diff == 1 and column_diff == 2)):
            return False
        elif  target_piece != "--" and target_piece[0] == move.piece[0]:
             return False
        else: 
            return True
    
    def _king_move(self, move):
        """check if a king move is valid"""
        row_diff = abs(move.start_row - move.end_row)
        column_diff = abs(move.start_column - move.end_column)
        target_piece = self.board[move.end_row][move.end_column]
        if  row_diff == 0 and column_diff == 0:
            if row_diff == 0 and column_diff == 2:
                return self._castle_move(move)
            return False
        elif row_diff > 1 or column_diff > 1:
            return False
        elif  target_piece != "--" and target_piece[0] == move.piece[0]:
             return False
        else:
            return True
    
    def _castle_move(self, move):
        """see if you can castle"""
        if move.piece.startswith("w"):
            back_row = 7
            if self.game.white_king_moved == True:
                return False
        else:
            back_row = 0
            if self.game.black_king_moved == True:
                return False
        if move.start_row != back_row or move.end_row != back_row:
            return False
        if move.end_column > move.start_column:
            rook_column = 7
            if move.piece.startswith("w"):
                if self.game.white_right_rook_moved:
                    return False
            else:
                if self.game.black_right_rook_moved:
                    return False
        else:
            rook_column = 0
            if move.piece.startswith("w"):
                if self.game.white_left_rook_moved:
                    return False
            else:
                if self.game.black_left_rook_moved:
                    return False 
        rook_piece = self.board[back_row][rook_column]
        if move.piece == ("wK"):
            expected_rook = ("wR")
        else:
            expected_rook = ("bR")
        if rook_piece != expected_rook:
            return False
        if rook_column > move.start_column:
            step = 1
        else:
            step = -1
        for column in range(move.start_column + step, rook_column, step):
            if self.board[back_row][column] != "--":
                return False
        return True 