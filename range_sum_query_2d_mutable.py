'''
Given a 2D matrix matrix, handle multiple queries of the following types:

Update the value of a cell in matrix.
Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
void update(int row, int col, int val) Updates the value of matrix[row][col] to be val.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
'''


class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        for row in matrix:
            for col in xrange(1, len(row)):
                row[col] += row[col-1]
        self.matrix = matrix
        

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        original = self.matrix[row][col]
        if col != 0:
            original -= self.matrix[row][col-1]
            
        diff = original - val
        
        for y in xrange(col, len(self.matrix[0])):
            self.matrix[row][y] -= diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0
        for x in xrange(row1, row2+1):
            sum += self.matrix[x][col2]
            if col1 != 0:
                sum -= self.matrix[x][col1-1]
        return sum
----------------------------------------------------------------------------
class NumMatrix(object):
def __init__(self, matrix):
    if not matrix:
        return
    self.m, self.n = len(matrix), len(matrix[0])
    self.matrix, self.bit = [[0]*(self.n) for _ in range(self.m)], [[0]*(self.n+1) for _ in range(self.m+1)]
    for i in range(self.m):
        for j in range(self.n):
            self.update(i, j, matrix[i][j])

def update(self, row, col, val):
    diff, self.matrix[row][col], i = val-self.matrix[row][col], val, row+1
    while i <= self.m:
        j = col+1
        while j <= self.n:
            self.bit[i][j] += diff
            j += (j & -j)
        i += (i & -i)
    
def sumRegion(self, row1, col1, row2, col2):
    return self.sumCorner(row2, col2) + self.sumCorner(row1-1, col1-1) - self.sumCorner(row1-1, col2) - self.sumCorner(row2, col1-1)
    
def sumCorner(self, row, col):
    res, i = 0, row+1
    while i:
        j = col+1
        while j:
            res += self.bit[i][j]
            j -= (j & -j)
        i -= (i & -i)
    return res
  
  
  --------------------------------------------------------------------------------------
  Pretty stadard binary segment tree implementation. It might be slow. It might be bug prone. It might be lengthy and never interview-worthy. But after all, a good programming practice.

class Node:
    def __init__(self, pt1, pt2, sum, lt=None, rt=None, lb=None, rb=None):
        self.pt1, self.pt2 = pt1, pt2
        self.sum = sum
        self.lt, self.rt, self.lb, self.rb = lt, rt, lb, rb

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]: return 
        
        def buildTree(pt1=(0, 0), pt2=(len(matrix)-1, len(matrix[0])-1)):
            if pt1 == pt2: 
                return Node(pt1, pt2, matrix[pt1[0]][pt1[1]])
            
            if pt1[0] > pt2[0] or pt1[1] > pt2[1]: return None
            
            mid1, mid2 = (pt1[0] + pt2[0]) // 2,  (pt1[1] + pt2[1]) // 2
            
            lt = buildTree(pt1, (mid1, mid2))
            rt = buildTree((pt1[0], mid2+1), (mid1, pt2[1]))
            lb = buildTree((mid1+1, pt1[1]), (pt2[0], mid2))
            rb = buildTree((mid1+1, mid2+1), pt2)
            node_sum = sum(n.sum for n in [lt, rt, lb, rb] if n)
            
            return Node(pt1, pt2, node_sum, lt, rt, lb, rb)
        
        self.root = buildTree()
            

    def update(self, row: int, col: int, val: int) -> None:
                
        def update1(node=self.root):
            # print(f'update {(i, j)} at node {node.pt1}, {node.pt2}')
            
            if node.pt1 == node.pt2 == (row, col):
                node.sum = val
                return 
            
            pt1, pt2 = node.pt1, node.pt2
            mid1, mid2 = (pt1[0] + pt2[0]) // 2,  (pt1[1] + pt2[1]) // 2
            
            if pt1[0] <= row <= mid1 and pt1[1] <= col <= mid2: 
                update1(node.lt)
            elif pt1[0] <= row <= mid1 and mid2+1 <= col <= pt2[1]: 
                update1(node.rt)
            elif mid1+1 <= row <= pt2[0] and pt1[1] <= col <= mid2: 
                update1(node.lb)
            elif mid1+1 <= row <= pt2[0] and mid2+1 <= col <= pt2[1]: 
                update1(node.rb)
                
            node.sum = sum(n.sum for n in [node.lt, node.rt, node.lb, node.rb] if n)
        
        update1()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        def sumRegion1(i1=row1, j1=col1, i2=row2, j2=col2, node=self.root):
            if not node or i1 > i2 or j1 > j2: 
                return 0
            if node.pt1 == (i1, j1) and node.pt2 == (i2, j2):
                return node.sum
            
            mid1, mid2 = (node.pt1[0] + node.pt2[0]) // 2,  (node.pt1[1] + node.pt2[1]) // 2
            
            # print(f'sum from {(i1, j1)} to {(i2, j2)} where node is {pt1}, {pt2}')
            return (sumRegion1(i1, j1, min(mid1, i2), min(mid2, j2), node.lt) 
                    + sumRegion1(max(mid1+1, i1), j1, i2, min(mid2, j2), node.lb) 
                    + sumRegion1(i1, max(mid2+1, j1), min(mid1, i2), j2, node.rt) 
                    + sumRegion1(max(mid1+1, i1), max(mid2+1, j1), i2, j2, node.rb) 
                   )
        
        return sumRegion1()
      
      
      ------------------------------------------------------------------------
      First of all, this is not the most optimal solution, but very intuitive if you are familiar with segment trees.
