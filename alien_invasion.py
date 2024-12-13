import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
  
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai=AlienInvasion()
    ai.run_game()

def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()
    self.clock = pygame.time.Clock()

def run_game(self):
    """Start the main loop for the game."""
    while True:
        pygame.display.flip()
        self.clock.tick(60)

def __init__(self):
    pygame.display.set_caption("Alien Invasion")

    # Set the background color.
    self.bg_color = (230, 230, 230)

def run_game(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Redraw the screen during each pass through the loop.
    self.screen.fill(self.bg_color)

    # Make the most recently drawn screen visible.
    pygame.display.flip()
    self.clock.tick(60)

import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()
    self.clock = pygame.time.Clock()
    self.settings = Settings()

    self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

def run_game(self):
    # Redraw the screen during each pass through the loop.
    self.screen.fill(self.settings.bg_color)

    # Make the most recently drawn screen visible.
    pygame.display.flip()
    self.clock.tick(60)

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

def __init__(self):
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

def run_game(self):
    # Redraw the screen during each pass through the loop.
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
    self.clock.tick(60)

def run_game(self):
    """Start the main loop for the game."""
    while True:
        self._check_events()

        # Redraw the screen during each pass through the loop.

def _check_events(self):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()\


def run_game(self):
    """Start the main loop for the game."""
    while True:
        self._check_events()
        self._update_screen()
        self.clock.tick(60)

def _check_events(self):

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()
    

def _check_events(self):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
                self.ship.rect.x += 1


                self.ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False

def run_game(self):
    """Start the main loop for the game."""
    while True:
        self._check_events()
        self.ship.update()
        self._update_screen()
        self.clock.tick(60)

def _check_event(self):

    for event in pygame.event.get():
        """Respond to keypresses and mouse events."""
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

def _check_events(self):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            self._check_keyup_events(event)

def _check_keydown_events(self, event):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True

def _check_keyup_events(self, event):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = False

    elif event.key == pygame.K_q:
        sys.exit()
        

def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()
    self.settings = Settings()

    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    self.settings.screen_width = self.screen.get_rect().width
    self.settings.screen_height = self.screen.get_rect().height
    pygame.display.set_caption("Alien Invasion")

from ship import Ship
from bullet import Bullet

def __init__(self):

    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()

def run_game(self):
    """Start the main loop for the game."""
    while True:
        self._check_events()
        self.ship.update()
        self.bullets.update()
        self._update_screen()
        self.clock.tick(60)


def _check_keydown_events(self, event):


    """Create a new bullet and add it to the bullets group."""
    new_bullet = Bullet(self)
    self.bullets.add(new_bullet)

def _update_screen(self):
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill(self.settings.bg_color)
    for bullet in self.bullets.sprites():
        bullet.draw_bullet()
    self.ship.blitme()

    pygame.display.flip()


def run_game(self):
    """Start the main loop for the game."""
    while True:
        self._check_events()
        self.ship.update()
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

        self._update_screen()
        self.clock.tick(60)

    while True:
        self._check_events()
        self.ship.update()
        self._update_bullets()
        self._update_screen()
        self.clock.tick(60)

from bullet import Bullet
from alien import Alien

def __init__(self):
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
    self.aliens = pygame.sprite.Group()
    self._create_fleet()


def _create_fleet(self):
    """Create the fleet of aliens."""
    # Make an alien.
    alien = Alien(self)
    self.aliens.add(alien)

def _update_screen(self):

    self.ship.blitme()
    self.aliens.draw(self.screen)
    pygame.display.flip()


def _create_fleet(self):
    """Create the fleet of aliens."""
# Create an alien and keep adding aliens until there's no room left.
# Spacing between aliens is one alien width.
    alien = Alien(self)
    alien_width = alien.rect.width

    current_x = alien_width
    while current_x < (self.settings.screen_width - 2 * alien_width):
        new_alien = Alien(self)
        new_alien.x = current_x
        new_alien.rect.x = current_x
        self.aliens.add(new_alien)
        current_x += 2 * alien_width


def _create_fleet(self):
    while current_x < (self.settings.screen_width - 2 * alien_width):
        self._create_alien(current_x)
        current_x += 2 * alien_width

def _create_alien(self, x_position):
    """Create an alien and place it in the row."""
    new_alien = Alien(self)
    new_alien.x = x_position
    new_alien.rect.x = x_position
    self.aliens.add(new_alien)

def _create_fleet(self):
    """Create the fleet of aliens."""
# Create an alien and keep adding aliens until there's no room left.
# Spacing between aliens is one alien width and one alien height.
    alien = Alien(self)
    alien_width, alien_height = alien.rect.size
    current_x, current_y = alien_width, alien_height
    while current_y < (self.settings.screen_height - 3 * alien_height):
        while current_x < (self.settings.screen_width - 2 * alien_width):
            self._create_alien(current_x, current_y)
            current_x += 2 * alien_width
# Finished a row; reset x value, and increment y value.
    current_x = alien_width
    current_y += 2 * alien_height

def _create_alien(self, x_position, y_position):
    """Create an alien and place it in the fleet."""
    new_alien = Alien(self)
    new_alien.x = x_position
    new_alien.rect.x = x_position
    new_alien.rect.y = y_position
    self.aliens.add(new_alien)

    while True:
        self._check_events()
        self.ship.update()
        self._update_bullets()
        self._update_aliens()
        self._update_screen()
        self.clock.tick(60)

def _update_aliens(self):
    """Update the positions of all aliens in the fleet."""
    self.aliens.update()


def _update_bullets(self):

    if not self.aliens:
    # Destroy existing bullets and create new fleet.
        self.bullets.empty()
        self._create_fleet()

def _update_aliens(self):

    self.aliens.update()
# Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(self.ship, self.aliens):
        print("Ship hit!!!")

import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship


def __init__(self):
    self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
# Create an instance to store game statistics.
    self.stats = GameStats(self)
    self.ship = Ship(self)


def _ship_hit(self):
    """Respond to the ship being hit by an alien."""
# Decrement ships_left.
    self.stats.ships_left -= 1
# Get rid of any remaining bullets and aliens.
    self.bullets.empty()
    self.aliens.empty()
# Create a new fleet and center the ship.
    self._create_fleet()
    self.ship.center_ship()
    # Pause.
    sleep(0.5)

def _update_aliens(self):
    if pygame.sprite.spritecollideany(self.ship, self.aliens):
        self._ship_hit()

def _check_aliens_bottom(self):
    """Check if any aliens have reached the bottom of the screen."""
    for alien in self.aliens.sprites():
        if alien.rect.bottom >= self.settings.screen_height:
# Treat this the same as if the ship got hit.
            self._ship_hit()
            break

def _update_aliens(self):
# Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(self.ship, self.aliens):
        self._ship_hit()
# Look for aliens hitting the bottom of the screen.
    self._check_aliens_bottom()

def __init__(self):
# Start Alien Invasion in an active state.
    self.game_active = True

def _ship_hit(self):
    """Respond to ship being hit by alien."""
    if self.stats.ships_left > 0:
# Decrement ships_left.
        self.stats.ships_left -= 1
# Pause.
        sleep(0.5)
    else:
        self.game_active = False

def run_game(self):
    """Start the main loop for the game."""
    while True:
        self._check_events()

        if self.game_active:
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()
# Start Alien Invasion in an inactive state.
    self.game_active = False

from game_stats import GameStats
from button import Button

def __init__(self):
    self.game_active = False
# Make the Play button.
    self.play_button = Button(self, "Play")

def _update_screen(self):
    self.aliens.draw(self.screen)
# Draw the play button if the game is inactive.
    if not self.game_active:
        self.play_button.draw_button()

    pygame.display.flip()


def _check_events(self):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mouse_pos = pygame.mouse.get_pos()
            self._check_play_button(mouse_pos)

def _check_play_button(self, mouse_pos):
    """Start a new game when the player clicks Play."""
    if self.play_button.rect.collidepoint(mouse_pos):
        self.game_active = True

def _check_play_button(self, mouse_pos):
    """Start a new game when the player clicks Play."""
    if self.play_button.rect.collidepoint(mouse_pos):
# Reset the game statistics.
        self.stats.reset_stats()
        self.game_active = True

        # Get rid of any remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()
# Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

def _check_play_button(self, mouse_pos):

    """Start a new game when the player clicks Play."""
    button_clicked = self.play_button.rect.collidepoint(mouse_pos)
    if button_clicked and not self.game_active:
    # Reset the game statistics.
        self.stats.reset_stats()

def _check_play_button(self, mouse_pos):
    """Start a new game when the player clicks Play."""
    button_clicked = self.play_button.rect.collidepoint(mouse_pos)
    if button_clicked and not self.game_active:
# Hide the mouse cursor.
        pygame.mouse.set_visible(False)

def _ship_hit(self):
    """Respond to ship being hit by alien."""
    if self.stats.ships_left > 0:
        self.game_active = False
        pygame.mouse.set_visible(True)
