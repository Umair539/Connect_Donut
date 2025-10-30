import pygame
import os

class Piece(object):
    img1 = pygame.image.load(os.path.join('Sprites', 'choccy.png'))
    img2 = pygame.image.load(os.path.join('Sprites', 'pink.png'))
    img=[img1,img2]
    
    def __init__(self, x, y, i):
        self.x = x
        self.y = y
        self.i = i
        
    def draw(self, win):
        win.blit(self.img[self.i], (self.x, self.y))