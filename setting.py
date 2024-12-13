class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

    def __init__(self):

        # Ship settings
        self.ship_speed = 1.5

    def __init__(self):
        # Ship settings
        self.ship_speed = 1.5
        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)


    # Bullet settings

        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

def __init__(self):
# Alien settings
    self.alien_speed = 1.0

# Alien settings
    self.alien_speed = 1.0
    self.fleet_drop_speed = 10
# fleet_direction of 1 represents right; -1 represents left.
    self.fleet_direction = 1

def check_edges(self):
    """Return True if alien is at edge of screen."""
    screen_rect = self.screen.get_rect()
    return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
def update(self):
    """Move the alien right or left."""
    self.x += self.settings.alien_speed * self.settings.fleet_direction
    self.rect.x = self.x

def _check_fleet_edges(self):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in self.aliens.sprites():
        if alien.check_edges():
            self._change_fleet_direction()
            break
def _change_fleet_direction(self):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in self.aliens.sprites():
        alien.rect.y += self.settings.fleet_drop_speed
    self.settings.fleet_direction *= -1  

def _update_aliens(self):
    """Check if the fleet is at an edge, then update positions."""
    self._check_fleet_edges()
    self.aliens.update()

def _update_bullets(self):
    """Update position of bullets and get rid of old bullets."""
# Check for any bullets that have hit aliens.
# If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)


        # Bullet settings
    self.bullet_speed = 2.5
    self.bullet_width = 3

def _update_bullets(self):
# Get rid of bullets that have disappeared.
    for bullet in self.bullets.copy():
        if bullet.rect.bottom <= 0:
            self.bullets.remove(bullet)
    self._check_bullet_alien_collisions()
def _check_bullet_alien_collisions(self):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(
    self.bullets, self.aliens, True, True)

    if not self.aliens:
# Destroy existing bullets and create new fleet.
        self.bullets.empty()
        self._create_fleet()

# Ship settings
    self.ship_speed = 1.5
    self.ship_limit = 3
