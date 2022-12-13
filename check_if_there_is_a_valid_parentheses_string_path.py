'''
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:

The path starts from the upper left cell (0, 0).
The path ends at the bottom-right cell (m - 1, n - 1).
The path only ever moves down or right.
The resulting parentheses string formed by the path is valid.
Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.
'''


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        if ((rows + cols - 1) % 2 or grid[0][0] == ")"
                or grid[rows - 1][cols - 1] == "("):
            return False
        opened = [[set() for _ in range(cols)] for _ in range(rows)]
        opened[0][0].add(1)
        row = 0
        for col in range(1, cols):
            if grid[row][col] == "(":
                opened[row][col].update(n + 1 for n in opened[row][col - 1])
            else:
                opened[row][col].update(n - 1 for n in opened[row][col - 1]
                                        if n > 0)
        col = 0
        for row in range(1, rows):
            if grid[row][col] == "(":
                opened[row][col].update(n + 1 for n in opened[row - 1][col])
            else:
                opened[row][col].update(n - 1 for n in opened[row - 1][col]
                                        if n > 0)
        for row in range(1, rows):
            for col in range(1, cols):
                opened[row - 1][col].update(opened[row][col - 1])
                if grid[row][col] == "(":
                    opened[row][col].update(n + 1 for n in
                                            opened[row - 1][col])
                else:
                    opened[row][col].update(n - 1 for n in
                                            opened[row - 1][col] if n > 0)
        return 0 in opened[rows - 1][cols - 1]
      
--------------------------------------------------------------------------------------------
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def helper(i, j, score):
            if i == m or j == n:
                return False
            if i == m - 1 and j == n - 1:
                return score == 1 and grid[i][j] == ')'
            
            if grid[i][j] == '(':
                return helper(i + 1, j, score + 1) or helper(i, j + 1, score + 1)
            if score == 0:
                return False
            return helper(i + 1, j, score - 1) or helper(i, j + 1, score - 1)
        
        return helper(0, 0, 0)
