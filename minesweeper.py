'''
Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 
 '''

def updateBoard(board, click):
	i, j, m, n = *click, len(board), len(board[0])
	def dfs(i, j):
		if board[i][j] == 'E':
			neis = [(x,y) for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1))
						if 0 <= x < m and 0 <= y < n]
			cnt = sum(board[x][y]=='M' for x,y in neis)
			if not cnt: 
				board[i][j] = 'B'
				for x, y in neis: dfs(x,y)
			else: board[i][j] = str(cnt)
	if board[i][j] == 'M': board[i][j] = 'X'
	else: dfs(i,j)
	return board

---------------------------------------------------------------------------------
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        ## RC ##
        ## APPROACH : DFS ##
        
        def adjacent_mines(i, j):
            mines = 0
            for x, y in directions:
                if 0 <= i + x < M and 0 <= j + y < N and board[i + x][j + y] == "M":
                    mines += 1
            return mines
        
        def dfs(i, j):
            
            # mark adjacent mine count at click position and return the board
            mines = adjacent_mines(i, j)
            if mines:
                board[i][j] = str(mines)
                return board
            
            # if no adjacent mines found then, do DFS
            board[i][j] = "B"
            
            for x, y in directions:
                if 0 <= i + x < M and 0 <= j + y < N and board[i + x][j + y] == "E":
                    dfs(i + x, j + y)
            return board
            
        
        if not board: return board
        M = len(board)
        N = len(board[0])
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1,1), (1,-1), (-1,1), (-1,-1)]
        
        # if click directly has mine, mark it as X and return
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        # if board has 'E' then check neighbors
        if board[click[0]][click[1]] == "E":
            return dfs(click[0], click[1])
