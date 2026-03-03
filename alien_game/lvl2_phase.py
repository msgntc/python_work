class Lvl2:
    """a class for the second level"""

    def __init__(self, ai_game):
        """initalize veribles"""
        self.ai_game = ai_game
        self.current_phs = 0
        self.lvl2_complete = False
    
    def start_lvl2(self):
        """start the second level"""
        self.ai_game.bullets.empty()
        self.ai_game.alien_bullets.empty()
        self.ai_game.aliens.empty()
        self.ai_game.boss = None
        self.lvl2_complete = False
        self.current_phs = 0
        self.start_lvl2_phs1()

    def start_lvl2_phs1(self):
        """start the first phase of leval two"""
        self.current_phs = 1
