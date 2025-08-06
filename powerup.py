from circleshape import *
from constants import *


class Powerup(CircleShape):
    
    SHIELD = ("shield", None)
    RAPID_FIRE = ("rapid fire", 5.0)
    POWERS = [RAPID_FIRE, SHIELD]

    def __init__(self, x, y, power, duration = None):
        super().__init__(x, y, POWERUP_RADIUS)
        self.power = power
        self.duration = duration

    def draw(self, screen):
        if self.power == self.SHIELD[0]:
            pygame.draw.circle(screen, 'yellow', self.position, self.radius, width = 2)
        if self.power == self.RAPID_FIRE[0]:
            pygame.draw.circle(screen, 'red', self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    