Algorithm is following:

we create a segment tree class with funcitons create, update, query as usual
To initialize: for every row in a matrix we convert it to a segement tree data structure
To update: we just update a segement tree for at a given row
To query: we iterate through the rows of segement trees and collect all sums in a given range.
Solution 1. Segment tree
class SegmentTree:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.N = len(nums)
        self.tree = defaultdict(int)
        # left, right, pos
        self._create(0, self.N - 1, 0)
    
    def _create(self, l: int, r: int, pos: int) -> None:
        if l == r:
            self.tree[pos] = self.nums[l]
            return self.tree[pos]
        mid = l + (r - l) // 2
        left = self._create(l, mid, 2 * pos + 1)
        right = self._create(mid + 1, r, 2 * pos + 2)
        self.tree[pos] = left + right
        return self.tree[pos]
    
    def update(self, ql: int, qr: int, val: int, l: int, r: int, pos: int) -> None:
        if ql <= l <= r <= qr:              # Case 1 total overlap
            self.tree[pos] = val
            return self.tree[pos]
        elif ql > r or qr < l:              # Case 2 NO overlap
            return self.tree[pos]
        mid = l + (r - l) // 2              # Case 3 Partial overlap
        left = self.update(ql, qr, val, l, mid, 2 * pos + 1)
        right = self.update(ql, qr, val, mid + 1, r, 2 * pos + 2)
        self.tree[pos] = left + right
        return self.tree[pos]
    
    def query(self, ql: int, qr: int, l: int, r: int, pos: int) -> int:
        if ql <= l <= r <= qr:              # Case 1 total overlap
            return self.tree[pos]
        elif ql > r or qr < l:              # Case 2 NO overlap
            return 0
        mid = l + (r - l) // 2              # Case 3 Partial overlap
        left = self.query(ql, qr, l, mid, 2 * pos + 1)
        right = self.query(ql, qr, mid + 1, r, 2 * pos + 2)
        return left + right


class NumMatrix:
    '''
    Space complexity: 
        O(mn) we have a segment tree of size n for every column
    
    Time complexity:
        Create: O(mn) 
        Query: O(mlogn)
        Update: O(logn)
        where m is num of rows and n is num of columns
    '''
    def __init__(self, matrix: List[List[int]]):
        if matrix and matrix[0]:
            self.empty = False
            self.N = len(matrix[0])
            self.trees = [0] * len(matrix)
            for i, row in enumerate(matrix):
                self.trees[i] = SegmentTree(row)
        else:
            self.empty = True

    def update(self, row: int, col: int, val: int) -> None:
        if not self.empty:
            self.trees[row].update(col, col, val, 0, self.N - 1, 0)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.empty:
            return 0
        result = 0
        for r in range(row1, row2 + 1):
            result += self.trees[r].query(col1, col2, 0, self.N - 1, 0)
        return result
Solution 2. Binary index tree
This is the same approach but using Binary index tree data structure instead of Segment tree.

class BIT:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.N = len(nums)
        self.tree = nums[:]
        self._create()
        
    def _create(self):
        for i in range(self.N):
            j = i + self._lsb(i)
            if j < self.N:
                self.tree[j] += self.tree[i]
    
    def _lsb(self, i: int) -> int:
        return i & (-i)
    
    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        while i < self.N:
            self.tree[i] += diff
            i += self._lsb(i)
    
    def query_interval(self, i: int, j: int) -> int:
        return self._query(j) - self._query(i-1)
    
    def _query(self, i: int) -> int:
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= self._lsb(i)
        return result
    

class NumMatrix:
    '''
    Space complexity: 
        O(mn) we have a binary index tree of size n for every column
    
    Time complexity:
        Create: O(mn)
        Query: O(mlogn)
        Update: O(logn)
        where m is num of rows and n is num of columns
    '''
    def __init__(self, matrix: List[List[int]]):
        if matrix and matrix[0]:
            self.empty = False
            self.trees = [0] * len(matrix)
            for i, row in enumerate(matrix):
                self.trees[i] = BIT([0] + row)
        else:
            self.empty = True

    def update(self, row: int, col: int, val: int) -> None:
        if not self.empty:
            self.trees[row].update(col + 1, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.empty:
            return 0
        result = 0
        for r in range(row1, row2 + 1):
            result += self.trees[r].query_interval(col1 + 1, col2 + 1)
        return result
      
--------------------------------------------------------------------------------
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        self.bit = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                self.bit[i][j] += matrix[i-1][j-1]
                if (i + (i & (-i))) <= m:
                    self.bit[(i + (i & (-i))) ][j] += self.bit[i][j]
            for j in range(1,n+1):
                if (j + (j & (-j))) <= n:
                    self.bit[i][j + (j & (-j))] += self.bit[i][j]

    def update(self, row: int, col: int, val: int) -> None:
        val -= self.sumRegion(row, col, row, col)
        row, col = row + 1, col + 1
        x = row
        while x < len(self.bit):
            y = col
            while y < len(self.bit[0]):
                self.bit[x][y] += val
                y += y & -y
            x += x & -x
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        def prefixQuery(row, col):
            res = 0
            x = row
            while x:
                y = col
                while y:
                    res += self.bit[x][y]
                    y -= y & -y
                x -= x & -x
            return res
        
        return prefixQuery(row2,col2)+prefixQuery(row1-1,col1-1)-prefixQuery(row1-1,col2)-prefixQuery(row2, col1-1)
      
  
      
