'''
Given an m x n matrix grid containing an odd number of integers where each row is 
sorted in non-decreasing order, return the median of the matrix.

You must solve the problem in less than O(m * n) time complexity.
'''




'''
Explanation
The idea is simple:
Find the smallest & largest number and used it as range for candidates
For each candidate, conduct a binary search on it
Now discuss the complexity:
People may argue the time complexity is O(mlgn * lg(hi - lo)), not O(mlgn)
But in fact, max(hi - lo) = 1,000,000, and log(1,000,000) ~= 14 (base e), so pretty much a constant, thus we can say it's a O(mlgn) solution
Implementation
'''

class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        lo, hi = sys.maxsize, -sys.maxsize
        for i in range(m):                               # find the larget & smallest number in `grid`
            lo = min(lo, grid[i][0])
            hi = max(hi, grid[i][-1])
        total = m * n            
        half = total // 2
        while lo <= hi:                                  # start binary search
            cnt = 0
            mid = (lo + hi) // 2
            for i in range(m):                           # O(m)
                cnt += bisect.bisect_right(grid[i], mid) # O(lgn)
            if cnt <= half:                              # `mid` too small to be a median
                lo = mid + 1
            else:                                        # `mid` (might be) too large to be a median
                hi = mid - 1
        return lo

---------------------------------------------------------------------------------------------

class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        indexs = [0] * m
        heap = []
        for i in range(m):
            heappush(heap, (grid[i][0], i))
        k = 0
        midIndex = (m * n) // 2 
        while True:
            (val, row) = heappop(heap)
            k += 1
            if k == midIndex + 1:
                return val
            if indexs[row] < n - 1:
                indexs[row] += 1
                heappush(heap, (grid[row][indexs[row]], row))
        return -1
      
      
