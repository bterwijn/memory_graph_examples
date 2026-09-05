

class NQueens:

    def __init__(self, size):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.available_cols = list([True] * size)
        self.open_up_diagonals = set(range(2*size - 1))
        self.open_down_diagonals = set(range(2*size - 1))

    def __repr__(self):
        return "\n".join(" ".join(row) for row in self.board) + "\n"

    def get_diagonal_indices(self, row, col):
        up_diagonal = row + col
        down_diagonal = row - col + (self.size - 1)
        return up_diagonal, down_diagonal

    def valid_position(self, up_diagonal, down_diagonal):
        return (up_diagonal   in self.open_up_diagonals and 
                down_diagonal in self.open_down_diagonals)

    def add_queen(self, row, col, up_diagonal, down_diagonal):
        self.board[row][col] = 'Q'
        self.available_cols[col] = False
        self.open_up_diagonals.remove(up_diagonal)
        self.open_down_diagonals.remove(down_diagonal)
        return True

    def remove_queen(self, row, col, up_diagonal, down_diagonal):
        self.board[row][col] = '.'
        self.available_cols[col] = True
        self.open_up_diagonals.add(up_diagonal)
        self.open_down_diagonals.add(down_diagonal)
        return True

    def solve(self, row=0):
        for col in range(self.size):
            if self.available_cols[col]:
                up_diagonal, down_diagonal = self.get_diagonal_indices(row, col)
                if self.valid_position(up_diagonal, down_diagonal):
                    self.add_queen(row, col, up_diagonal, down_diagonal)
                    if row == self.size - 1:
                        print(self)
                    else:
                        self.solve(row + 1)
                    self.remove_queen(row, col, up_diagonal, down_diagonal)

nqueens = NQueens(8)
nqueens.solve()
