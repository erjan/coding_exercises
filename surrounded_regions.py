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
            
    
 #--------------------------------------------without class - only functions ----------------------------
def print_grid(grid):
    print('------------------------')
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end = ' ')
        print()
    
def solve( board):
    row = len(board)
    if row <=2:return
    col = len(board[0])
    if col <=2: return

    for i in range(row):
        for j in range(col):
            if board[i][j] == 'O' and (i == 0 or j == 0 or i == (row -1) or j == (col-1)):
                 dfs(board,i,j)

    for i in range(row):
        for j in range(col):
            if  board[i][j] == 'O': board[i][j] = 'X'
            elif  board[i][j] == 'A': board[i][j] = 'O'
        
def dfs(board, i,j):
    if i >= 0 and i < len( board) and j  >=0 and j < len( board[0]) and  board[i][j] == 'O':
         board[i][j] = 'A'
         dfs(board, i+1, j)
         dfs(board, i-1,j)
         dfs(board, i, j+1)
         dfs(board, i, j-1)
             
g = [
["O","X","X","X"],
["X","X","O","X"],
["X","O","O","X"],
["O","O","X","X"]
]

print_grid(g)
solve(g)
print_grid(g)

'''
my own explanation: 
find the o on the border - it's first or last row or first or last column
mark them as V(visited) and traverse dfs style to see if they are connected to any other next surrounding cells
mark them too
traverse again thru the list to see and mark any 0s with x and any Visited V as O
done
'''
