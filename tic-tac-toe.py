import numpy as np
from copy import deepcopy
import random
import sys

sys.setrecursionlimit(1500)

# The initial state of the game board is empty with numbers 1-9 representing the places
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# X goes first, so if the player is X, they get first choice

def legal_moves(input_board):
    moves = []
    for row in input_board:
        for col in row:
            if col != 'X' and col != 'O':
                moves.append(int(col))
    return moves

# If they player is X, they can place, otherwise the computer picks a point for X (right now, at random)
def choose_x_level_1(board):
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
        other_choice = random.choice(legal_moves(board))
        if other_choice == 1:
            board[0][0] = 'X'
        elif other_choice == 2:
            board[0][1] = 'X'
        elif other_choice == 3:
            board[0][2] = 'X'
        elif other_choice == 4:
            board[1][0] = 'X'
        elif other_choice == 5:
            board[1][1] = 'X'
        elif other_choice == 6:
            board[1][2] = 'X'
        elif other_choice == 7:
            board[2][0] = 'X'
        elif other_choice == 8:
            board[2][1] = 'X'
        else:
            board[2][2] = 'X'
       
# O will then go next
def choose_o_level_1(board):
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
        other_choice = random.choice(legal_moves(board))
        if other_choice == 1:
            board[0][0] = 'O'
        elif other_choice == 2:
            board[0][1] = 'O'
        elif other_choice == 3:
            board[0][2] = 'O'
        elif other_choice == 4:
            board[1][0] = 'O'
        elif other_choice == 5:
            board[1][1] = 'O'
        elif other_choice == 6:
            board[1][2] = 'O'
        elif other_choice == 7:
            board[2][0] = 'O'
        elif other_choice == 8:
            board[2][1] = 'O'
        else:
            board[2][2] = 'O'

#next, let's draw the current octothorp
def draw_board(board):
    print('|' + str(board[0][0]) + '|' + str(board[0][1]) + '|' + str(board[0][2]) + '|')
    print('|' + str(board[1][0]) + '|' + str(board[1][1]) + '|' + str(board[1][2]) + '|')
    print('|' + str(board[2][0]) + '|' + str(board[2][1]) + '|' + str(board[2][2]) + '|')
    

#determining who the winner of the game is    
def has_won(board, value):
    if (board[0][0] == value and board[1][0] == value and board[2][0] == value) or \
    (board[0][1] == value and board[1][1] == value and board[2][1] == value) or \
    (board[0][2] == value and board[1][2] == value and board[2][2] == value) or \
    (board[0][0] == value and board[0][1] == value and board[0][2] == value) or \
    (board[1][0] == value and board[1][1] == value and board[1][2] == value) or \
    (board[2][0] == value and board[2][1] == value and board[2][2] == value) or \
    (board[0][0] == value and board[1][1] == value and board[2][2] == value) or \
    (board[0][2] == value and board[1][1] == value and board[2][0] == value):
        return True
    else:
        return False
    
def game_over(input_board):
    if (has_won(input_board, "X") == True) or (has_won(input_board, 'O') == True) or (len(legal_moves(input_board)) == 0):
        return True
    else:
        return False
    
def evaluate_board(input_board):
    if has_won(input_board, 'X') == True:
        return 1
    elif has_won(input_board, 'O') == True:
        return -1
    else:
        return 0
    
def select_space(input_board, space, symbol):
    if space == 1:
        input_board[0][0] = symbol
    elif space == 2:
        input_board[0][1] = symbol
    elif space == 3:
        input_board[0][2] = symbol
    elif space == 4:
        input_board[1][0] = symbol
    elif space == 5:
        input_board[1][1] = symbol
    elif space == 6:
        input_board[1][2] = symbol
    elif space == 7:
        input_board[2][0] = symbol
    elif space == 8:
        input_board[2][1] = symbol
    else:
        input_board[2][2] = symbol
    
def minimax(input_board, is_maximizing):
    # base case
    if game_over(input_board):
        return evaluate_board(input_board)
    if is_maximizing == True:
        best_value = -float('Inf')
        symbol = 'X'
    else:
        best_value = float('Inf')
        symbol = 'O'
    for move in legal_moves(input_board):
        new_board = deepcopy(input_board)
        select_space(new_board, move, symbol)
        hypothetical_value = minimax(new_board, not is_maximizing)
        if is_maximizing:
            if hypothetical_value > best_value:
                best_value = hypothetical_value
        else:
            if hypothetical_value < best_value:
                best_value = hypothetical_value
    return best_value

def play_game_level_1():
    while True:
        has_won(board, 'O')
        if (has_won(board, 'O') == True):
            print('O has won')
            draw_board(board)
            break
        elif len(legal_moves(board)) == 0:
            print('Tie')
            draw_board(board)
            break
        else:
            choose_x_level_1(board)
            moves(board)
        has_won(board, 'X')
        if (has_won(board, 'X') == True):
            print('X has won')
            draw_board(board)
            break
        elif len(legal_moves(board)) == 0:
            print('Tie')
            draw_board(board)
            break
        else: 
            choose_o_level_1(board)
            moves(board)

level = int(input("What level do you want to play: 1 or 2?\n"))

if level == 1:
    char = input('Do you want to be X\'s or O\'s?\n')
    play_game_level_1()
else:
    print(minimax(board, True))