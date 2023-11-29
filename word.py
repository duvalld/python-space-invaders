import pygame
from random import choice

class Word(pygame.sprite.Sprite):
    def __init__(self, x, y, myster_word):
        super().__init__()
       
        
        # create a font object
        font = pygame.font.Font(None, 36)
        # create a surface with the rendedered text
        self.image = font.render(myster_word, True, "black", "white")
        # get the rectangle that encloses the text surface
        self.rect = self.image.get_rect(topleft = (x, y))
        
        