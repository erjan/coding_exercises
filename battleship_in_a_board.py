'''
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).
'''

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                # if self.isbs(board, i, j):
                if board[i][j] == 'X' and not (i > 0 and board[i - 1][j] == 'X') and not (j > 0 and board[i][j - 1] == 'X'):
                    ans += 1
        
        return ans
      
--------------------------------------------------------------------
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    var = 1
                    if (r > 0 and board[r-1][c] == 'X') or (c > 0 and board[r][c-1] == 'X'):
                        var = 0
                    count += var
        return count
