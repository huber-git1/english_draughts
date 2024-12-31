import pygame
from checkers.coin import *
from checkers.values import *

class Board:

    def draw_initial_squares(self,win):
        win.fill(BROWN)
        for row in range(8):
            for col in range(row%2,8,2):
                pygame.draw.rect(win, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_final_squares(self,win):
        for row in range(10,18):
            for col in range(row%2,18,2):
                pygame.draw.rect(win, WHITE,(row * SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_initial_coins(self,win,list1,list2):
        self.draw_initial_squares(win)
        board = Board()
        coin_pos = [[0, 1, 0, 2, 0, 3, 0, 4], [5, 0, 6, 0, 7, 0, 8, 0], [0, 9, 0, 10, 0, 11, 0, 12],[13, 0, 14, 0, 15, 0, 16, 0],
                    [0, 17, 0, 18, 0, 19, 0, 20], [21, 0, 22, 0, 23, 0, 24, 0],[0, 25, 0, 26, 0, 27, 0, 28],[29, 0, 30, 0, 31, 0, 32, 0]]
        for row in range(8):
            for col in range(8):
                if coin_pos[row][col] != 0 and coin_pos[row][col] in list1:
                    if list2[list1.index(coin_pos[row][col])] == "W":
                        coin = Coin(WHITE,col,row)
                        coin.draw_coin(win)
                    else:
                        coin = Coin(BLACK,col,row)
                        coin.draw_coin(win)

    def draw_final_coins(self,win,list1,list2):
        self.draw_final_squares(win)
        board = Board()
        coin_pos = [[0, 1, 0, 2, 0, 3, 0, 4], [5, 0, 6, 0, 7, 0, 8, 0], [0, 9, 0, 10, 0, 11, 0, 12],
                    [13, 0, 14, 0, 15, 0, 16, 0],
                    [0, 17, 0, 18, 0, 19, 0, 20], [21, 0, 22, 0, 23, 0, 24, 0], [0, 25, 0, 26, 0, 27, 0, 28],
                    [29, 0, 30, 0, 31, 0, 32, 0]]
        for row in range(8):
            for col in range(8):
                if coin_pos[row][col] != 0 and coin_pos[row][col] in list1:
                    if list2[list1.index(coin_pos[row][col])] == "W":
                        coin = Coin(WHITE, col+10, row)
                        coin.draw_coin(win)
                    else:
                        coin = Coin(BLACK, col+10, row)
                        coin.draw_coin(win)