'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
'''


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def valid_move(r, c, n):
            for i in range(9):
                if board[i][c]==n: return False
                if board[r][i]==n: return False
                if board[3*(r//3)+i//3][3*(c//3)+i%3]==n: return False
            return True
        
        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c]!=".": continue
                    for n in "123456789":
                        if valid_move(r, c, n):
                            board[r][c] = n
                            if backtrack(): return True
                            board[r][c] = "."
                    return False
            return True
        backtrack()
