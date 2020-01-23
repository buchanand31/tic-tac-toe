import numpy as np
from copy import deepcopy
from random import randint

# The initial state of the game board is empty with numbers 1-9 representing the places
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# X goes first, so if the player is X, they get first choice
char = input('Do you want to be X\'s or O\'s?\n')

# If they player is X, they can place, otherwise the computer picks a point for X (right now, at random)
def choose_x():
    other_choice = randint(1,9)
    if char == 'X':
        draw_board(board)
        choice = int(input('Where do you want to place your ' + char + '?\n'))
        if choice == 1:
            board[0][0] = char
        elif choice == 2:
            board[0][1] = char
        elif choice == 3:
            board[0][2] = char
        elif choice == 4:
            board[1][0] = char
        elif choice == 5:
            board[1][1] = char
        elif choice == 6:
            board[1][2] = char
        elif choice == 7:
            board[2][0] = char
        elif choice == 8:
            board[2][1] = char
        else:
            board[2][2] = char
    else:
        if other_choice == 1:
            if (board[0][0] == 'X') or (board[0][0] == 'O'):
                choose_x()
            else:
                board[0][0] = 'X'
        elif other_choice == 2:
            if (board[0][1] == 'X') or (board[0][1] == 'O'):
                choose_x()
            else:
                board[0][1] = 'X'
        elif other_choice == 3:
            if (board[0][2] == 'X') or (board[0][2] == 'O'):
                choose_x()
            else:
                board[0][2] = 'X'
        elif other_choice == 4:
            if (board[1][0] == 'X') or (board[1][0] == 'O'):
                choose_x()
            else:
                board[1][0] = 'X'
        elif other_choice == 5:
            if (board[1][1] == 'X') or (board[1][1] == 'O'):
                choose_x()
            else:
                board[1][1] = 'X'
        elif other_choice == 6:
            if (board[1][2] == 'X') or (board[1][2] == 'O'):
                choose_x()
            else:
                board[1][2] = 'X'
        elif other_choice == 7:
            if (board[2][0] == 'X') or (board[2][0] == 'O'):
                choose_x()
            else:
                board[2][0] = 'X'
        elif other_choice == 8:
            if (board[2][1] == 'X') or (board[2][1] == 'O'):
                choose_x()
            else:
                board[2][1] = 'X'
        else:
            if (board[2][2] == 'X') or (board[2][2] == 'O'):
                choose_x()
            else:
                board[2][2] = 'X'
       
# O will then go next
def choose_o():
    other_choice = randint(1, 9)
    if char == 'O':
        draw_board(board)
        choice = int(input('Where do you want to place your ' + char + '?\n'))
        if choice == 1:
            board[0][0] = char
        elif choice == 2:
            board[0][1] = char
        elif choice == 3:
            board[0][2] = char
        elif choice == 4:
            board[1][0] = char
        elif choice == 5:
            board[1][1] = char
        elif choice == 6:
            board[1][2] = char
        elif choice == 7:
            board[2][0] = char
        elif choice == 8:
            board[2][1] = char
        else:
            board[2][2] = char
    else:
        if other_choice == 1:
            if (board[0][0] == 'O') or (board[0][0] == 'X'):
                choose_o()
            else:
                board[0][0] = 'O'
        elif other_choice == 2:
            if (board[0][1] == 'O') or (board[0][1] == 'X'):
                choose_o()
            else:
                board[0][1] = 'O'
        elif other_choice == 3:
            if (board[0][2] == 'O') or (board[0][2] == 'X'):
                choose_o()
            else:
                board[0][2] = 'O'
        elif other_choice == 4:
            if (board[1][0] == 'O') or (board[1][0] == 'X'):
                choose_o()
            else:
                board[1][0] = 'O'
        elif other_choice == 5:
            if (board[1][1] == 'O') or (board[1][1] == 'X'):
                choose_o()
            else:
                board[1][1] = 'O'
        elif other_choice == 6:
            if (board[1][2] == 'O') or (board[1][2] == 'X'):
                choose_o()
            else:
                board[1][2] = 'O'
        elif other_choice == 7:
            if (board[2][0] == 'O') or (board[2][0] == 'X'):
                choose_o()
            else:
                board[2][0] = 'O'
        elif other_choice == 8:
            if (board[2][1] == 'O') or (board[2][1] == 'X'):
                choose_o()
            else:
                board[2][1] = 'O'
        else:
            if (board[2][2] == 'O') or (board[2][2] == 'X'):
                choose_o()
            else:
                board[2][2] = 'O'

# now define a function to let the player choose a move, if X makes a move that fills the board, we want to have the 
# function pass nothing
def select_move():
    choose_x()
    if ((board[0][0] == 'X') or (board[0][0] == 'O')) and ((board[0][1] == 'X') or (board[0][1] == 'O')) and \
    ((board[0][2] == 'X') or (board[0][2] == 'O')) and ((board[1][0] == 'X') or (board[1][0] == 'O')) and \
    ((board[1][1] == 'X') or (board[1][1] == 'O')) and ((board[1][2] == 'X') or (board[1][2] == 'O')) and \
    ((board[2][0] == 'X') or (board[2][0] == 'O')) and ((board[2][1] == 'X') or (board[2][1] == 'O')) and \
    ((board[2][2] == 'X') or (board[2][2] == 'O')):
        pass
    else:
        choose_o()

#next, let's draw the current octothorp
def draw_board(board):
    print('|' + str(board[0][0]) + '|' + str(board[0][1]) + '|' + str(board[0][2]) + '|')
    print('|' + str(board[1][0]) + '|' + str(board[1][1]) + '|' + str(board[1][2]) + '|')
    print('|' + str(board[2][0]) + '|' + str(board[2][1]) + '|' + str(board[2][2]) + '|')
    

#determining who the winner of the game is    
def has_won(board):
    winner = 0
    if (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') or \
    (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') or \
    (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X') or \
    (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X') or \
    (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X') or \
    (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X') or \
    (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or \
    (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
        winner = 1
    elif (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O') or \
    (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O') or \
    (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O') or \
    (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O') or \
    (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O') or \
    (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O') or \
    (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or \
    (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
        winner = -1
    return winner

def play_game_level_1():
    x = 0
    while True:
        has_won(board)
        if (has_won(board) == 1):
            print('X has won')
            draw_board(board)
            break
        elif (has_won(board) == -1):
            print('O has won')
            draw_board(board)
            break
        else:
            try:
                select_move()
            except RecursionError:
                print('Tie')
                draw_board(board)
                break
        new_board = deepcopy(board)

play_game_level_1()