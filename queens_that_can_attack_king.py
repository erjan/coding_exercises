'''
On an 8x8 chessboard, there can be multiple Black Queens and one White King.

Given an array of integer coordinates queens that represents the positions of the Black Queens, and a pair of coordinates king that represent the position of the White King, return the coordinates of all the queens (in any order) that can attack the King.
'''

class Solution:
    def queensAttacktheKing(self, queens, king):
        x,y = king[1],king[0] # king's location
        qs = {(q[1],q[0]) for q in queens} # locations of queens
        dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]] # 8 directions a queen can attack

        def dfs(x,y,dx,dy):
            if 0<=x<=7 and 0<=y<=7:
                if (x,y) in qs: return [y,x]
                return dfs(x+dx, y+dy, dx, dy)
            return None

        res = []
        for dx, dy in dirs:
            r = dfs(x+dx, y+dy, dx, dy)
            if r: res.append(r)
        return res
