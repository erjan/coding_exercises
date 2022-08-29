
'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters 
of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once.

'''

class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        visited = {}

        for i in range(m):
            for j in range(n):
                if self.dfs(board,word,i,j,visited):
                    return True

        return False

    def dfs(self,board,word,i,j,visited,pos = 0):
        if pos == len(word):
            return True

        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited.get((i,j)) or word[pos] != board[i][j]:
            return False

        visited[(i,j)] = True
        res = self.dfs(board, word, i, j + 1, visited, pos + 1) \
                    or self.dfs(board, word, i, j - 1, visited, pos + 1) \
                    or self.dfs(board, word, i + 1, j, visited, pos + 1) \
                    or self.dfs(board, word, i - 1, j, visited, pos + 1)

        visited[(i,j)] = False
        return res
