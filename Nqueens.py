import time
import copy
from itertools import product

__author__ = 'Raymond Macharia <raymond.machira@gmail.com>'

BOARD_SIZE = 8 ## Also analogous to number of queens to place.
NUM_NODES_EXPANDED = 0 ## counts the number of times we try to place a queen ie nodes we expand
CONSTRAINT = False

def solve(board, column = 0, constraints = {}):
    global NUM_NODES_EXPANDED
    NUM_NODES_EXPANDED += 1

    if column >= BOARD_SIZE:
        return board, goal_found(board)

    for i in [i for i in range(0,BOARD_SIZE) if (column in constraints and i not in constraints[column]) or (column not in constraints)]:
        # create a new mutable board
        new_board = board[:]
        constraints_copy = copy.deepcopy(constraints)
        new_board[column] = i

        new_constraints = create_constraints(column,i) if CONSTRAINT else {}

        for key in new_constraints.keys():
            if key in constraints_copy: constraints_copy[key] = constraints_copy[key].union(new_constraints[key])
            else: constraints_copy[key] = new_constraints[key]

        sol_board, solved = solve(new_board, column=column+1, constraints=constraints_copy)
        if solved:
            return sol_board, True

    return board, False

def create_constraints(col, choice):
    # dictionary of new constraints introduced by this choice.
    dict_constraints = {}
    r1 = choice - 1
    r2 = choice + 1

    for i in range(col+1,BOARD_SIZE):
        c = set()
        # remove same row
        c.add(choice)
        if r1 > -1:
            c.add(r1)
            r1 -= 1
        if r2 < BOARD_SIZE:
            c.add(r2)
            r2 += 1

        dict_constraints[i] = c

    return dict_constraints

def goal_found(board):
    # alldiff constraint
    if (len(board) != len(set(board))): return False

    for (col,row) in enumerate(board[:BOARD_SIZE - 1]):
        r1 = r2 = row
        # check the diagonals
        for c2 in range(col + 1, BOARD_SIZE):
            r1+= 1
            r2+=-1
            if (0 <= r1 < BOARD_SIZE and board[c2] == r1) or (0<= r2 < BOARD_SIZE and board[c2] == r2): return False

    return True

def test_my_test(empty_board, row_cols):
    # place a queen on each coordinate
    for rw, cl in row_cols:
        empty_board[rw][cl] = 1

    show_board(empty_board)

    time.sleep(0.2)
    assert (goal_found(empty_board))

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