from ChessEngine.engine import board
from utils import *

"""
+---+---+---+---+---+---+---+---+
| r | n | b | q | k | b | n | r | 8
+---+---+---+---+---+---+---+---+
| p | p |   | p | p | p | p | p | 7
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 6
+---+---+---+---+---+---+---+---+
|   |   | p |   |   |   |   |   | 5
+---+---+---+---+---+---+---+---+
|   |   |   |   | P |   |   |   | 4
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 3
+---+---+---+---+---+---+---+---+
| P | P | P | P |   | P | P | P | 2
+---+---+---+---+---+---+---+---+
| R | N | B | Q | K | B | N | R | 1
+---+---+---+---+---+---+---+---+
  a   b   c   d   e   f   g   h

"""

brd = board(display=False)

prev = [['W','W','W','W','W','W','W','W'],
        ['W','W','W','W','W','W','W','W'],
        ['a','a','a','a','a','a','a','a'],
        ['a','a','a','a','a','a','a','a'],
        ['a','a','a','a','a','a','a','a'],
        ['a','a','a','a','a','a','a','a'],
        ['B','B','B','B','B','B','B','B'],
        ['B','B','B','B','B','B','B','B']
        ]

def get_best_move_from_board():
    best_move = brd.get_best()
    while (best_move=='o/o/o' or best_move=='o/o'):
        best_move = brd.get_best()
    return best_move

def print_array(arr):
    for i in range(8):
        for j in range(8):
            print(arr[i][j], end=' ')
        print()
    print()

while (True):
    # Take input from user
    arr = []
    for i in range(8):
        s = input()
        temp = s.split(' ')
        arr.append(temp)
    # arr.reverse()
    # print_array(prev)
    # print_array(arr)
    player_move = move_from_player(arr,prev)
    # print(player_move)
    # print(move)
    # Implement detected move in stockfish board
    brd.move_piece(player_move, display=False)
    # Get best move
    best_move = get_best_move_from_board()
    if (best_move == None):
        print("Check mate!!")
        break
    # Implement best move in stockfish board
    brd.move_piece(best_move)
    # Assuming there is a single best move
    # Implement best move in our board
    arr = update_array(arr,best_move)
    prev = arr
    # print(best_move)
