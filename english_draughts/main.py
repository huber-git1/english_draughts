import pygame
from checkers.board import *
from checkers.values import *
from checkers.board import *
win = pygame.display.set_mode((WIDTH, HEIGHT))

def main(list1,list2,list3,list4):
    initial_coin_list = list1
    initial_coin_type_list = list2
    final_coin_list = list3
    final_coin_type_list = list4
    running = True
    board = Board()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        board.draw_initial_coins(win,initial_coin_list,initial_coin_type_list)
        board.draw_final_coins(win,final_coin_list, final_coin_type_list)
        pygame.display.update()
    pygame.quit()

class Game:
    def __init__(self,coin,moves):
        self.present_move = coin
        self.no_of_moves = moves

def moves_input(game):
    COIN_POS_ON_BOARD = [[0, 1, 0, 2, 0, 3, 0, 4], [5, 0, 6, 0, 7, 0, 8, 0], [0, 9, 0, 10, 0, 11, 0, 12],
                         [13, 0, 14, 0, 15, 0, 16, 0],
                         [0, 17, 0, 18, 0, 19, 0, 20], [21, 0, 22, 0, 23, 0, 24, 0],
                         [0, 25, 0, 26, 0, 27, 0, 28],
                         [29, 0, 30, 0, 31, 0, 32, 0]]
    COIN_TYPE_DIRECTION = {1 : BLACK, -1 : WHITE}
    game = game
    input_move_type_1 = {}  # type_1 is just moving the coin diagonally from one sqaure to other
    input_move_type_2 = {}   #type_2 is to jump over the coins
    initial_coin_list = []
    final_coin_list = []
    jump_coin_list = []
    initial_coin_direction_list = []
    final_coin_direction_list = []
    jump_coin_direction_list = []
    initial_coin_type_list = []
    final_coin_type_list = []
    jump_coin_type_list = []
    restricting_coins_for_move_2 = []
    restricting_coins_type_for_move_2 = []
    inter_jump_positions = []
    temp = []
    move = None
    direction = 0
    #seperatinng the two types of moves
    for i in range(game.no_of_moves):
        temp.append(input().split())

        # dividing the two tyepe of moves
    for i in range(len(temp)):
        if "-" in temp[i]:
            input_move_type_1[i + 1] = temp[i]
        elif "*" in temp[i]:
            input_move_type_2[i + 1] = temp[i]

    #finding the position of coins
    for i in range(len(temp)):
        #logic for type 1 move
        if i+1 in input_move_type_1:
            move = temp[i]
            #direction of coin
            if int(move[0]) < int(move[2]):
                direction = 1
            elif int(move[0]) > int(move[2]):
                direction = -1
            #adding initial and final position to the list
            if (int(move[0]) not in initial_coin_list) :
                initial_coin_list.append(int(move[0]))
                initial_coin_direction_list.append(direction)
                if direction == -1:
                    if game.present_move == "W":
                        initial_coin_type_list.append("W")
                    elif game.present_move == "B":
                        initial_coin_type_list.append("B")
                if direction == 1:
                    if game.present_move == "B":
                        initial_coin_type_list.append("B")
                    elif game.present_move == "W":
                        initial_coin_type_list.append("W")

            if int(move[2]) not in final_coin_list:
                final_coin_list.append(int(move[2]))
                final_coin_direction_list.append(direction)
                final_coin_type_list.append(initial_coin_type_list[initial_coin_list.index(int(move[0]))])

            #changing the coin
            if game.present_move == "W":
                game.present_move = "B"
            elif game.present_move == "B":
                game.present_move = "W"

        #position finding of coins for type 2 move
        elif i + 1 in input_move_type_2:
            move = temp[i]
            initial_position = int(move[0])
            final_to_position = int(move[-1])
            if initial_position < final_to_position:
                direction = 1
            if initial_position > final_to_position:
                direction = -1
            #finding the jump coins
            jump_coin_list1 = []
            jump_coin_direction_list1 = []
            j = 0
            while j < len(move) - 1:
                from_position = int(move[j])
                to_position = int(move[j + 2])
                # direction of coin
                if from_position < to_position:
                    direction = 1
                elif from_position > to_position:
                    direction = -1
                inter_jump_positions.append(to_position)

                row_1 = [COIN_POS_ON_BOARD.index(row) for row in COIN_POS_ON_BOARD if from_position in row]
                col_1 = [row.index(from_position) for row in COIN_POS_ON_BOARD if from_position in row]
                row_2 = [COIN_POS_ON_BOARD.index(row) for row in COIN_POS_ON_BOARD if to_position in row]
                col_2 = [row.index(to_position) for row in COIN_POS_ON_BOARD if to_position in row]
                jump_coin = COIN_POS_ON_BOARD[(row_1[0] + row_2[0]) // 2][(col_1[0] + col_2[0]) // 2]

                if jump_coin not in jump_coin_list:
                    jump_coin_list.append(jump_coin)
                    jump_coin_direction_list.append(direction)
                    if game.present_move == "B":
                        jump_coin_type_list.append("W")
                    elif game.present_move == "W":
                        jump_coin_type_list.append("B")
                    jump_coin_list1.append(jump_coin)
                    jump_coin_direction_list1.append(direction)
                j += 2

            # adding initial and final positions to lists
            if initial_position :
                initial_coin_list.append(initial_position)
                initial_coin_direction_list.append(direction)
                if jump_coin_direction_list1.count(-1) == len(jump_coin_direction_list1):
                    if game.present_move == "W":
                        initial_coin_type_list.append("W")
                    elif game.present_move == "B":
                        initial_coin_type_list.append("B")
                elif jump_coin_direction_list1.count(-1) != len(jump_coin_direction_list1):
                    if game.present_move == "B":
                        initial_coin_type_list.append("B")
                    if game.present_move == "W":
                        initial_coin_type_list.append("W")
                elif jump_coin_direction_list1.count(1) == len(jump_coin_direction_list1):
                    if game.present_move == "B":
                        initial_coin_type_list.append("B")
                    if game.present_move == "W":
                        initial_coin_type_list.append("W")
                elif jump_coin_direction_list1.count(1) != len(jump_coin_direction_list1):
                    if game.present_move == "B":
                        initial_coin_type_list.append("B")
                    if game.present_move == "W":
                        initial_coin_type_list.append("W")

            if final_to_position not in final_coin_list:
                final_coin_list.append(final_to_position)
                final_coin_direction_list.append(direction)
                final_coin_type_list.append(initial_coin_type_list[initial_coin_list.index(initial_position)])

            #finding neighbouring coins for the end coin
            end_coin_row = [COIN_POS_ON_BOARD.index(row) for row in COIN_POS_ON_BOARD if final_to_position in row]
            end_coin_col = [row.index(final_to_position) for row in COIN_POS_ON_BOARD if final_to_position in row]
            ULC_R, ULC_C = end_coin_row[0] - 1, end_coin_col[0] - 1  # ULC_R = UPPER_LEFT_COIN ROW FOR END COIN,ULC_C = UPPER_LEFT_COIN COLUMN FOR END COIN
            URC_R, URC_C = end_coin_row[0] - 1, end_coin_col[0] + 1  # URC_R = UPPER_RIGHT_COIN ROW FOR END COIN,URC_C = UPPER_RIGHT_COIN COLUMN FOR END COIN
            DLC_R, DLC_C = end_coin_row[0] + 1, end_coin_col[0] - 1  # DLC_R = DOWN_LEFT_COIN ROW FOR END COIN, DLC_C = DOWN_LEFT_COIN COLUMN FOR END COIN
            DRC_R, DRC_C = end_coin_row[0] + 1, end_coin_col[0] + 1  # DLC_R = DOWN_RIGHT_COIN ROW FOR END COIN, DLC_C = DOWN_RIGHT_COIN COLUMN FOR END COIN

            DULC_R, DULC_C = end_coin_row[0] - 2, end_coin_col[0] - 2  # DULC_R = DIAGONAL COIN ROW FOR ULC,DULC_C = DIAGONAL COIN COLUMN FOR ULC
            DURC_R, DURC_C = end_coin_row[0] - 2, end_coin_col[0] + 2  # DURC_R = DIAGONAL COIN ROW FOR URC,DURC_C = DIAGONAL COIN COLUMN FOR URC
            DDLC_R, DDLC_C = end_coin_row[0] + 2, end_coin_col[0] - 2  # DDLC_R = DIAGONAL COIN ROW FOR DLC,DDLC_C = DIAGONAL COIN COLUMN FOR DLC
            DDRC_R, DDRC_C = end_coin_row[0] + 2, end_coin_col[0] + 2  # DDRC_R = DIAGONAL COIN ROW FOR DRC,DDRC_C = DIAGONAL COIN COLUMN FOR DRC

            neighbour_1, neighbour_2, neighbour_3, neighbour_4 = [], [], [], []
            if ULC_R < ROWS and ULC_C < COLS:
                neighbour_1.append(COIN_POS_ON_BOARD[ULC_R][ULC_C])
                if DULC_R < ROWS and DULC_C < COLS:
                    neighbour_1.append(COIN_POS_ON_BOARD[DULC_R][DULC_C])
                else:
                    neighbour_1.append(0)
            if URC_R < ROWS and URC_C < COLS:
                neighbour_2.append(COIN_POS_ON_BOARD[URC_R][URC_C])
                if DURC_R < ROWS and DURC_C < COLS:
                    neighbour_2.append(COIN_POS_ON_BOARD[DURC_R][DURC_C])
                else:
                    neighbour_2.append(0)
            if DLC_R < ROWS and DLC_C < COLS:
                neighbour_3.append(COIN_POS_ON_BOARD[DLC_R][DLC_C])
                if DDLC_R < ROWS and DDLC_C < COLS:
                    neighbour_3.append(COIN_POS_ON_BOARD[DDLC_R][DDLC_C])
                else:
                    neighbour_3.append(0)
            if DRC_R < ROWS and DRC_C < COLS:
                neighbour_4.append(COIN_POS_ON_BOARD[DRC_R][DRC_C])
                if DDRC_R < ROWS and DDRC_C < COLS:
                    neighbour_4.append(COIN_POS_ON_BOARD[DDRC_R][DDRC_C])
                else:
                    neighbour_4.append(0)

            #finding the restricting coins for the end coin
            if final_to_position in final_coin_list and final_coin_type_list[i] == "W" and final_coin_direction_list[i] == -1:
                if len(neighbour_1) != 0 and neighbour_1[1] not in inter_jump_positions:
                    if neighbour_1[1] != 0 :
                        restricting_coins_for_move_2.append(neighbour_1[1])
                        restricting_coins_type_for_move_2.append("B")
                if len(neighbour_2) != 0 and neighbour_2[1] not in inter_jump_positions:
                    if neighbour_2[1] != 0:
                        restricting_coins_for_move_2.append(neighbour_2[1])
                        restricting_coins_type_for_move_2.append("B")
                if len(neighbour_3) != 0 and neighbour_3[1] not in inter_jump_positions:
                    if neighbour_3[1] != 0:
                        restricting_coins_for_move_2.append(neighbour_3[1])
                        restricting_coins_type_for_move_2.append("B")
                if len(neighbour_4) != 0 and neighbour_4[1] not in inter_jump_positions:
                    if neighbour_4 != 0:
                        restricting_coins_for_move_2.append(neighbour_4[1])
                        restricting_coins_type_for_move_2.append("B")

            if final_to_position in final_coin_list and final_coin_type_list[i] == "w" and final_coin_direction_list[i] == -1:
                if len(neighbour_1) != 0 and neighbour_1[1] not in inter_jump_positions :
                    if neighbour_1[1] != 0:
                        restricting_coins_for_move_2.append(neighbour_1[1])
                        restricting_coins_type_for_move_2.append("B")
                if len(neighbour_2) != 0 and neighbour_2[1] not in inter_jump_positions:
                    if neighbour_2[1] != 0:
                        restricting_coins_for_move_2.append(neighbour_2[1])
                        restricting_coins_type_for_move_2.append("B")

            if final_to_position in final_coin_list and final_coin_type_list[i] == "B" and final_coin_direction_list[i] == -1 :
                if len(neighbour_1) != 0 and neighbour_1[1] not in inter_jump_positions :
                    if neighbour_1[1] != 0:
                        restricting_coins_for_move_2.append(neighbour_1[1])
                        restricting_coins_type_for_move_2.append("W")
                if len(neighbour_2) != 0 and (neighbour_2[1] not in inter_jump_positions) :
                    if neighbour_2[1] != 0:
                        restricting_coins_for_move_2.append(neighbour_2[1])
                        restricting_coins_type_for_move_2.append("W")
                if len(neighbour_3) != 0 and neighbour_3[1] not in inter_jump_positions :
                    if neighbour_3[1] != 0:
                        restricting_coins_for_move_2.append(neighbour_3[1])
                        restricting_coins_type_for_move_2.append("W")
                if len(neighbour_4) != 0 and neighbour_4[1] not in inter_jump_positions :
                    if neighbour_4[1] != 0:
                        restricting_coins_for_move_2.append(neighbour_4[1])
                        restricting_coins_type_for_move_2.append("W")

            if final_to_position in final_coin_list and final_coin_type_list[i] == "b" and final_coin_direction_list[i] == -1:
                if len(neighbour_3) != 0 and neighbour_3[1] not in inter_jump_positions:
                    if neighbour_3[1] != 0:
                        restricting_coins_for_move_2.append(neighbour_3[1])
                        restricting_coins_type_for_move_2.append("W")
                if len(neighbour_4) != 0 and neighbour_4[1] not in inter_jump_positions :
                    if neighbour_4[1] != 0:
                        restricting_coins_for_move_2.append(neighbour_4[1])
                        restricting_coins_type_for_move_2.append("W")

            if game.present_move == "W":
                game.present_move = "B"
            elif game.present_move == "B":
                game.present_move = "W"

    final_initial_coin_list = []
    final_initial_coin_type_list = []
    for i in range(len(initial_coin_list) ):
        temp = final_coin_list[0:i+1]
        if initial_coin_list[i] not in temp and initial_coin_list[i] not in final_initial_coin_list:
            final_initial_coin_list.append(initial_coin_list[i])
            final_initial_coin_type_list.append(initial_coin_type_list[initial_coin_list.index(initial_coin_list[i])])
    for i in restricting_coins_for_move_2:
        if i not in inter_jump_positions and i not in final_coin_list:
            final_initial_coin_list.append(i)
            final_initial_coin_type_list.append(initial_coin_type_list[restricting_coins_for_move_2.index(i)])
    for i in jump_coin_list:
        if i not in final_coin_list and i not in final_initial_coin_list:
            final_initial_coin_list.append(i)
            final_initial_coin_type_list.append(jump_coin_type_list[jump_coin_list.index(i)])

    final_final_coin_list = []
    final_final_coin_type_list = []
    for i in final_coin_list:
        if i not in jump_coin_list :
            if i in initial_coin_list and initial_coin_list.count(i) == 1:
                final_final_coin_list.append(i)
                final_final_coin_type_list.append(initial_coin_type_list[initial_coin_list.index(i)])
            if i not in initial_coin_list:
                final_final_coin_list.append(i)
                final_final_coin_type_list.append(final_coin_type_list[final_coin_list.index(i)])
    for i in restricting_coins_for_move_2:
        if i not in final_final_coin_list and i not in inter_jump_positions:
            final_final_coin_list.append(i)
            final_final_coin_type_list.append(restricting_coins_type_for_move_2[restricting_coins_for_move_2.index(i)])

    main(final_initial_coin_list,final_initial_coin_type_list,final_final_coin_list,final_final_coin_type_list)

data =list(input().split())
game =Game(data[0], int(data[1]))
moves_input(game)
