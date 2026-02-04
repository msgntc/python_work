import json
from pathlib import Path
class GameStats:
    """track stats"""

    def __init__(self, ai_game):
        """initalize satistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        try:
            self.path = Path('high_score.txt')
            high_score = self.path.read_text() 
            value = json.loads(high_score)
            self.high_score = value
        except:
            self.high_score = 0
                        
    def reset_stats(self):
        """initalize satistics"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """save the high score to a Json"""
        self.path.write_text(json.dumps(self.high_score))