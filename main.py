__author__ = 'Raymond Macharia <raymond.machira@gmail.com>'
import Nqueens
import sys
##
## Tests for correctness and instruments the code, to produce performance reports.
NUM_PIECES = 18
CONSTRAINT = True
OUTFILE = 'result.csv'

if __name__ == '__main__':
    # global NUM_PIECES, NUM_TRIES
    if len(sys.argv) > 1:
        NUM_PIECES = int(sys.argv[1])
        if sys.argv > 2:
            CONSTRAINT = True if (sys.argv[2]) else False
    start_board = [0]* NUM_PIECES

    Nqueens.CONSTRAINT = CONSTRAINT
    Nqueens.BOARD_SIZE = NUM_PIECES

    final_board, is_solved = Nqueens.solve(start_board)

    with open(OUTFILE,'a') as outfile:
        # outfile.write("Number of Pieces,Nodes Expanded,Solved,UsingConstraint\n")
        outfile.write("{0},{1},{2},{3}\n".format(NUM_PIECES,Nqueens.NUM_NODES_EXPANDED,is_solved,CONSTRAINT))