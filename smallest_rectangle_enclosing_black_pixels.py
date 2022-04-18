'''
You are given an m x n binary matrix image where 0 represents a white pixel and 1 represents a black pixel.

The black pixels are connected (i.e., there is only one black region). Pixels are connected horizontally and vertically.

Given two integers x and y that represents the location of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

You must write an algorithm with less than O(mn) runtime complexity

 
 '''


Suppose we have a 2D array

"000000111000000"
"000000101000000"
"000000101100000"
"000001100100000"
Imagine we project the 2D array to the bottom axis with the rule "if a column has any black pixel it's projection is black otherwise white". The projected 1D array is

"000001111100000"
Theorem

If there are only one black pixel region, then in a projected 1D array all the black pixels are connected.

Proof by contradiction

Assume to the contrary that there are disconnected black pixels at i
and j where i < j in the 1D projection array. Thus there exists one
column k, k in (i, j) and and the column k in the 2D array has no
black pixel. Therefore in the 2D array there exists at least 2 black
pixel regions separated by column k which contradicting the condition
of "only one black pixel region".

Therefore we conclude that all the black pixels in the 1D projection
array is connected.

This means we can do a binary search in each half to find the boundaries, if we know one black pixel's position. And we do know that.

To find the left boundary, do the binary search in the [0, y) range and find the first column vector who has any black pixel.

To determine if a column vector has a black pixel is O(m) so the search in total is O(m log n)

We can do the same for the other boundaries. The area is then calculated by the boundaries.
Thus the algorithm runs in O(m log n + n log m)
                                                        
                                                        
                                                        
def minArea(self, image, x, y):
    top = self.searchRows(image, 0, x, True)
    bottom = self.searchRows(image, x + 1, len(image), False)
    left = self.searchColumns(image, 0, y, top, bottom, True)
    right = self.searchColumns(image, y + 1, len(image[0]), top, bottom, False)
    return (right - left) * (bottom - top)

def searchRows(self, image, i, j, opt):
    while i != j:
        m = (i + j) / 2
        if ('1' in image[m]) == opt:
            j = m
        else:
            i = m + 1
    return i

def searchColumns(self, image, i, j, top, bottom, opt):
    while i != j:
        m = (i + j) / 2
        if any(image[k][m] == '1' for k in xrange(top, bottom)) == opt:
            j = m
        else:
            i = m + 1
    return i
                                                        
                                                        
-----------------------------------------------------------------
  Update

Simpler version inspired by yibin_easy's solution.

def minArea(self, image, x, y):
    a, b = (sum('1' in row for row in image)
            for image in (image, zip(*image)))
    return a * b
Or:

def minArea(self, image, x, y):
    return sum('1' in r for r in image) * sum('1' in r for r in zip(*image))
Old

def minArea(self, image, x, y):
    a, b = (max(I) - min(I) + 1
            for image in (image, zip(*image))
            for I in [[i for i, row in enumerate(image) if '1' in row]])
    return a * b
                                                        
--------------------------------------------------------------------------------------
                                                        4 times Binary Search to find top, bottom, leftmost, rightmost.
In example 1, the answer = (bottom - top + 1) * (rightmost - leftmost + 1) = (2 - 0 + 1) * (2 - 1 + 1) = 6.

I heard some people told me that, in the ACM contest, they usually use while left + 1 < right.
Then such writing method will take a side effect, that is, you need to judge after while loop,
because either left or right can be the result.

The good benefit of such writing method is to exclude the crossing border case when you analyse
left or right.

In this question, a little difficult coding part is when you want to compute leftmost or rightmost col. You need to find
whether there is any "1" in the mid col. This is not so easy as searching in row. So you can see I use any function there. But anyway, this is basic running skills of dealing with matrix.

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
                
        def search_top_row(image, left, right):            
            while left + 1 < right:                
                mid = left + (right - left) // 2                
                if "1" in image[mid]:
                    right = mid
                else:
                    left = mid            
            if "1" in image[left]:
                return left
            else:
                return right

            
        def search_bottom_row(image, left, right):
            while left + 1 < right:
                mid = left + (right - left) // 2
                if "1" in image[mid]:
                    left = mid
                else:
                    right = mid
            if "1" in image[right]:
                return right
            else:
                return left

            
        def search_leftmost_col(image, left, right, top, bottom):
            while left + 1 < right:
                mid = left + (right - left) // 2
                temp = []
                for k in range(top, bottom + 1):
                    if image[k][mid] == "1":
                        temp.append(True)
                if any(temp):
                    right = mid
                else:
                    left = mid
            temp1 = []
            for k in range(top, bottom + 1):
                if image[k][left] == "1":
                    temp1.append(True)
            if any(temp1):
                return left
            else:
                return right

            
        def search_rightmost_col(image, left, right, top, bottom):
            while left + 1 < right:
                mid = left + (right - left) // 2
                temp = []
                for k in range(top, bottom + 1):
                    if image[k][mid] == "1":
                        temp.append(True)
                if any(temp):
                    left = mid
                else:
                    right = mid
            temp1 = []
            for k in range(top, bottom + 1):
                if image[k][right] == "1":
                    temp1.append(True)
            if any(temp1):
                return right
            else:
                return left

            
        top = search_top_row(image, 0, x)
		
        bottom = search_bottom_row(image, x, len(image) - 1)
		
        leftmost = search_leftmost_col(image, 0, y, top, bottom)
		
        rightmost = search_rightmost_col(image, y, len(image[0]) - 1, top, bottom)

        
        return (bottom - top + 1) * (rightmost - leftmost + 1)
                                                        
                                                        
