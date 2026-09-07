import string

def main():
    sudoku = Sudoku()
    board = """
. . 3 | . 2 . | 6 . . 
9 . . | 3 . 5 | . . 1 
. . 1 | 8 . 6 | 4 . . 
------+-------+------
. . 8 | 1 . 2 | 9 . -
7 . . | . . . | . . 8
. . 6 | 7 . 8 | 2 . -
------+-------+------
. . 2 | 6 . 9 | 5 . -
8 . . | 2 . 3 | . . 9
. . 5 | . 1 . | 3 . -
"""
    sudoku.set_board(board)
    print('initial board:')
    print(sudoku)
    sudoku.solve()
    print('no more solutions')


def horizontal_indices(size, row, col):
    return [(row, c) for c in range(size) if c != col]

def vertical_indices(size, row, col):
    return [(r, col) for r in range(size) if r != row]

def square_indices(square_size, row, col):
    start_row = (row // square_size) * square_size
    start_col = (col // square_size) * square_size
    return [(r, c) for r in range(start_row, start_row + square_size)
                    for c in range(start_col, start_col + square_size)
                    if (r, c) != (row, col)]

class Sudoku:

    def __init__(self, size = 9):
        self.size = size
        self.square_size = int(size ** 0.5)
        self.values = [[set(range(1, size+1)) for _ in range(size)] for _ in range(size)]

    def __repr__(self):
        s = ''
        for row in range(self.size):
            if row % 3 == 0 and row > 0:
                s += '-+-'.join('-' * (2*(self.square_size)-1) for _ in range(self.square_size)) + '\n'
            for col in range(self.size):
                if col % 3 == 0 and col > 0:
                    s += '| '
                if len(self.values[row][col]) == 1:
                    s += str(next(iter(self.values[row][col]))) + ' '
                else:
                    s += '. '
            s+='\n'  # new line
        return s

    def set_board(self, board):
        lines = board.strip().splitlines()
        row = 0
        for _, line in enumerate(lines):
            line = ''.join([s for s in line if s in '.' + string.digits])
            if line:
                col = 0
                for c in line:
                    if c.isdigit() and c != '0':
                        self.set_number(row, col, int(c))
                    col += 1
                row += 1

    def set_number(self, row, col, number):
        old_numbers = self.values[row][col]
        self.values[row][col] = {number}
        remove_from_cells = []
        dead_end = False
        for r, c in horizontal_indices(self.size, row, col):
            if number in self.values[r][c]:
                self.values[r][c].remove(number)
                remove_from_cells.append((r, c))
                dead_end = dead_end or len(self.values[r][c]) == 0
        for r, c in vertical_indices(self.size, row, col):
            if number in self.values[r][c]:
                self.values[r][c].remove(number)
                remove_from_cells.append((r, c))
                dead_end = dead_end or len(self.values[r][c]) == 0
        for r, c in square_indices(self.square_size, row, col):
            if number in self.values[r][c]:
                self.values[r][c].remove(number)
                remove_from_cells.append((r, c))
                dead_end = dead_end or len(self.values[r][c]) == 0
        #print(f'set {row=} {col=} {number=}')
        return dead_end, old_numbers, remove_from_cells

    def unset_number(self, row, col, number, old_numbers, remove_from_cells):
        self.values[row][col] = old_numbers
        for r, c in remove_from_cells:
            self.values[r][c].add(number)
        #print(f'unset {row=} {col=} {number=}')

    def get_most_constrained_cells(self):
        min_options = self.size + 1
        min_cells = []
        for row in range(self.size):
            for col in range(self.size):
                nr_options = len(self.values[row][col])
                if nr_options > 1:
                    if nr_options < min_options:
                        min_options = nr_options
                        min_cells = [(row, col)]
                    elif nr_options == min_options:
                        min_cells.append((row, col))
        return min_options, min_cells

    def get_least_constraining_value(self, cells):
        max_options = self.size * 3
        best_row = None
        best_col = None
        best_number = None
        for row, col in cells:
            for number in self.values[row][col]:
                dead_end, old_numbers, removed_from_cells = self.set_number(row, col, number)
                if not dead_end:
                    if len(removed_from_cells) < max_options:
                        max_options = len(removed_from_cells)
                        best_row = row
                        best_col = col
                        best_number = number
                self.unset_number(row, col, number, old_numbers, removed_from_cells)
        return best_row, best_col, best_number
    
    def solve(self):
        min_options, min_cells = self.get_most_constrained_cells()
        #print('solve', min_options, min_cells)
        if min_options == self.size + 1:
            print('solution found:')
            print(self)
        elif min_cells:
            best_row, best_col, best_number = self.get_least_constraining_value(min_cells)
            if best_row is not None:
                dead_end, old_numbers, removed_from_cells = self.set_number(best_row, best_col, best_number)
                self.solve()
                self.unset_number(best_row, best_col, best_number, old_numbers, removed_from_cells)
                #print('backtrack')

main()