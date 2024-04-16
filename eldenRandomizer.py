import pygame
from pygame.locals import *
import random

# pygame setup
pygame.init()

pygame.display.set_caption("ELDEN RING CHARACTER ATTRIBUTE RANDOMIZER")

#Base Window Settings
width, height = 1920, 1080
resolution = (width, height)
flags = pygame.SCALED
screen = pygame.display.set_mode(resolution, flags, vsync=1)

# setting font
title_font = pygame.font.Font('fonts/Mantinia Regular.otf', 96)
font = pygame.font.Font('fonts/Mantinia Regular.otf', 24)

#Images, etc.
bg_image = pygame.image.load('images/background.jpg')
title_img = pygame.image.load('images/title.png')
textShadow = pygame.image.load('images/textShadow.png')
shadowSize = textShadow.get_width(), textShadow.get_height()

#Button Class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    
    def draw(self, _x, _y):
        #Draw button on screen
        self._pos = (_x, _y)
        screen.blit(self.image, self._pos)


##Randomize Button
randomize_img = pygame.image.load('images/randomizeButton.png').convert_alpha()
randomize_button = Button(randomize_img.get_width(), randomize_img.get_height(), randomize_img)


class EldenRandom():
    def __init__(self, randAttribute = random.randrange(0,255), 
                 randColor = pygame.Color(0,0,0), 
                 randCol_r = 0, 
                 randCol_g = 0, 
                 randCol_b = 0):
        self.randAttribute = randAttribute
        self.randColor = randColor
        self.randCol_r = randCol_r
        self.randCol_g = randCol_g
        self.randCol_b = randCol_b

def main():
    # Game loop
    running = True
    clock = pygame.time.Clock()

    titlePos = ((resolution[0]/2) - (title_img.get_width()/2), 0 + (title_img.get_height()/4))
    
    while running:
        #Background and Title
        screen.blit(bg_image, (0,0))
        screen.blit(title_img, (titlePos))

        # Randomizer text under title
        title_text = title_font.render("Attribute Randomizer", True, (228, 190, 125))
        titleRand_w, titleRand_h = title_text.get_width(), title_text.get_height()
        titleRand_shadow = pygame.transform.scale(textShadow, ((titleRand_w*2), titleRand_h*1.5))

        screen.blit(titleRand_shadow, ((resolution[0]/2) - (titleRand_shadow.get_width())/2, titlePos[1] + (titleRand_h*1.25)))
        screen.blit(title_text, ((resolution[0]/2) - titleRand_w/2, titlePos[1] + (titleRand_h*1.5)))
        randomize_button.draw(((resolution[0]/2) - (randomize_img.get_width()/2)), ((resolution[1]/2) - (randomize_img.get_height()/2)))

        # Event Handler
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT: #or (event.type == KEYDOWN and pygame.key.get_pressed(K_q))
                running = False

        pygame.display.update()

        # flip() to display everything on screen
        #pygame.display.flip


        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()