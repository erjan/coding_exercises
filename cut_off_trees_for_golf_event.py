'''
You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:

0 means the cell cannot be walked through.
1 represents an empty cell that can be walked through.
A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.
In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

Note: The input is generated such that no two trees have the same height, and there is at least one tree needs to be cut off.
'''

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        forest.append([0] * len(forest[0]))
        for row in forest: row.append(0)
        # distance
        def distance(i, j, I, J):
            manhattan = abs(i - I) + abs(j - J)
            detour = 0
            good, bad = [(i, j)], []
            visited = set()
            while True:
                if not good:
                    good, bad = bad, []
                    detour += 1
                i, j = good.pop()
                if i == I and j == J: return manhattan + detour * 2
                if (i, j) in visited: continue
                visited.add((i, j))
                for i, j, closer in ((i-1, j, i > I), (i+1, j, i < I), (i, j+1, j < J), (i, j-1, j > J)):
                    if forest[i][j]:
                        (good if closer else bad).append((i, j))
                    
        trees = [(height, r, c) for r, row in enumerate(forest) for c, height in enumerate(row) if forest[r][c] > 1]
        # check
        queue = [(0, 0)]
        reached = set()
        reached.add((0, 0))
        while queue:
            r, c = queue.pop()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                row, col = r + dr, c + dc
                if forest[row][col] and (row, col) not in reached:
                    queue.append((row, col))
                    reached.add((row,col))
        if not all([(i, j) in reached for (height, i, j) in trees]): return -1
        trees.sort()
        return sum([distance(i, j, I, J) for (_, i, j), (_, I, J) in zip([(0, 0, 0)] + trees, trees)])