------------------------------------------------------
                                                        class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        
        M, N = len(image), len(image[0])
        top, left, right, bottom = x, y, y+1, x+1
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            top, left, right, bottom = min(x, top), min(y, left), max(y+1, right), max(x+1, bottom)
            image[x][y] = '0'
            for r, c in [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]:
                if 0 <= r < M and 0 <= c < N and image[r][c] == '1':
                    stack.append((r, c))
        return (bottom-top)*(right-left)
                                                        
                                                        
---------------------------------------------------------------------
                                                        import math
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        x1 = math.inf
        y1 = math.inf
        x2 = -math.inf
        y2 = -math.inf
        i = 0
        while i<len(image):
            j = 0
            while j<len(image[i]):
                if image[i][j]=="1":
                    if i<y1:
                        y1 = i
                    if i>y2:
                        y2 = i
                    if j<x1:
                        x1 = j
                    if j>x2:
                        x2 = j
                j = j+1
            i = i+1
        x = x2-x1+1
        y = y2-y1+1
        return x*y
                                                        
                                                        
------------------------------------------------------------------------------
                                                        Approach: BFS with axis trace

Initially , Our horizontal axis = 0 and vertical axis = 0

If we go right, horizontal axis = horizontal axis + 1
If we go left, horizontal axis = horizontal axis - 1
If we go top, vertical axis = vertical axis + 1
If we go down, vertical axis = vertical axis - 1

so

Width of Min Area rectangle: Max horizontal axis - Min horizontal axis + 1
Height of Min Area rectangle: Max vertical axis - Min vertical axis + 1

T(N) = O(M*N)
S(N) = O(Min(M,N)) # Queue


from collections import deque

directions = [(-1,0),(1,0),(0,-1),(0,1)]
class Solution:
    def bfs(self,image,x,y):
        
        n = len(image)
        m = len(image[0])
        
        min_horizontal_axis = 0
        max_horizontal_axis = 0
        min_vertical_axis = 0
        max_vertical_axis = 0
        
        queue = deque()
        queue.append((x,y,0,0))
        image[x][y] = "0" # mark
        
        while(len(queue)):
            popped_x,popped_y,h_axis,v_axis = queue.popleft()
            
            for dx,dy in directions:
                u,v = popped_x + dx,popped_y + dy
                
                if 0 <= u < n and 0 <= v < m:
                    
                    # inside bounday
                    if image[u][v] == "1":
                        # unvisited
                        queue.append((u,v,h_axis+dx,v_axis+dy))
                        image[u][v] = "0" # mark
                        
                        min_horizontal_axis = min(min_horizontal_axis,h_axis+dx)
                        max_horizontal_axis = max(max_horizontal_axis,h_axis+dx)
                        min_vertical_axis = min(min_vertical_axis,v_axis+dy)
                        max_vertical_axis = max(max_vertical_axis,v_axis+dy)
        
        print(image)
        
        width = max_horizontal_axis - min_horizontal_axis + 1
        height = max_vertical_axis - min_vertical_axis + 1
        
        return width * height            
                        
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        
        return self.bfs(image,x,y)
                                                        
                                                        
-----------------------------------------------------------------------------
                                                        class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        rows, cols = len(image), len(image[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        minX, maxX = x, x
        minY, maxY = y, y
        stk = []
        stk.append((x,y))
        while stk:
            cX, cY = stk.pop()
			#set the previous match to 0, so we don't go back and forth for ALL OF TIME
            image[cX][cY] = "0"
            for d in directions:
                newX, newY = cX + d[0], cY + d[1]
                if 0 <= newX < rows and 0 <= newY < cols:
                    if image[newX][newY] == "1":
                        stk.append((newX,newY))
                        minX, maxX = min(minX, newX), max(maxX, newX)
                        minY, maxY = min(minY, newY), max(maxY, newY)
            
        
        if minX == x and maxX == x and minY == y and maxY == y:
            return 1
        
        return (maxX - minX + 1) * (maxY - minY + 1)
                                                        
