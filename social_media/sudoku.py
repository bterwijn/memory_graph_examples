import random
import time


class Sudoku:
    def __init__(self):
        self.board = self.generate_safe_puzzle()

    def display_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - -")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(self.board[i][j], end=" ")
            print()
        print()

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def check_row(self, row, num):
        return num not in self.board[row]

    def check_column(self, col, num):
        for i in range(9):
            if self.board[i][col] == num:
                return False
        return True

    def check_box(self, row, col, num):
        sr = (row // 3) * 3
        sc = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[sr + i][sc + j] == num:
                    return False
        return True

    def is_valid_move(self, row, col, num):
        if self.board[row][col] != 0:
            return False
        if not self.check_row(row, num):
            return False
        if not self.check_column(col, num):
            return False
        if not self.check_box(row, col, num):
            return False
        return True

    def move_error(self, row, col, num):
        if self.board[row][col] != 0:
            return "Cell already taken"
        if not self.check_row(row, num):
            return "Number already in row"
        if not self.check_column(col, num):
            return "Number already in column"
        if not self.check_box(row, col, num):
            return "Number already in box"
        return "Move accepted"

    def place_move(self, row, col, num):
        if self.is_valid_move(row, col, num):
            self.board[row][col] = num
            return True, "Move accepted"
        return False, self.move_error(row, col, num)

    def solve(self, solver=False):
        empty = self.find_empty()
        if not empty:
            return True

        r, c = empty

        for num in range(1, 10):
            valid = self.is_valid_move(r, c, num)
            if valid:
                self.board[r][c] = num

                if solver:
                    self.display_board()
                    time.sleep(0.03)

                if self.solve(solver):
                    return True

                self.board[r][c] = 0

        return False

    def generate_solved(self):
        empty = self.find_empty()
        if not empty:
            return True

        r, c = empty
        nums = list(range(1, 10))
        random.shuffle(nums)

        for num in nums:
            valid = self.is_valid_move(r, c, num)
            if valid:
                self.board[r][c] = num

                if self.generate_solved():
                    return True

                self.board[r][c] = 0

        return False

    def generate_safe_puzzle(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.generate_solved()

        attempts = 40

        while attempts > 0:
            r = random.randint(0, 8)
            c = random.randint(0, 8)

            if self.board[r][c] != 0:
                backup = self.board[r][c]
                self.board[r][c] = 0
                copy = [row[:] for row in self.board]

                if not self.solve():
                    self.board[r][c] = backup

                self.board = copy
                attempts -= 1

        return self.board

    def play(self):
        while True:
            self.display_board()
            print("Enter: row,col,num OR solve OR quit")
            inp = input("> ")

            if inp.lower() == "solve":
                self.solve(solver=True)
                self.display_board()
                break

            if inp.lower() == "quit":
                break

            try:
                r, c, n = map(int, inp.split(","))
                r -= 1
                c -= 1

                if r not in range(9) or c not in range(9) or n not in range(1, 10):
                    print("Out of range! Use 1-9 only")
                    continue

                success, msg = self.place_move(r, c, n)
                print(msg)

            except ValueError:
                print("Invalid format! Use row,col,num")


game = Sudoku()
game.play()
