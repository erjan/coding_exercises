'''
This question is about implementing a basic elimination algorithm for Candy Crush.

Given an m x n integer array board representing the grid of candy where board[i][j] represents the type of candy. A value of board[i][j] == 0 represents that the cell is empty.

The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the stable board.
'''


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        #start the while loop
        while True:
            # check for the candies to be crushed
            crush = set()
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if j>1 and board[i][j] and board[i][j] == board[i][j-1] == board[i][j-2]:
                        crush |= {(i,j), (i,j-1), (i,j-2)}
                    if i>1 and board[i][j] and board[i][j] == board[i-1][j] == board[i-2][j]:
                        crush |= {(i,j), (i-1,j), (i-2,j)}
                        
            # crush the candies.
            if not crush: break
            for i, j in crush:
                board[i][j] = 0
                    
            # drop the candies
            for col in range(len(board[0])):
                idx = len(board)-1
                for row in range(len(board)-1, -1, -1):
                    if board[row][col]>0:
                        board[idx][col] = board[row][col]
                        idx -= 1
                        
                for row in range(idx+1):
                    board[row][col] = 0
                    
        return board
      
      
----------------------------------

class Solution:
    
    def __init__(self):
        self.m = 0
        self.n = 0
        self.candyToCrush = set()
    
    def getCandiesToCrush(self, x, y, board, val):
        """ Get indices of the candies that needs to be crushed """
        # for non-zero values
        if val != 0:
            # check horizontally
            if x + 2 < self.m and board[x+1][y] == val and board[x+2][y] == val:
                self.candyToCrush.update([(x,y), (x+1,y), (x+2,y)])
            # check vertically
            if y + 2 < self.n and board[x][y+1] == val and board[x][y+2] == val:
                self.candyToCrush.update([(x,y), (x,y+1), (x,y+2)])
            
    def crushCandies(self, board):
        """ Crush the candies by replacing the candy id to 0 """
        for i, j in self.candyToCrush:
            board[i][j] = 0
        return board
    
    def applyGravity(self, board):
        """ Drop the candies """
        for j in range(self.n):
            # initialize top, bottom
            top = bottom = self.m - 1
            while top >= 0:
                if board[top][j] != 0:
                    board[bottom][j], board[top][j] = board[top][j], board[bottom][j]
                    bottom-=1
                top-=1
        return board
    
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        self.m = len(board)
        self.n = len(board[0])
        
        # reset the hashset
        self.candyToCrush = set()

        for i in range(self.m):
            for j in range(self.n):
                self.getCandiesToCrush(i, j, board, board[i][j])
		
		# stable state achieved
        if len(self.candyToCrush) == 0:
            return board

        # crush candies
        board = self.crushCandies(board)

        # apply gravity
        board = self.applyGravity(board)
            
        return self.candyCrush(board)
