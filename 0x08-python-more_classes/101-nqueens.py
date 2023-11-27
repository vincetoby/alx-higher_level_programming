#!/usr/bin/python3
"""101-nqueens finds every possible solution to the N queens puzzle, including
translations and reflections.

Attributes:
    N (int): base number of queens, and length of board side in piece positions
    candi (list) of (list) of (list) of (int): list of all successful
        solutions for given amount of columns checked
"""
from sys import argv

if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)


def column_generate(board_surf=[]):
    """Adds a column of zeroes to the right of any board about to be tested for
    queen arrangements in that column.

    Args:
        board_surf: 2D list of ints

    Returns:
        returns the modified 2D list

    """
    if len(board_surf):
        for the_row in board_surf:
            the_row.append(0)
    else:
        for the_row in range(N):
            board_surf.append([0])
    return board_surf


def queen_adder(board_surf, the_row, column):
    """Sets "queen" or 1, to coordinates given in board.

    Args:
        board_surf: 2D list of ints, only as wide as
            needed to test the rightmost column for queen conflicts.
        the_row: an integer, first dimension index
        column: an int as well, second dimension index

    """
    board_surf[the_row][column] = 1


def new_queen(board_surf, the_row, column):
    """this checks that for a new queen(1) placed in the rightmost
    column, there are no other "queen's", or 1 values, in the martix to the
    left, and diagonally up-left and down-left.

    Args:
        board_surf: 2D list of ints
        the_row (integer): first dimension index
        column (integer): second dimension index

    Returns:
        True if no  conflicts is found for new queen, False otherwise

    """
    a = the_row
    b = column

    for i in range(1, N):
        if (b - i) >= 0:
            # checks up-left diagonal
            if (a - i) >= 0:
                if board_surf[a - i][b - i]:
                    return False
            # checks left
            if board_surf[a][b - i]:
                return False
            # checks down-left diagonal
            if (a + i) < N:
                if board_surf[a + i][b - i]:
                    return False
    return True


def arrange_format(candi):
    """Converts a board (which is a matrix of 1 and 0) series of row/column
    indices of each queen(1).

    Args:
        candi: list of all successful solutions for
            amount of columns last checked

    Attributes:
        alx: each member list contains the row
    column number for each queen found

    Returns:
        alx, list containing the coordinates

    """
    alx = []
    for a, attempt in enumerate(candi):
        alx.append([])
        for i, the_row in enumerate(attempt):
            alx[a].append([])
            for j, column in enumerate(the_row):
                if column:
                    alx[a][i].append(i)
                    alx[a][i].append(j)
    return alx

# initialize candi list with first column of 0's
candi = []
candi.append(column_generate())

# move column by column, testing the rightmost
for column in range(N):
    # start a new gen of the candi list for every round of testing
    new_candi = []
    # test each candi from prev round, at the current column
    for matrix in candi:
        # for every row in that candi's right-most column
        for the_row in range(N):
            # check for conflicts
            if new_queen(matrix, the_row, column):
                # if no, create a copy of that candi
                tempo = [line[:] for line in matrix]
                # place a queen in that position
                queen_adder(tempo, the_row, column)
                # and unless you're in the last round of testing,
                if column < N - 1:
                    # add new column of 0's on the right for the next round
                    column_generate(tempo)
                # add that new candidate to this round's list of successes
                new_candi.append(tempo)
    # when finished with the round, discard the "parent" candi
    candi = new_candi

# format results to match assignment output
for result in arrange_format(candi):
    print(result)
