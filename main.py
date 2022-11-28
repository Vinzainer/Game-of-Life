#!/usr/bin/python3

import time
import numpy as np

board = np.zeros((11,11))
board[5,5] = 1
board[5,6] = 1
board[5,7] = 1

def update_board(board):
    lines, columns = (10,10)

    for x in range(lines):
        for y in range(columns):
            total = count_neighbours(board, x, y)

            if(board[x, y] and (total < 2 or total > 3)):
                board[x, y] = 0

            if(not board[x, y] and total == 3):
                board[x, y] = 1

def count_neighbours(board, x, y):
    total = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if(board[x+i, y+j]):
                total += 1

    if(board[x, y]):
        total -= 1

    return total

while(True):
    print(board)
    print()
    update_board(board)
    time.sleep(2)