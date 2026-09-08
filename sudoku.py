import string
import functools as ft

def main():

    board1 = """
. . 3 | . 2 . | 6 . . 
9 . . | 3 . 5 | . . 1 
. . 1 | 8 . 6 | 4 . . 
------+-------+------
. . 8 | 1 . 2 | 9 . .
7 . . | . . . | . . 8
. . 6 | 7 . 8 | 2 . .
------+-------+------
. . 2 | 6 . 9 | 5 . .
8 . . | 2 . 3 | . . 9
. . 5 | . 1 . | 3 . .
"""

    board2 = """
8 0 0 0 0 0 0 0 0
0 0 3 6 0 0 0 0 0
0 7 0 0 9 0 2 0 0
0 5 0 0 0 7 0 0 0
0 0 0 0 4 5 7 0 0
0 0 0 1 0 0 0 3 0
0 0 1 0 0 0 0 6 8
0 0 8 5 0 0 0 1 0
0 9 0 0 0 0 4 0 0
"""

    board3 = """
0 0 0 0 0 0 6 8 0
0 0 0 0 7 3 0 0 9
3 0 9 0 0 0 0 4 5
4 9 0 0 0 0 0 0 0
8 0 3 0 5 0 9 0 2
0 0 0 0 0 0 0 3 6
9 6 0 0 0 0 3 0 8
7 0 0 6 8 0 0 0 0
0 2 8 0 0 0 0 0 0
"""
    boards = [board1, board2, board3]

    sudoku = Sudoku()
    for board in boards:
        sudoku.reset(board)
        print('initial board:')
        print(sudoku)
        sudoku.solve()
        print('no more solutions')

class Sudoku:
    UNSET = 0

    def __init__(self, board = None):
        if board is not None:
            self.reset(board)

    def reset(self, board):
        size, given_numbers = self.set_board(board)
        self.size = size
        self.square_size = int(size ** 0.5)
        Sudoku.horizontal_indices.cache_clear()
        Sudoku.vertical_indices.cache_clear()
        Sudoku.square_indices.cache_clear()
        self.clear(size)
        self.set_given_numbers(given_numbers)

    def set_board(self, board):
        size = None
        given_nubers = []
        lines = board.strip().splitlines()
        row = 0
        for _, line in enumerate(lines):
            line = ''.join([s for s in line if s in '.' + string.digits])
            if line:
                col = 0
                for c in line:
                    if c.isdigit() and c != '0':
                        given_nubers.append((row, col, int(c)))
                    col += 1
                if size is None:
                    size = col
                elif size != col:
                    raise ValueError(f'line {line} has {col} columns, expected {size}')
                row += 1
        return size, given_nubers

    def clear(self, size):
        self.values = [[set(range(1, size+1)) for _ in range(size)] for _ in range(size)]
        self.board = [[Sudoku.UNSET for _ in range(size)] for _ in range(size)]

    def set_given_numbers(self, given_numbers):
        for row, col, number in given_numbers:
            self.set_number(row, col, number)

    def __repr__(self):
        s = ''
        for row in range(self.size):
            if row % 3 == 0 and row > 0:
                s += '-+-'.join('-' * (2*(self.square_size)-1) for _ in range(self.square_size)) + '\n'
            for col in range(self.size):
                if col % 3 == 0 and col > 0:
                    s += '| '
                if self.board[row][col] != Sudoku.UNSET:
                    s += str(self.board[row][col]) + ' '
                else:
                    s += '. '
            s+='\n'  # new line
        return s

    @ft.cache
    def horizontal_indices(self, row, col):
        no_col = col // self.square_size
        return [(row, c) for c in range(self.size) if c // self.square_size != no_col]

    @ft.cache
    def vertical_indices(self, row, col):
        no_row = row // self.square_size
        return [(r, col) for r in range(self.size) if r // self.square_size != no_row]

    @ft.cache
    def square_indices(self, row, col):
        start_row = (row // self.square_size) * self.square_size
        start_col = (col // self.square_size) * self.square_size
        return [(r, c) for r in range(start_row, start_row + self.square_size)
                        for c in range(start_col, start_col + self.square_size)
                        if (r, c) != (row, col)]

    def set_number(self, row, col, number):
        old_numbers = self.values[row][col]
        self.values[row][col] = {number}
        self.board[row][col] = number
        remove_from_cells = []
        dead_end = False
        for r, c in self.horizontal_indices(row, col):
            if number in self.values[r][c]:
                self.values[r][c].remove(number)
                remove_from_cells.append((r, c))
                dead_end = dead_end or len(self.values[r][c]) == 0
        for r, c in self.vertical_indices(row, col):
            if number in self.values[r][c]:
                self.values[r][c].remove(number)
                remove_from_cells.append((r, c))
                dead_end = dead_end or len(self.values[r][c]) == 0
        for r, c in self.square_indices(row, col):
            if number in self.values[r][c]:
                self.values[r][c].remove(number)
                remove_from_cells.append((r, c))
                dead_end = dead_end or len(self.values[r][c]) == 0
        #print(f'set {row=} {col=} {number=}')
        return dead_end, old_numbers, remove_from_cells

    def unset_number(self, row, col, number, old_numbers, remove_from_cells):
        self.values[row][col] = old_numbers
        self.board[row][col] = Sudoku.UNSET
        for r, c in remove_from_cells:
            self.values[r][c].add(number)
        #print(f'unset {row=} {col=} {number=}')

    def get_most_constrained_cells(self):
        min_options = self.size + 1
        min_cells = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == Sudoku.UNSET:
                    nr_options = len(self.values[row][col])
                    if nr_options < min_options:
                        min_options = nr_options
                        min_cells = [(row, col)]
                    elif nr_options == min_options:
                        min_cells.append((row, col))
        return min_options, min_cells

    def get_least_constraining_values_ordered(self, cells):
        values_ordered = []
        min_removed_from_cells = self.size * 3
        best_cell = None
        #print(f'=== {cells=}')
        for cell in cells:
            #print(f'{cell=}')
            row, col = cell
            for number in self.values[row][col]:
                dead_end, old_numbers, removed_from_cells = self.set_number(row, col, number)
                #print(f'{dead_end=} {number=} {removed_from_cells=}')
                if not dead_end:
                    nr_removed_from_cells = len(removed_from_cells)
                    if nr_removed_from_cells < min_removed_from_cells:
                        min_removed_from_cells = nr_removed_from_cells
                        best_cell = cell
                    values_ordered.append((nr_removed_from_cells, cell, number))
                self.unset_number(row, col, number, old_numbers, removed_from_cells)
        values_ordered = [v for v in values_ordered if v[1] == best_cell]
        values_ordered.sort(key=lambda x: x[0])
        return values_ordered

    def solve(self):
        min_options, min_cells = self.get_most_constrained_cells()
        #print('solve', min_options, min_cells)
        if min_options > self.size:
            print('solution found:')
            print(self)
        elif min_cells:
            values_ordered = self.get_least_constraining_values_ordered(min_cells)
            #print(f'{values_ordered=}')
            if values_ordered:
                for nr_removed_from_cells, cell, number in values_ordered:
                    row, col = cell
                    dead_end, old_numbers, removed_from_cells = self.set_number(row, col, number)
                    self.solve()
                    self.unset_number(row, col, number, old_numbers, removed_from_cells)

main()