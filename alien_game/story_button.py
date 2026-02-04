import pygame.font

class Story_button:
    """a class to build buttons for the game"""
    def __init__(self, ai_game, msg):
        """initalize butten atrabutes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # set the dimentions of the button
        self.width, self.hight = 200, 50
        self.story_button_color = (60, 135, 85)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # build the buttons rect object and center it 
        self.rect = pygame.Rect(0, 0, self.width, self.hight)
        self.rect.top = 413
        self.rect.left = 470

        # the buttons message neeeds to be prepared only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """turn msg into a rendered image and center the image"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                    self.story_button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_butten(self):
        """braw blank butten and a message"""
        self.screen.fill(self.story_button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)