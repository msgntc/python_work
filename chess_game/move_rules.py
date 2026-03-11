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
        return False
    def _pawn_move(self, move):
        """check if a pan move is valid"""
        if move.piece.startswith("w"):
            direction = -1
            start_pawn_row = 6
            middle_row = start_pawn_row - 1
        else:
            direction = 1
            start_pawn_row = 1
            middle_row = start_pawn_row + 1
        target_piece = self.board[move.end_row][move.end_column]
        middle_row = start_pawn_row 
        if move.start_column == move.end_column:
            if move.end_row == move.start_row + direction and target_piece == "--":
                return True
            elif (move.start_row == start_pawn_row and move.end_row == move.start_row + 2 * direction
                   and target_piece == "--" and middle_row == "--"):
                return True
