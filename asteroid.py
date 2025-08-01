from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        for sign in [1, -1]:
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = self.velocity.rotate(angle * sign) * 1.2