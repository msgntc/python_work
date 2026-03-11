class MoveRules():
    """a class for the rules in chess"""

    def __init__(self, board):
        """ initalize all my atrabutes"""
        self.board = board

    def is_valid_move(self, move):
        """check wich piese was selected"""
        if move.piece == "--":
            return False
        piece_tipe = move.piece[1]
        if piece_tipe == "P":
            return self._pawn_move(move)
        if piece_tipe == "R":
            return self._pawn_move(move)
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
                    
            if move.start_row == move.end_row:
                column_step = 1
            else:
                 column_step = -1 

        