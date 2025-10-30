import pygame
import os


class Piece(object):
    img1 = pygame.image.load(os.path.join("Sprites", "choccy.png"))
    img2 = pygame.image.load(os.path.join("Sprites", "pink.png"))
    img = [img1, img2]

    def __init__(self, x, y, i):
        self.x = x  # x coordinate
        self.y = y  # y coordinate
        self.i = i  # image index in img

    def draw(self, win):
        win.blit(self.img[self.i], (self.x, self.y))
