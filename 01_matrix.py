'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        DEFAULT = -1
        queue = []
        result = [[DEFAULT] * len(mat[0]) for _ in range(len(mat))]
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    queue.append((r, c, 0)) # depth is 0. i.e. 0 steps to get to this 0
                    result[r][c] = 0
                    
        visited = set()
        while queue:
            row, col, depth = queue.pop(0)
            
            if (row, col) in visited:
                continue
                
            visited.add((row, col))
            if result[row][col] == DEFAULT: # no other 0 has gotten here first
                result[row][col] = depth
                
            # if in bounds, not visited, and no result from another 0 yet
            if row > 0 and (row - 1, col) not in visited and result[row - 1][col] == DEFAULT:
                queue.append((row - 1, col, depth + 1))
            if row < len(mat) - 1 and (row + 1, col) not in visited and result[row + 1][col] == DEFAULT:
                queue.append((row + 1, col, depth + 1))
            if col > 0 and (row, col - 1) not in visited and result[row][col - 1] == DEFAULT:
                queue.append((row, col - 1, depth + 1))
            if col < len(mat[0]) - 1 and (row, col + 1) not in visited and result[row][col + 1] == DEFAULT:
                queue.append((row, col + 1, depth + 1))
                
        return result
