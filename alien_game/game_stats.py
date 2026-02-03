class GameStats:
    """track stats"""

    def __init__(self, ai_game):
        """initalize satistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        

    def reset_stats(self):
        """initalize satistics"""
        self.ships_left = self.settings.ship_limit
        self.score = 0