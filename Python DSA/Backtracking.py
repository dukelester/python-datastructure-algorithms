'''
Uses the brute forcing algorithm to find a solution
tries all the possible solutions and outputs the desired solution
uses recursion to find the best solution


Problems in backtracking ::
    decision problem ==> search for the feasible solution
    optimization problem ==> search for the best solution
    enumeration problem ==> find all the feasible solutions

    traverses a tree in recursive manner in depth first search

'''

#the N-Queern Problem

class NQueens:
    def __init__(self, n):
        self.n = n
        self.chess_table =[[0 for i in range(n)] for j in range(n)]


    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print('Q', end="")
                else:
                    print("-" ,end=" ")
            print('\n')

    def is_place_safe(self, row_index, column_index):
        for i in range(self.n):
            if self.chess_table[row_index][i] == 1:
                return False

        j = column_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j = j -1

        j = column_index
        for i in range(row_index, self.n):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j = j -1
        return True


    def solve(self, column_index):
        if column_index == self.n:
            return True

        for row_index in range(self.n):
            if self.is_place_safe(row_index, column_index):
                self.chess_table[row_index][column_index] = 1
                if self.solve(column_index + 1):
                    return True
                self.chess_table[row_index][column_index] = 0

        return False

    def solve_NQueens(self):
        if self.solve(0):
            self.print_queens()
        else:
            print("No solution exists for the problem")



queens = NQueens(10)
queens.solve_NQueens()

print([[number for number in range(20)] for n in range(20)])