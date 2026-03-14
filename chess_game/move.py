class Move():
    """ a class for moving a piece"""
    def __init__(self, start_row, start_column, end_row, end_column, piece):
        """initalize everything"""
        self.start_row = start_row
        self.start_column = start_column
        self.end_row = end_row
        self.end_column = end_column
        self.piece = piece