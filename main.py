# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
import circleshape
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
field = AsteroidField()


def main():
    print(f"Starting Asteroids!\n"
            f"Screen width: {SCREEN_WIDTH}\n"
            f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000.0
        updatable.update(dt)

        for asteroid in asteroids:
            if player.chk_collision(asteroid) == True:
                print("Game over!")
                sys.exit()
        for d in drawable:
            d.draw(screen) 
        pygame.display.flip()
       
       


# ensures this wont run unless its executed directly
# and imports wont make daisy chains of bs
if __name__ == "__main__":
    main()