'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
'''

#truth table:
#original new state
#  0       0    0
#  1       0    1
#  0       1    2
#  1       1    3

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        
        def countNeib(r,c):
            nei = 0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if (i == r and j == c) or i < 0 or j < 0 or i == m or j == n:
                        continue
                    if board[i][j] in [1,3]:
                        nei+=1
            return nei
        
        for r in range(m):
            for c in range(n):
                nei = countNeib(r,c)
                
                if board[r][c] == 1:
                    if nei in [2,3]:
                        board[r][c] = 3
                    
                elif nei == 3:
                        board[r][c] = 2
                        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2,3]:
                    board[r][c] = 1
                    
