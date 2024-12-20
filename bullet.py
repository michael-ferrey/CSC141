import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):

    def __init__(self, ai_game):

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
        self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

def update(self):
    """Move the bullet up the screen."""
    # Update the exact position of the bullet.
    self.y -= self.settings.bullet_speed
    # Update the rect position.
    self.rect.y = self.y
def draw_bullet(self):
    """Draw the bullet to the screen."""
    pygame.draw.rect(self.screen, self.color, self.rect) 


def _fire_bullet(self):

    if len(self.bullets) < self.settings.bullets_allowed:
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
https://images.app.goo.gl/Bjq7T6Qji4rPhmEf9
