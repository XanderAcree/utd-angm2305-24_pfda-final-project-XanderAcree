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
font = pygame.font.Font('fonts/Garamond Premier Pro/Garamond Premier Pro Regular.ttf', 24)
button_font = pygame.font.Font('fonts/Garamond Premier Pro/Garamond Premier Pro Regular.ttf', 27)

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

detailed_appearance_img = pygame.image.load('images/ER_detailedAppearance.png').convert_alpha()
detailed_appearance_button = button.Button((detailed_appearance_img.get_width()/2) - (detailed_appearance_img.get_width()/3) + 77,
                              213+(60*5),detailed_appearance_img,1)

age_img = pygame.image.load('images/ER_age.png').convert_alpha()
age_button = button.Button((age_img.get_width()/2) - (age_img.get_width()/3) + (77*2),
                              213+(60*6),age_img,1)

voice_img = pygame.image.load('images/ER_voice.png').convert_alpha()
voice_button = button.Button((voice_img.get_width()/2) - (voice_img.get_width()/3) + (77*2),
                              213+(60*7),voice_img,1)

skinCol_img = pygame.image.load('images/ER_skincol.png').convert_alpha()
skinCol_button = button.Button((skinCol_img.get_width()/2) - (skinCol_img.get_width()/3) + (77*2),
                              213+(60*8),skinCol_img,1)

def main():
    # Game loop
    running = True
    clock = pygame.time.Clock()
    attributes = EldenRandom.EldenRandom.returnAll()

    origin_results = button_font.render(attributes[0], True, (200,200,198))
    origin_w, origin_h = button_font.size(attributes[0])

    bodytype_results = button_font.render(attributes[1], True, (200,200,198))
    bodytype_w, bodytype_h = button_font.size(attributes[1])

    keepsake_results = button_font.render(attributes[2], True, (200,200,198))
    keepsake_w, keepsake_h = button_font.size(attributes[2])

    age_results = button_font.render(attributes[3], True, (200,200,198))
    age_w, age_h = button_font.size(attributes[3])

    voice_results = button_font.render(attributes[4], True, (200,200,198))
    voice_w, voice_h = button_font.size(attributes[4])

    #skinCol = pygame.draw.rect(screen,attributes[5],(505,401,398,31))

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
            screen.blit(origin_results, 
                        (((origin_img.get_width())*(1-0.44326617179)) + (199) + (origin_w/2),
                        213+(60*1)+(origin_h/2.5)))
            
            bodytype_button.draw(screen)
            screen.blit(bodytype_results, 
                        (((bodytype_img.get_width())*(1-0.44326617179)) + (199) + (bodytype_w/2),
                        213+(60*2)+(bodytype_h/2.5)))
            
            keepsake_button.draw(screen)
            screen.blit(keepsake_results, 
                        (((keepsake_img.get_width())*(1-0.44326617179)) + (199) + (keepsake_w/2),
                        213+(60*3)+(keepsake_h/2.5)))
            
            detailed_appearance_button.draw(screen)

            age_button.draw(screen)
            screen.blit(age_results, 
                        (((age_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336)) + (199) + (age_w/2),
                        213+(60*6)+(age_h/2.5)))
            
            voice_button.draw(screen)
            screen.blit(voice_results, 
                        (((voice_img.get_width())*(1-0.44326617179)) + (77/(1-0.38693467336)) + (199) + (voice_w/2),
                        213+(60*7)+(voice_h/2.5)))
            skinCol_x = 505 - 42 + 154 + (77/2) + 5 + (77/(1))
            skinCol_y = 401+40-(age_img.get_height()/2) + (60*5)

            skinCol_button.draw(screen)
            pygame.draw.rect(screen,attributes[5],(skinCol_x,skinCol_y,380,31))
            
        elif randomize_button.draw(screen) == False and detailed_appearance_button.draw(screen) == False:
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