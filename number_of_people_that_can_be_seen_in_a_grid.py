'''
You are given an m x n 0-indexed 2D array of positive integers heights where heights[i][j] is the height of the person standing at position (i, j).

A person standing at position (row1, col1) can see a person standing at position (row2, col2) if:

The person at (row2, col2) is to the right or below the person at (row1, col1). More formally, this means that either row1 == row2 and col1 < col2 or row1 < row2 and col1 == col2.
Everyone in between them is shorter than both of them.
Return an m x n 2D array of integers answer where answer[i][j] is the number of people that the person at position (i, j) can see.
'''



Explanation
Below is a Python 3 implementation of hint section in the problem description
Two things need to be aware in Python implementation
Python built-in bisect library only works with ascendingly-ordered sequence, thus we will need a deque to make sure the sequence behaves like a mono-stack while maintaining increasing order
When doing binary search, there are two cases need to be considered
num = 3, s = [1], in this case, binary search will give us idx = 1
num = 3, s = [1,4], in this case, binary search will give us idx = 1, but since 4 is the first number larger than 3, it should be considered as visiable too.
In conclusion, we will need to plus 1 if idx < len(s) else 0
Time: O(mnlog(mn)) = O(mnlog(n) + mnlog(m))
For more intuition, please read hint section in the problem description
Implementation
class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        ans = [[0] * n for _ in range(m)]
        s = collections.deque()                   # a deque behave like mono-stack
        for i in range(m):                        # look right
            for j in range(n-1, -1, -1):
                num = heights[i][j]
                idx = bisect.bisect_left(s, num)  # binary search on an increasing order sequence
                ans[i][j] += idx + (idx < len(s)) # if `idx` is not out of bound, meaning the next element in `s` is the first one large than `num`, we can count it too
                while s and s[0] <= num:          # keep a mono-descreasing stack
                    s.popleft()
                s.appendleft(num)    
            s.clear()
        for j in range(n):                        # look below
            for i in range(m-1, -1, -1):
                num = heights[i][j]
                idx = bisect.bisect_left(s, num)
                ans[i][j] += idx + (idx < len(s))
                while s and s[0] <= num:
                    s.popleft()
                s.appendleft(num)    
            s.clear()
        return ans
--------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m): 
            stack = []
            for j in range(n): 
                prev = -inf
                while stack and heights[i][stack[-1]] < heights[i][j]: 
                    if prev < heights[i][stack[-1]]: ans[i][stack[-1]] += 1
                    prev = heights[i][stack.pop()]
                if stack and prev < heights[i][stack[-1]]: ans[i][stack[-1]] += 1
                stack.append(j)
        for j in range(n): 
            stack = []
            for i in range(m): 
                prev = -inf 
                while stack and heights[stack[-1]][j] < heights[i][j]: 
                    if prev < heights[stack[-1]][j]: ans[stack[-1]][j] += 1
                    prev = heights[stack.pop()][j]
                if stack and prev < heights[stack[-1]][j]: ans[stack[-1]][j] += 1
                stack.append(i)
        return ans 
