import pygame
from constants import *
from circleshape import *
from shot import Shot
from powerup import *

class Player(CircleShape):
    def __init__(self, x, y, active_powerups = None):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.active_powerups = active_powerups or {}

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,'white', self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED *dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.timer < 0 :
            self.shoot()
            if Powerup.RAPID_FIRE[0] in self.active_powerups:
                self.timer = POWER_SHOOT_COOLDOWN
            else:
                self.timer = PLAYER_SHOOT_COOLDOWN
        self.timer -= dt  

        expired_powerups = []
        for powerup in self.active_powerups:
            self.active_powerups[powerup] -= dt
            if self.active_powerups[powerup] <= 0:
                expired_powerups.append(powerup)
            
        for powerup in expired_powerups:
            del self.active_powerups[powerup]

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        new_shot = Shot(self.position[0], self.position[1])
        new_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
    
    def apply_powerup(self, power_type, duration = None):
        if duration:
            self.active_powerups[power_type] = duration
        else:
            self.active_powerups[power_type] = True






