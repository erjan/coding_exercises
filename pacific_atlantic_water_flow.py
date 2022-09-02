'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
'''


def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:return []
        m, n = len(matrix),len(matrix[0])
        p_visited = set()
        a_visited = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def dfs(visited, x,y):
            visited.add((x,y))
            for dx, dy in directions:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<m and 0<=new_y<n and (new_x,new_y) not in visited and matrix[new_x][new_y]>=matrix[x][y]:
                    dfs(visited, new_x,new_y)
        #iterate from left border and right border
        for i in range(m):
            dfs(p_visited,i,0)
            dfs(a_visited,i,n-1)
        #iterate from up border and bottom border
        for j in range(n):
            dfs(p_visited,0,j)
            dfs(a_visited,m-1,j)
        #The intersections of two sets are coordinates where water can flow to both P and A
        return list(p_visited.intersection(a_visited))
