import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from dialouge import Dialogue
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """overall class to manage game assets and behavior"""
    def __init__(self):
        """Initalize the game, and create the game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion by: Thqt0ne6uy")

        # start alien invasion in an inactive state.
        self.game_mode = "MENU"
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() 
        self.aliens = pygame.sprite.Group()

        # Story dialogue system 
        self.dialogue = None

        self._create_fleet() 

        # Make the Play button
        self.buttons = [
        Button(self, "story", "Story Mode", 350, 413, 200, 50),
        Button(self, "free play", "Free Play", 800, 413, 200, 50),
        Button(self, "time", "A 5 minute experience", 800, 500, 200, 0),
        Button(self, "S_time", "A 15 minute experience", 350, 500, 200, 0),
        ]

    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._check_events()
            if self.game_mode == "FREE":
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            elif self.game_mode == "STORY":
                self.settings.alien_speed = 10
                self.settings.ship_speed = 10
                self.settings.bullet_speed = 20
                if not self.dialogue.active:
                    self._update_bullets()
                    self._update_aliens()
                    self.ship.update()
            self._update_screen()
            self.clock.tick(60)  

    def _check_events(self):
            """respond to key"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP: 
                     self._check_keyup_events(event)  
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.game_mode == "STORY" and self.dialogue and self.dialogue.active:
                        finished = self.dialogue.handle_click(mouse_pos)
                        if finished:
                            pygame.mouse.set_visible(False)
                            self.ship.center_ship()
                            self._create_fleet()
                            continue
                    self._check_button_pressed(mouse_pos)

    def _check_button_pressed(self, mouse_pos):
        """start a new game when the player clicks play"""
        button_clicked = False
        butten_selected = None

        # Only allow button clicks from the menu
        if self.game_mode != "MENU":
            return

        for butten in self.buttons:
            if butten.name == "free play":
                if butten.rect.collidepoint(mouse_pos):
                    button_clicked = True
                    butten_selected = "FREE"
                    break

            elif butten.name == "story":
                if butten.rect.collidepoint(mouse_pos):
                    button_clicked = True
                    butten_selected = "STORY"
                    break

        if button_clicked:
            if butten_selected == "FREE":
                self._start_free_play()
            elif butten_selected == "STORY":
                self._start_story_mode()

    def _start_free_play(self):
        """start free play"""  
        self.settings.initialize_dynamic_settings()
        # Reset the game satistics
        self.settings.helth = 1
        self.stats.reset_stats()
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
        self.game_mode = "FREE" 

        # Get rid of any remaining bullets and aliens. 
        self.bullets.empty()
        self.aliens.empty()

        # create a new fleet and centure the ship
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse curser
        pygame.mouse.set_visible(False)

            # play a song
        if self.game_mode == "FREE":
                pygame.mixer.music.load("song/song.mp3")
                pygame.mixer.music.play(-1)

    def _start_story_mode(self):
        """start your grand adventure (smilly face emoji)"""
        self.settings.helth = 2
        self.settings.initialize_dynamic_settings()
        # Reset the game satistics
        self.stats.reset_stats()
        self.sb.prep_ships()
        self.game_mode = "STORY"
        self.sb.prep_score()
        self.sb.prep_high_score()
        self.sb.prep_level()

        # Get rid of any remaining bullets and aliens. 
        self.bullets.empty()
        self.aliens.empty()

        # create a new fleet and centure the ship
        self.ship.center_ship()

        lines = [
            "Its been 14 days scence sientist descovered the wormhole",
            "I was sent to gather data when i was attacked",
            "the attacker was a ship almost identikle to mine",
            "I maneged to get the ship to flee but not without setback",
            "my ship wich usually is much stronger is in a weekend condision",
            "And i fear that this my be detramental",
            "my radars have picked up stange energy singnals",
            "I dant know what it is...",
            "...but my guess...",
            "ALIENS"
        ]
        self.dialogue = Dialogue(self, lines)

    def _check_keydown_events(self, event):
        """respond to keypresses"""            
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()  
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()      

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet an add it to the bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)  

    def _update_bullets(self): 
        """updates position of bullets and get rid of of old bullets""" 
        # updates position of bullets
        self.bullets.update()

        # Get rid of old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """respont to bullet alien colisions""" 
        # check for bullets hitting aliens if true get rid of the bullet and allien
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, False)
        if collisions:
            for hit_aliens in collisions.values():
                for alien in hit_aliens:
                    alien.helth -= 1
                    if alien.helth <= 0:
                        self.aliens.remove(alien)
                        self.stats.score += self.settings.alien_points
                self.sb.prep_score()
                self.sb.check_high_score()
        if not self.aliens:
            #destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # increase level
            self.stats.level += 1 
            self.sb.prep_level()
    
    def _update_aliens(self):
        """ check if the fleet is at the edge then update the positions off all aliens"""
        self._check_fleet_edges()
        self.aliens.update()

        # look for alien-ship colisions.

        hit_alien = pygame.sprite.spritecollideany(self.ship, self.aliens)
        if hit_alien:
            self._ship_hit(hit_alien)

        # look for aliens hitting the bottom of the screen
        self._check__aliens_bottom()

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Make an alien and create aliens until no room 
        # space betweeen aliens is one alian width and one aliah hight
        alien = Alien(self)
        alien_width, alien_hight = alien.rect.size

        current_x, current_y = alien_width, alien_hight
        while current_y < (self.settings.screen_height - 3 * alien_hight):
            while current_x < (self.settings.screen_width - 2 * alien_width):     
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            # finished a row; reset the x value, and incrament y value
            current_x = alien_width
            current_y += 2 * alien_hight

    def _create_alien(self, x_position, y_position):
        """create an alian and put it in a fleet"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """respond apropetly if a alien reches an egde"""
        for alein in self.aliens.sprites():
            if alein.check_edges():
                self._change_fleet_direction()
                break

    def _check__aliens_bottom(self):
        """check if any aliens have reached the bottom of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # the same as if the ship gets hit
                self._ship_hit()
                break      

    def _change_fleet_direction(self):
        """drop the entier fleet and change the fleet dirction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1                

    def _update_screen(self):
         """Update imiges and flip the screen"""
         self.screen.fill(self.settings.bg_color)
         for bullet in self.bullets.sprites():
             bullet.draw_bullet()
         self.ship.blitme()
         self.aliens.draw(self.screen)

         # draw the score information
         self.sb.show_score()

         # Draw the play button if the game is inactive.
         if self.game_mode == "MENU":
             for button in self.buttons:
                 button.draw_button()

         if self.game_mode == "STORY" and self.dialogue and self.dialogue.active:
           self.dialogue.draw()         

         pygame.display.flip()

    def _ship_hit(self, hit_alien):
        """respond to the ship being hit by and alien"""
        if self.stats.ships_left > 0:
           # Decrement ships_left, and update scorebord
           self.stats.ships_left -= 1
           self.sb.prep_ships()  
           if self.game_mode == "FREE":
 
            # get rid of bullets and aliens
                self.bullets.empty()
                self.aliens.empty()

           #create a new fleet and center the ship
                self._create_fleet()
                self.ship.center_ship()

                # Pause
                sleep(0.5)
           elif self.game_mode == "STORY":
                if hit_alien:
                    self.aliens.remove(hit_alien)
                return

        else:
            self.game_mode = "MENU"
            pygame.mouse.set_visible(True)
            pygame.mixer.music.stop()

if __name__ == '__main__':
    # Make a game istance, and run the game.
    ai = AlienInvasion()
    ai.run_game()