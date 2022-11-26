from collections import deque

"""
A 2d array is used to represent the 2048 board
"""

def get_next_moves(board):
    """
    Returns a list of boards, each of which represents a next move from the input board
    """
    res = [[] for _ in range(4)]
    for m in range(4):
        new_board = move(board, m)
        if new_board != board:
            res[m] = new_board

    return res

def move(board, m):
    """
    There are four possible moves: up, down, left, right
    These are represented as 0, 1, 2, 3 respectively
    """
    assert m in range(4)
    return move_helper(board, m >= 2, not m & 1)

def move_helper(board, horizontal, natural):
    """
    horizontal is a bool for whether the move is horizontal or vertical
    natural is a bool that is true if the move is up or left

    up: False, True
    down: False, False
    left: True, True
    right: True, False
    """
    n = len(board)
    new_board = [[0] * n for _ in range(n)]
    for i in range(n):
        q = deque()
        for j in range(n):
            r, c = (i, j) if horizontal else (j, i)
            if not board[r][c]:
                continue
            if natural:
                q.append(board[r][c])
            else:
                q.appendleft(board[r][c])

        def condense():
            new_q = deque()
            prev = 0
            while q:
                curr = q.popleft()
                if not prev:
                    prev = curr
                elif curr == prev:
                    new_q.append(curr * 2)
                    prev = 0
                else:
                    new_q.append(prev)
                    prev = curr

            if prev:
                new_q.append(prev)
            return new_q

        q = condense()
        for j in range(n) if natural else reversed(range(n)):
            if not q:
                break
            r, c = (i, j) if horizontal else (j, i)
            new_board[r][c] = q.popleft()

    return new_board

def get_empty_spots(board):
    """
    Returns the coordinates of all the empty cells on the board
    """
    n = len(board)
    res = []
    for r in range(n):
        for c in range(n):
            if not board[r][c]:
                res.append((r, c))

    return res

def string_of_board(board, target_n):
    """
    Pretty prints board. Takes in a target,
    which is the largest value that the board can display (used for formatting)
    """
    n = len(board)
    partition = "+" + ("-" + "-" * target_n + "-+") * n + "\n"
    filler = "|" + (" " + " " * target_n + " |") * n + "\n"

    res = partition
    for r in range(n):
        res += filler + "|"
        for c in range(n):
            res += " " + (str(board[r][c]) if board[r][c] else "").center(target_n) + " |"
        res += "\n" + filler + partition

    return res

def main():
    vertical_test = [[4, 0, 2, 0],
                     [2, 0, 2, 0],
                     [2, 0, 2, 0],
                     [2, 0, 4, 0]]
    horizontal_test = [[4, 2, 2, 2],
                       [0, 0, 0, 0],
                       [2, 2, 2, 4],
                       [0, 0, 0, 0]]

    for m in range(4):
        print(string_of_board(move(vertical_test, m), 6))
    for m in range(4):
        print(string_of_board(move(horizontal_test, m), 6))

if __name__ == "__main__":
    main()
