from random import choice, choices
from sys import argv

from board import get_next_moves, get_empty_spots, string_of_board

def get_adversary_move(board):
    """
    Places either a 2 or 4 tile randomly on the board
    """
    tile = choices([2, 4], weights=[90, 10])
    r, c = choice(get_empty_spots(board))
    board[r][c] = tile[0]
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

UP = "\x1B[1A"  # ANSI escape to move up a line
CLR = "\x1B[0K"  # ANSI escape to clear a line
def reprint_screen(board_string):
    """
    Reprints the board and input in the same position in terminal.
    Assumes a board and input have already been printed.
    """
    print(UP + CLR + UP, end="")
    for _ in range(board_string.count("\n")):
        print(UP + CLR, end="")

    print(board_string, end="")
    print("\n" + "Move: ", end="")

def main():
    if len(argv) > 3:
        print("Expected python3 manager.py <opt: max tile value> <opt: board dimensions>")
        return

    target = int(argv[1]) if len(argv) >= 2 else 2048
    n = int(argv[2]) if len(argv) >= 3 else 4
    if n <= 0:
        print("Dimensions must be positive")
        return

    def is_power_of_two(num):
        if num == 2:
            return True
        if num & 1:
            return False
        return is_power_of_two(num // 2)

    if target != -1 and (target < 2 or not is_power_of_two(target)):
        print("Invalid target: Target must be a power of 2, or -1 for non-stopping play")
        return

    target_n = max(len(str(target)), 7)  # formatting
    print()
    print("\n" * (4 * n + 3), end="")  # formatting
    board = get_adversary_move([[0] * n for _ in range(n)])
    while True:
        board_string = string_of_board(board, target_n)
        reprint_screen(board_string)
        if target > 0 and won(board, target):
            print("You won!")
            return

        next_moves = get_next_moves(board)
        if not any(next_moves):
            print("You lost")
            return

        key_to_move = {
            "w": 0,
            "s": 1,
            "a": 2,
            "d": 3,
        }
        m = input()
        while m != "exit" and (m not in key_to_move or not next_moves[key_to_move[m]]):
            reprint_screen(board_string)
            m = input()
        if m == "exit":
            return

        board = get_adversary_move(next_moves[key_to_move[m]])

if __name__ == "__main__":
    main()
