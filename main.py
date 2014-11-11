__author__ = 'Raymond Macharia <raymond.machira@gmail.com>'
import Nqueens
import sys
##
## Tests for correctness and instruments the code, to produce performance reports.
NUM_PIECES = 8
NUM_TRIES = 100
OUTFILE = 'result.csv'

if __name__ == '__main__':
    global NUM_PIECES, NUM_TRIES
    if (sys.argv) > 1:
        NUM_PIECES = int(sys.argv[1])
        if len(sys.argv) > 2:
            NUM_TRIES = int(sys.argv[2])

    # start_board = Nqueens.initialise(board_size=NUM_PIECES)
    #
    #
    # final_board, is_solved = Nqueens.solve(start_board)
