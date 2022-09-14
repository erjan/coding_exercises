'''
You are given a 0-indexed 8 x 8 grid board, where board[r][c] represents the cell (r, c) on a game board. On the board, free cells are represented by '.', white cells are represented by 'W', and black cells are represented by 'B'.

Each move in this game consists of choosing a free cell and changing it to the color you are playing as (either white or black). However, a move is only legal if, after changing it, the cell becomes the endpoint of a good line (horizontal, vertical, or diagonal).

A good line is a line of three or more cells (including the endpoints) where the endpoints of the line are one color, and the remaining cells in the middle are the opposite color (no cells in the line are free). You can find examples for good lines in the figure below:
'''

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        l = len(board)
        
        if color == 'W':
            opp = 'B'
        else:
            opp = 'W'
        
        def search(d):
            x,y = rMove+d[0], cMove+d[1]
            
            cnt = 0
            while 0<=x<l and 0<=y<l and board[x][y] == opp:
                cnt += 1
                x,y = x+d[0], y+d[1]
            
            if 0<=x<l and 0<=y<l and board[x][y] == color and cnt >= 1:
                return True
            else:
                return False
            
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(1,1),(-1,1),(-1,-1)]
        return any(search(d) for d in directions)
