from textwrap import fill
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init() 
    
    clock = pygame.time.Clock() 
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    my_player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    new_asteroid_field = AsteroidField()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")
        for drawable_object in drawable:
            drawable_object.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(my_player):
                print("Game over!")
                sys.exit()
        pygame.display.flip()   
        dt = clock.tick(60)/1000  # Limit to 60 FPS

if __name__ == "__main__":
    main()
