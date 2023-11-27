#!/usr/bin/python3
"""101-nqueens finds all possible solutions the N queens puzzle, including
translations and reflections.

Attempted virtual backtracking without recursion. In local tests process will
start to slow down visibly for N > 8, and is successful up to N = 11 but
will be killed if used for N > 11. Recursion could allow for a lighter weight
process, but it's not yet apparent to this student how to retain a record of
which solutions are already derived with that method.

Attributes:
    N (int): base number of queens, and length of board side in piece positions
    candidates (list) of (list) of (list) of (int): list of all successful
        solutions for given amount of columns checked

"""
from sys import argv

if len(argv) is not 2:
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
        board (list) of (list) of (int): 2D list of ints, only as wide as
        needed to test the rightmost column for queen conflicts.

    Returns:
        modified 2D list

    """
    if len(board_surf):
        for the_row in board_surf:
            the_row.append(0)
    else:
        for the_row in range(N):
            board_surf.append([0])
    return board_surf


def queen_adder(board_surf, the_row, column):
    """Sets "queen," or 1, to coordinates given in board.

    Args:
        board (list) of (list) of (int): 2D list of ints, only as wide as
            needed to test the rightmost column for queen conflicts.
        row (int): first dimension index
        col (int): second dimension index

    """
    board_surf[the_row][column] = 1


def new_queen(board_surf, the_row, column):
    """For the board given, checks that for a new queen placed in the rightmost
    column, there are no other "queen"s, or 1 values, in the martix to the
    left, and diagonally up-left and down-left.

    Args:
        board (list) of (list) of (int): 2D list of ints, only as wide as
            needed to test the rightmost column for queen conflicts.
        row (int): first dimension index
        col (int): second dimension index

    Returns:
        True if no left side conflicts found for new queen, or False if a
    conflict is found.

    """
    a = the_row
    b = column

    for i in range(1, N):
        if (b - i) >= 0:
            # check up-left diagonal
            if (a - i) >= 0:
                if board_surf[a - i][b - i]:
                    return False
            # check left
            if board_surf[a][b - i]:
                return False
            # check down-left diagonal
            if (a + i) < N:
                if board_surf[a + i][b - i]:
                    return False
    return True


def arrange_format(candi):
    """Converts a board (matrix of 1 and 0) into a series of row/column
    indicies of each queen/1.

    Args:
    candidates (list) of (list) of (list) of (int): list of all successful
        solutions for amount of columns last checked

    Attributes:
        holberton (list) of (list) of (int): each member list contains the row
    column number for each queen found

    Returns:
        holberton, the list of coordinates

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

# init candidates list with first column of 0s
candi = []
candi.append(column_generate())

# proceed column by column, testing the rightmost
for column in range(N):
    # start a new generation of the candidate list for every round of testing
    new_candi = []
    # test each candidate from previous round, at current column
    for matrix in candi:
        # for every row in that candidate's rightmost column
        for the_row in range(N):
            # are there any conflicts in placing a queen at those coordinates?
            if new_queen(matrix, the_row, column):
                # no? then create a "child" (copy) of that candidate
                tempo = [line[:] for line in matrix]
                # place a queen in that position
                queen_adder(tempo, the_row, column)
                # and unless you're in the last round of testing,
                if column < N - 1:
                    # add a new column of 0s on the right for the next round
                    column_generate(tempo)
                # add that new candidate to this round's list of successes
                new_candi.append(tempo)
    # when finished with the round, discard the "parent" candidates
    candi = new_candi

# format results to match assignment output
for item in arrange_format(candi):
    print(item)
