from textwrap import fill
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from powerup import Powerup
from powerupfield import PowerupField
import sys
from shot import Shot
import time

def main():
    pygame.init() 
    font = pygame.font.Font(None, 36)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() 
    
    dt = 0
    score = 0
    start_time = time.time()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Powerup.containers = (powerups, updatable, drawable)
    PowerupField.containers = (updatable)
   
    my_player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    new_asteroid_field = AsteroidField()
    new_powerup_field = PowerupField()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")
        for drawable_object in drawable:
            drawable_object.draw(screen)
        updatable.update(dt)
        for asteroid in list(asteroids):
            if asteroid.collision_check(my_player):
                print(f"Player collision! Asteroid at {asteroid.position}, radius: {asteroid.radius}")
                print(f"Player at {my_player.position}")
                print("Game over!")
                print(f"Score: {score}")
                sys.exit()
        for asteroid in list(asteroids):
            for shot in shots:
                if asteroid.collision_check(shot):
                    new_asteroids = asteroid.split()
                    shot.kill()
                    score += 10
                    for new_asteroid in new_asteroids:
                        asteroids.add(new_asteroid)
        for powerup in list(powerups):
            if powerup.collision_check(my_player):
                powerup.kill()
                my_player.apply_powerup(powerup.power, powerup.duration)
        current_time = time.time()
        time_bonus = int((current_time - start_time) * 2)
        total_score = score + time_bonus

        score_text = font.render(f"Score: {total_score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()   
        dt = clock.tick(60)/1000  # Limit to 60 FPS

if __name__ == "__main__":
    main()
