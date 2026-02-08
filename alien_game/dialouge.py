import pygame
from button import Button


class Dialogue:
    """Handles story dialogue display and progression."""

    def __init__(self, game, lines):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings

        self.lines = lines
        self.index = 0
        self.active = True

        self.font = pygame.font.SysFont(None, 48)
        self.hint_font = pygame.font.SysFont(None, 32)
        self.next_button = Button(game, "next", "Next", 0, 0, 160, 50)

    def reset(self, lines):
        """Load new dialogue lines and restart."""
        self.lines = lines
        self.index = 0
        self.active = True

    def advance(self):
        """Go to next line. Returns False when finished."""
        self.index += 1
        if self.index >= len(self.lines):
            self.active = False
            return False
        return True

    def draw(self):
        """Draw dialogue overlay."""
        padding = 20
        if not self.active:
            return

        # Dark overlay
        overlay = pygame.Surface(
            (self.settings.screen_width, self.settings.screen_height)
        )
        overlay.set_alpha(160)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        # Dialogue box
        box_w = int(self.settings.screen_width * 0.85)
        box_h = 180
        box_x = (self.settings.screen_width - box_w) // 2
        box_y = 60

        pygame.draw.rect(self.screen, (20, 20, 20),
                         (box_x, box_y, box_w, box_h), border_radius=16)
        pygame.draw.rect(self.screen, (220, 220, 220),
                         (box_x, box_y, box_w, box_h), 3, border_radius=16)
        self.next_button.rect.x = (box_x + box_w) - self.next_button.rect.width - padding
        self.next_button.rect.y = (box_y + box_h) - self.next_button.rect.height - padding
        self.next_button.msg_image_rect.center = self.next_button.rect.center
        self.next_button.draw_button()

        # Current line 
        line = self.lines[self.index]
        text_surf = self.font.render(line, True, (240, 240, 240))
        self.screen.blit(text_surf, (box_x + 25, box_y + 35))


    def handle_click(self, mouse_pos):
        if not self.active:
            return False
        if self.next_button.rect.collidepoint(mouse_pos):
           result = self.advance()
           if not result:
                return True
        
        return False