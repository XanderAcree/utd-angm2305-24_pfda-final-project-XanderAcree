import pygame
from pygame.locals import *
import button
import EldenRandom
import moviepy

# pygame setup
pygame.init()

pygame.display.set_caption("ELDEN RING CHARACTER ATTRIBUTE RANDOMIZER")

#Base Window Settings
width, height = 1920, 1200
resolution = (width, height)
flags = pygame.SCALED
screen = pygame.display.set_mode(resolution, flags, vsync=1)

# setting font
title_font = pygame.font.Font('fonts/Mantinia Regular.otf', 96)
font = pygame.font.Font('fonts/Mantinia Regular.otf', 24)
button_font = pygame.font.Font('fonts/Mantinia Regular.otf', 27)

#Images, etc.
bg_image = pygame.image.load('images/elden ring.png')
title_img = pygame.image.load('images/title.png')
#textShadow = pygame.image.load('images/textShadow.png')
#shadowSize = textShadow.get_width(), textShadow.get_height()
randResults_grad = pygame.image.load('images/randomizerScreen_gradient.png')
#randResults_screen = pygame.transform.scale(randResults_grad, (1920, 1200))

#Button Class
#class Button():
#    def __init__(self, x, y, image):
#        self.image = image
#        self.rect = self.image.get_rect()
#        self.rect.topleft = (x,y)
#    
#    def draw(self, _x, _y):
#        #Draw button on screen
#        self._pos = (_x, _y)
#        screen.blit(self.image, self._pos)


##Randomize Button
randomize_img = pygame.image.load('images/randomizeButton/randomizeButton_00012.png').convert_alpha()
randomize_button = button.Button(((resolution[0]/2) - (randomize_img.get_width()/2)), 
                                 ((resolution[1]/2) - (randomize_img.get_height()/2)), randomize_img, 1)
origin_img = pygame.image.load('images/ER_origin.png').convert_alpha()
origin_button = button.Button((origin_img.get_width()/2) - (origin_img.get_width()/3) + 77,
                              213+60,origin_img,1)
bodytype_img = pygame.image.load('images/ER_bodytype.png').convert_alpha()
bodytype_button = button.Button((bodytype_img.get_width()/2) - (bodytype_img.get_width()/3) + 77,
                              213+(60*2),bodytype_img,1)
keepsake_img = pygame.image.load('images/ER_keepsake.png').convert_alpha()
keepsake_button = button.Button((keepsake_img.get_width()/2) - (keepsake_img.get_width()/3) + 77,
                              213+(60*3),keepsake_img,1)

def main():
    # Game loop
    running = True
    clock = pygame.time.Clock()
    attributes = EldenRandom.EldenRandom.returnAll()
    titlePos = ((resolution[0]/2) - (title_img.get_width()/2), 0 + (title_img.get_height()/4))
    isRandButtonClicked = False
    while running:
        #Randomizer Results Screen
        if randomize_button.draw(screen) == True or isRandButtonClicked == True:
            isRandButtonClicked = True
            screen.fill((24,21,15))
            screen.blit(randResults_grad, (((resolution[0]) - (randResults_grad.get_width() - 190)),
                                           ((resolution[1]) - (randResults_grad.get_height() - 120))))
            origin_button.draw(screen)
            origin_results = button_font.render(attributes[0], True, (200,200,198))
            screen.blit(origin_results, 
                        ((origin_img.get_width()/2) - (origin_img.get_width()/3) + 77 + ((origin_img.get_width()/4)*3),
                        213+60))
            bodytype_button.draw(screen)
            bodytype_results = button_font.render(attributes[1], True, (200,200,198))
            keepsake_button.draw(screen)

        elif randomize_button.draw(screen) == False:
            screen.fill((0,0,0))
            #Background and Title
            bg_image.set_alpha(50)
            screen.blit(bg_image, (((resolution[0]/2) - (bg_image.get_width()/2)),((resolution[1]/2) - (bg_image.get_height()/2))))
            #screen.blit(bg_image, (0,0))
            
            screen.blit(title_img, (titlePos))

            # Randomizer text under title
            title_text = title_font.render("Attribute Randomizer", True, (228, 190, 125))
            titleRand_w, titleRand_h = title_text.get_width(), title_text.get_height()
            #titleRand_shadow = pygame.transform.scale(textShadow, ((titleRand_w*2), titleRand_h*1.5))

            #screen.blit(titleRand_shadow, ((resolution[0]/2) - (titleRand_shadow.get_width())/2, titlePos[1] + (titleRand_h*1.25)))

            screen.blit(title_text, ((resolution[0]/2) - titleRand_w/2, titlePos[1] + (titleRand_h*1.5)))
            randomize_button.draw(screen)

            #randomize_button.draw(((resolution[0]/2) - (randomize_img.get_width()/2)), ((resolution[1]/2) - (randomize_img.get_height()/2)))

        # Event Handler
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT: #or (event.type == KEYDOWN and pygame.key.get_pressed(K_q))
                running = False
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_q]:
                isRandButtonClicked = False

        pygame.display.update()

        # flip() to display everything on screen
        #pygame.display.flip


        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()