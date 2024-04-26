import pygame, sys
from pygame.locals import *
from PIL import Image, ImageSequence
class randButton(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        #sprites = []
        #gif = Image.open(f'{seq_path}')
        #for frame_index in range(gif.n_frames):
        #    gif.seek(frame_index)
        #    frame_rgba = gif.convert("RGBA")
        #    pygame_image = pygame.image.fromstring(
        #        frame_rgba.tobytes(), frame_rgba.size, frame_rgba.mode
        #    )
        #    sprites.append(pygame_image)
        #return sprites
        self.sprites = []
        self.image = pygame.image.load("randomizeButton_00000.png")
        i = 0
        for i in range(46):
            if i < 10:
                path_name = "randomizeButton_0000"+str(i)+".png"
            else:
                path_name = "randomizeButton_000"+str(i)+".png"
            image = pygame.image.load(path_name)
            self.sprites.append(image)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]
    
    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]

        