__author__ = 'Raymond Macharia <raymond.machira@gmail.com>'


def solve(board, num_queens):
    if num_queens == 0: return board

    for queen in range(num_queens):
        # initialize empty row for that queen
        board[queen] = [0] * 8

        # place queens staring at lowest index
        for index in range(len(board)):
            board[queen][index] = 1
            if is_board_valid(board):
                solve(board, num_queens - 1)

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
        if 1 in actual_row:
            print(row_index, actual_row.index(1))
            if not test_diagonals(board, (row_index, actual_row.index(1))): return False

    return True


def test_diagonals(board, start_position):
    # diagonals run in all four directions.
    # These names help us remember what pairs are heading which way.
    # _ denotes decreasing.
    # 1 denotes increasing.
    # Clearly there is a lot of repetition here, but I needed to do it to crystalise my process

    r1, c1 = _r1, _c1 = _r0, c0 = r0, _c0 = start_position
    r1 += 1
    c1 += 1
    while r1 < len(board) and c1 < len(board):
        if board[r1][c1] == 1:
            return False
        r1 += 1
        c1 += 1
    _r1 += -1
    _c1 += -1
    while _r1 >= -1 and _c1 > -1:
        if board[_r1][_c1] == 1:
            return False
        _r1 += -1
        _c1 += -1

    _r0 += -1
    c0 += 1
    while _r0 > -1 and c0 < len(board):
        if board[_r0][c0] == 1:
            return False
        _r0 += -1
        c0 += 1
    r0 += 1
    _c0 += -1
    while r0 < len(board) and _c0 > -1:
        if board[r0][_c0] == 1:
            return False
        r0 += 1
        _c0 += -1

    return True


def test_my_test(empty_board):
    empty_board[5][5] = 1
    empty_board[0][0] = 1
    for row in empty_board:
        print row

    assert (is_board_valid(empty_board))


if __name__ == '__main__':
    board_size = 8
    board = [None] * board_size
    for i in range(board_size):
        board[i] = [0] * board_size

    test_my_test(board)
    # solve([],board_size)
