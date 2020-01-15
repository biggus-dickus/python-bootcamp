#! /usr/bin/env python

import random


def generate_board():
    return [None for i in range(0, 9)]

game = {
    'players': ('O', 'X'),
    'is_x_turn': random.randint(0, 1) == 1,
    'board': generate_board()
}

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def is_game_over(): 
    return None not in game['board']

def get_playable_squares(board):
    return [i for i, cell in enumerate(board) if cell == None]

def update_board(i):
    game['board'][i] = 'X' if game['is_x_turn'] else 'O'

def render_board(squares):
    board_str = ''

    for i, square in enumerate(squares):
        j = i + 1
        v = square or j
        cell = f' {v} |' if j % 3 != 0 else f' {v}\n'

        board_str += cell

    print(board_str)

def greet():
    print('Welcome to Tic-Tac-Toe written in Python! We hope you know the rules.')

    player_one = ''
    while player_one not in game['players']:
        player_one = input('Would you like to play as X or O?: ').upper()
    
    will_play_first = player_one == 'X' and game['is_x_turn'] == 1
    turn = 'first' if will_play_first else 'second'
    
    print(f'Great, you\'ll be playing as {player_one} and you will play {turn}')

def alternate_turn():
    game['is_x_turn'] = not game['is_x_turn']

def make_turn():
    player = 'X' if game['is_x_turn'] else 'O'
    square_index = -1
    is_invalid_input = False

    while not is_integer(square_index) or int(square_index) - 1 not in get_playable_squares(game['board']):
        is_invalid_input = square_index != -1
        if is_invalid_input:
            print(f'\nInvalid input: "{square_index}" Only numbers on the game board are allowed!')

        square_index = input(f'{player}, it\'s your turn. Choose any free square you see on the board and enter its number: ')

    return int(square_index) - 1

def check_winner(squares):
    lines = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )
  
    for cell in lines:
        if squares[cell[0]] and squares[cell[0]] == squares[cell[1]] and squares[cell[0]] == squares[cell[2]]:
            return squares[cell[0]]
    
    return None


# =================== #
def run_game():
    greet()

    while not is_game_over():
        winner = check_winner(game['board'])
        render_board(game['board'])

        if winner:
            print(f'Monsieur {winner}, you won! Congratulations!')
            break

        turn = make_turn()
        update_board(turn)
        alternate_turn()

    else:
        render_board(game['board'])
        print('It\'s a tie!')


run_game()
