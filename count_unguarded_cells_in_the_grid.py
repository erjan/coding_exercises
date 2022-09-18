'''
You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.
'''

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0]* n for _ in range(m)]
    

        for i,j in guards:
            matrix[i][j] = 'g'

        for i,j in walls:
            matrix[i][j] = 'w'

        directions = [(-1,0), (0,1), (1,0), (0,-1)]

        def isValid(i,j):
            if i < 0 or j < 0 or i>=m or j >=n:
                return False
            return True

        def dfs(i,j,direction):
            if not isValid(i,j):
                return

            if matrix[i][j] == 'w' or matrix[i][j] == 'g':
                return 

            matrix[i][j] = '*'

            x,y = direction
            new_i = i+x
            new_j = j+y
            if isValid(new_i,new_j):
                dfs(new_i,new_j,direction)

        for i in range(m):
            for j in range(n):

                if matrix[i][j] == 'g':
                    dfs(i-1,j,directions[0])
                    dfs(i,j+1,directions[1])
                    dfs(i+1,j,directions[2])
                    dfs(i,j-1,directions[3])

        c = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    c+=1
        return c
