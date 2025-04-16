# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import circleshape
from constants import *
from player import *


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def main():
    print(f"Starting Asteroids!\n"
            f"Screen width: {SCREEN_WIDTH}\n"
            f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick()


# ensures this wont run unless its executed directly
# and imports wont make daisy chains of bs
if __name__ == "__main__":
    main()