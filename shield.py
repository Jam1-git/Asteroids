import pygame
from constants import *
from circleshape import *


class Shield(CircleShape):
    def __init__(self, player):
        super().__init__(player.position.x, player.position.y, radius = SHIELD_RADIUS)
        self.player = player

    def draw(self, screen):
        pygame.draw.circle(screen, 'yellow', self.position, self.radius, width = 2)

    def update(self, dt):
        self.position = self.player.position