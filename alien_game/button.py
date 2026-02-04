import pygame.font

class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, name, msg, x, y, width=200, height=50):
        self.screen = ai_game.screen

        # identity
        self.name = name 

        # visuals
        self.width, self.height = width, height
        self.story_button_color = (60, 135, 85)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(x, y, self.width, self.height)
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.story_button_color
        )
        self.msg_image_rect = self.msg_image.get_rect(center=self.rect.center)

    def draw_button(self):
        self.screen.fill(self.story_button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
