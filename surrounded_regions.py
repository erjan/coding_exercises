'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.board = board
        row = len(board)
        if row <=2:return
        col = len(board[0])
        if col <=2: return

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and (i == 0 or j == 0 or i == (row -1) or j == (col-1)):
                    self.dfs(i,j)

        for i in range(row):
            for j in range(col):
                if self.board[i][j] == 'O':self.board[i][j] = 'X'
                elif self.board[i][j] == 'A':self.board[i][j] = 'O'
        
    def dfs(self, i,j):
        if i >= 0 and i < len(self.board) and j  >=0 and j < len(self.board[0]) and self.board[i][j] == 'O':
            self.board[i][j] = 'A'
            self.dfs( i+1, j)
            self.dfs( i-1,j)
            self.dfs( i, j+1)
            self.dfs( i, j-1)
            
    
       
        
