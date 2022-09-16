'''
Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
isLeaf: True if the node is leaf node on the tree or False if the node has the four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.
'''

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node': # grid is a square
        end = len(grid)
        gridSum = sum([sum(row) for row in grid])
        
        if gridSum == end**2:
            return Node(1, True)
        
        elif gridSum == 0:
            return Node(0, True)
        
        else:
            node = Node(None, False)
            end //= 2
            node.topLeft = self.construct([row[:end] for row in grid[:end]])
            node.bottomLeft = self.construct([row[:end] for row in grid[end:]])
            node.topRight = self.construct([row[end:] for row in grid[:end]])
            node.bottomRight = self.construct([row[end:] for row in grid[end:]])
            
        return node
      
----------------------------------------------------------------------------------
class MatrixPrefixSum:
    def __init__(self, matrix):
        n = len(matrix)
        self.prefix = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                self.prefix[i][j] = (
                    self.prefix[i][j - 1]  # left
                    + self.prefix[i - 1][j]  # top
                    - self.prefix[i - 1][j - 1]  # overlap
                    + matrix[i - 1][j - 1]
                )

    def get(self, r1, c1, r2=0, c2=0):
        return (
            self.prefix[r1 + 1][c1 + 1]  # all
            - self.prefix[r2][c1 + 1]  # top
            - self.prefix[r1 + 1][c2]  # left
            + self.prefix[r2][c2]  # overlap
        )


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        N = len(grid)
        prefix = MatrixPrefixSum(grid)

        def dfs(r1, c1, width):
            total = prefix.get(r1 + width - 1, c1 + width - 1, r1, c1)
            if total in (0, width * width):
                return Node(int(total > 0), 1, None, None, None, None)

            width >>= 1
            return Node(
                1,
                0,
                dfs(r1, c1, width),
                dfs(r1, c1 + width, width),
                dfs(r1 + width, c1, width),
                dfs(r1 + width, c1 + width, width),
            )

        return dfs(0, 0, N)
