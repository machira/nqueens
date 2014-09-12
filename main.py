import time

__author__ = 'Raymond Macharia <raymond.machira@gmail.com>'


def solve(board, num_queens):
    if num_queens == 0: return board

    # for queen in range(num_queens):
        # initialize empty row for that queen
    queen = len(board) - num_queens
    # board[queen] = [0] * 8
    # place queens staring at lowest index
    for index in range(queen,len(board)):
        board[queen][index] = 1
        if is_board_valid(board) and is_board_valid(solve(board, num_queens - 1)):
            # this works
            break
        # this position failed, try the next one
        board[queen][index] = 0

    return board


def is_board_valid(board):
    # test all rows
    for row in range(len(board)):
        if sum(board[row]) > 1: return False
    # test all columns
    for column_index in range(len(board)):
        column = [board[index][column_index] for index in range(len(board))]
        if sum(column) > 1: return False

    # test diagonals
    for row in enumerate(board):
        row_index = row[0]
        actual_row = row[1]
        # if there is a queen on  this
        if 1 in actual_row:
            if not test_diagonals(board, (row_index, actual_row.index(1))): return False

    return True


def span_out_on_a_diagonal(board, start_position, row_increment, column_increment):
    r1, c1 = start_position
    r1 += row_increment
    c1 += column_increment

    while -1 < r1 < len(board) and -1 < c1 < len(board):
        if board[r1][c1] == 1:
            return False
        r1 += row_increment
        c1 += column_increment

    return True


def test_diagonals(board, start_position):
    # diagonals run in all four directions.
    # These names help us remember what pairs are heading which way.
    # _ denotes decreasing.
    # 1 denotes increasing.
    # Clearly there is a lot of repetition here, but I needed to do it to crystalise my process

    # r1, c1 = start_position
    if not (span_out_on_a_diagonal(board, start_position, 1, 1)
            and span_out_on_a_diagonal(board, start_position, -1, -1)
            and span_out_on_a_diagonal(board, start_position, -1, 1)
            and span_out_on_a_diagonal(board, start_position, 1, -1)):
        return False
    return True


def test_my_test(empty_board, row_cols):
    # place a queen on each cordinate
    for rw, cl in row_cols:
        empty_board[rw][cl] = 1

    for row_ in empty_board:
        print row_
    time.sleep(0.2)
    assert (is_board_valid(empty_board))


if __name__ == '__main__':
    board_size = 8
    board = [None] * board_size
    for i in range(board_size):
        board[i] = [0] * board_size

    # test_my_test(board, [(0, 7), (6, 0)])
    new_board = solve(board,board_size)
    for row in new_board:
        print row
