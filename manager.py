from random import choice, choices

from board import get_empty_spots

def get_adversary_move(board):
    """
    Places either a 2 or 4 tile randomly on the board
    """
    tile = choices([2, 4], weights=[90, 10])
    r, c = choice(get_empty_spots(board))
    board[r][c] = tile
    return board

def won(board, target):
    """
    Checks if any tile on the board is at least the target
    """
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] >= target:
                return True

    return False


