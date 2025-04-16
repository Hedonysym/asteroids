# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print(f"Starting Asteroids!\n"
            f"Screen width: {SCREEN_WIDTH}\n"
            f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

# ensures this wont run unless its executed directly
# and imports wont make daisy chains of bs
if __name__ == "__main__":
    main()