import time
from itertools import product

__author__ = 'Raymond Macharia <raymond.machira@gmail.com>'

BOARD_SIZE = 8


def solve(board, constraints):

    if goal_found(board):
        return board, True


    # for queen in range(num_queens):
        # initialize empty row for that queen
    queen = len(board) - num_queens
    # board[queen] = [0] * 8
    # place queens staring at lowest index
    for index in range(len(board)):
        board[queen][index] = 1
        if solve(board,num_queens-1)[1] and goal_found(board):
            # this works
            return board, True
        # this position failed, try the next one
        board[queen][index] = 0

    return board, False


def goal_found(board):
    # alldiff constraint
    if (len(board) != len(set(board))): return False

    for (col,row) in enumerate(board[:BOARD_SIZE - 1]):
        # if not(span_out_on_a_diagonal (board,(row,col),1,1) and span_out_on_a_diagonal(board,(row,col),-1,1)): return False
        r1 = r2 = row
        for c2 in range(col + 1, BOARD_SIZE):
            r1+= 1
            r2+=-1
            if (0 <= r1 < BOARD_SIZE and board[c2] == r1) or (0<= r2 < BOARD_SIZE and board[c2] == r2): return False

    return True


def span_out_on_a_diagonal(board, start_position, row_increment, column_increment):
    list(enumerate(board)).index(start_position)

    r1, c1 = start_position
    r1 += row_increment
    c1 += column_increment

    while -1 < r1 < len(board) and -1 < c1 < len(board):
        if board[r1][c1] == 1:
            return False
        r1 += row_increment
        c1 += column_increment

    return True


def test_my_test(empty_board, row_cols):
    # place a queen on each coordinate
    for rw, cl in row_cols:
        empty_board[rw][cl] = 1

    show_board(empty_board)

    time.sleep(0.2)
    assert (goal_found(empty_board))

def initialise(board_size=BOARD_SIZE):
    # initialize board with all queens in the first row
    global BOARD_SIZE
    BOARD_SIZE = board_size

    board = [1] * board_size
    return board

def play(board):
    new_board,is_solved = solve(board,BOARD_SIZE)
    if is_solved:
        show_board(new_board)


def show_board(board):
    """
    Prints out a board
    :param board:
    :return:
    """
    sttr = ''
    for (i,j) in list(product(range(0,BOARD_SIZE),range(0,BOARD_SIZE))):
        sttr += '\n' if j == 0 else ''
        sttr += '1' if board[j]==i else '0'

    print(sttr)


if __name__ == '__main__':
    # board = initialise()
    # play(board)
    BOARD_SIZE = 4
    board = [1,3,0,2]
    goal_found(board)