
def main():
    sudoku = Sudoku()
    board = """
- - 3 # - 2 - # 6 - - 
9 - - # 3 - 5 # - - 1 
- - 1 # 8 - 6 # 4 - - 
#####################
- - 8 # 1 - 2 # 9 - -
7 - - # - - - # - - 8
- - 6 # 7 - 8 # 2 - -
#####################
- - 2 # 6 - 9 # 5 - -
8 - - # 2 - 3 # - - 9
- - 5 # - 1 - # 3 - -
"""
    sudoku.set_board(board)
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
            for col in range(self.size):
                if len(self.values[row][col]) == 1:
                    s += str(next(iter(self.values[row][col]))) + ' '
                else:
                    s += '- '
            s+='\n'  # new line
        return s

    def set_board(self, board):
        lines = board.strip().splitlines()
        row = 0
        for i, line in enumerate(lines):
            line = line.strip().strip("#")
            if line:        
                col = 0
                for c in line:
                    if c in ' #':  # ignore
                        continue
                    if c.isdigit():
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
    
    def solve(self):
        min_options, min_cells = self.get_most_constrained_cells()
        #print('solve', min_options, min_cells)
        if min_options == self.size + 1:
            print('solution found:')
            print(self)
        elif min_cells:
            row, cell = min_cells[0]
            for number in self.values[row][cell]:
                dead_end, old_numbers, removed_from_cells = self.set_number(row, cell, number)
                if not dead_end:
                    self.solve()
                self.unset_number(row, cell, number, old_numbers, removed_from_cells)
                #print('backtrack')

main()