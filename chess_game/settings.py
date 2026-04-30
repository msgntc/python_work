class Settings():
    """A class for settings. set = settings"""
    def __init__(self):
        """intialize the games static set"""
        #screen set
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (30, 30, 30)

        # chess board set
        self.board_size = 8
        self.board_pixels = 640
        self.square_size = self.board_pixels // self.board_size
        self.light_square = (240, 217, 181)
        self.dark_square = (181, 136, 99)
        self.board_x = (self.screen_width - self.board_pixels) // 2
        self.board_y = (self.screen_height - self.board_pixels) // 2
        self.highlight_color = (255, 255, 0)
        self.legal_highlight_color = (178, 34, 34)