import pygame
from .values import *
class Coin:
    PADDING = 5
    OUTLINE = 2

    def _init_(self,color,row,col):
        self.color = color
        self.radius = 0
        self.row = row
        self.col = col
        self.men = None
        self.king = None
        if self.color == WHITE:
            self.direction = -1
        else:
            self.direction = 1
        self.x = 0
        self.y = 0
        #self.position()

    def position(self):
        self.x = self.row * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = self.col * SQUARE_SIZE + SQUARE_SIZE // 2

    def make_men(self):
        self.men = True

    def make_king(self):
        self.king = True

    def coin_radius(self):
        self.radius = SQUARE_SIZE // 2 - self.PADDING

    def get_radius(self):
        return self.radius

    def draw_coin(self,win):
        pygame.draw.circle(win, GRAY, (self.x, self.y), self.get_radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.get_radius)

    def _repr_(self):
        return str(self.color)