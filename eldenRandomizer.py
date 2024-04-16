import pygame
from pygame.locals import *
import random

# pygame setup
pygame.init()
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))

# setting font
font = pygame.font.Font("fonts\Mantinia Regular.otf", 48)

class EldenRandom():
    def __init__(self, randAttribute = random.randrange(0,255), randColor = pygame.Color(0,0,0), randCol_r = pygame.Color.r(0), randCol_g = pygame.Color.g(0), randCol_b = pygame.Color.b(0)):
        self.randAttribute = randAttribute
        self.randColor = randColor
        self.randCol_r = randCol_r
        self.randCol_g = randCol_g
        self.randCol_b = randCol_b
        


def main():
    # Game loop
    running = True
    while running:

        # Event Handler
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()
    
    pygame.QUIT

if __name__ == "__main__":
    main()