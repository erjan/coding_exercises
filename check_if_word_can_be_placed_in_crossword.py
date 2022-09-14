'''
You are given an m x n matrix board, representing the current state of a crossword puzzle. The crossword contains lowercase English letters (from solved words), ' ' to represent any empty cells, and '#' to represent any blocked cells.

A word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top) in the board if:

It does not occupy a cell containing the character '#'.
The cell each letter is placed in must either be ' ' (empty) or match the letter already on the board.
There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.
There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.
Given a string word, return true if word can be placed in board, or false otherwise.
'''


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        W = len(word)
        
        def valid(x, y):
            return 0 <= x < m and 0 <= y < n
        
        def place(x, y, word, direction):
            dx, dy = direction
            for c in word:
                if not valid(x, y) or board[x][y] == '#' or (board[x][y] != ' ' and board[x][y] != c):
                    return False
                x, y = x+dx, y+dy
            return True
            
        
        for x in range(m):
            for y in range(n):
                if board[x][y] == '#' or (board[x][y] != ' ' and board[x][y] != word[0]):
                    continue
                
                # left to right
                if (not valid(x, y-1) or board[x][y-1] == '#') and (not valid(x, y+W) or board[x][y+W] == '#') and place(x, y, word, [0, 1]):
                    return True
                
                # right to left
                if (not valid(x, y+1) or board[x][y+1] == '#') and (not valid(x, y-W) or board[x][y-W] == '#') and place(x, y, word, [0, -1]):
                    return True
                
                # top to bottom
                if (not valid(x-1, y) or board[x-1][y] == '#') and (not valid(x+W, y) or board[x+W][y] == '#') and place(x, y, word, [1, 0]):
                    return True
                
				# bottom to top
                if (not valid(x+1, y) or board[x+1][y] == '#') and (not valid(x-W, y) or board[x-W][y] == '#') and place(x, y, word, [-1, 0]):
                    return True
                
        return False
----------------------------------------------------------------------------
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        len_word = len(word)
        
        # Return True if the indices are inbound
        def inbound(i: int, j: int) -> bool:
            return 0 <= i < m and 0 <= j < n
        
        # Return True if a board cell doesn't match the letter in the word
        def mismatch(i: int, j: int, char_index: int) -> bool:
            return board[i][j] != ' ' and board[i][j] != word[char_index] and board[i][j] != word[-char_index-1]
        
        # Return True if the word can be placed as a crossword
        def check(i: int, j: int, di: int, dj: int) -> bool:
            for char_index in range(len_word):
                if not inbound(i, j) or board[i][j] == '#' or mismatch(i, j, char_index):
                    return False
                i, j = i+di, j+dj
            return True
        
        for x, y in product(range(m), range(n)):
            if board[x][y] == '#' or mismatch(x, y, 0):
                continue
            
            # Check horizontally placing the word
            if (not inbound(x, y-1) or board[x][y-1] == '#') and (not inbound(x, y+len_word) or board[x][y+len_word] == '#') and check(x, y, 0, 1):
                return True
            
            # Check vertically placing the word
            if (not inbound(x-1, y) or board[x-1][y] == '#') and (not inbound(x+len_word, y) or board[x+len_word][y] == '#') and check(x, y, 1, 0):
                return True
        
        return False

--------------------------------------------------------
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        words=[word,word[::-1]]
        n=len(word)
        for B in board,zip(*board):
            for row in B:
                q=''.join(row).split('#')
                for w in words:
                    for s in q:
                        if len(s)==n:
                            if all(s[i]==w[i] or s[i]==' ' for i in range(n)):
                                return True
        return False
      
