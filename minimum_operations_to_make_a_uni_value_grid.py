'''
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.
'''
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        numRows, numCols, nums = len(grid), len(grid[0]), []
        for row in range(numRows):
            for col in range(numCols):
                nums.append(grid[row][col])
        nums.sort()
        median, ans = nums[len(nums) // 2], 0
        for num in nums:
            quotient, remainder = abs(num - median) // x, abs(num - median) % x
            if remainder:
                return -1
            ans += quotient
        return ans
      
-----------------------------------------------------------------------------------------------
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        res = []

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                res.append(grid[i][j])

        res.sort()


        rem = res[0] % x
        for i in range(1, len(res)):
            if res[i] % x != rem:
                return -1

        q = res[len(res)//2]

        moves = 0
        for n in res:
            moves += abs(n-q)//x
        return moves
--------------------------------------------------------------------------------------------------------

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        # flatten the numbers
        nums = []
        for row in grid:
            for num in row:
                nums.append(num)
        
        # sort and find the median
        nums.sort()
        n = len(nums)
        median = nums[n//2]
        
        # calculate the number of operations required
        operations = 0
        for num in nums:
            diff = abs(median-num)
            if diff%x !=0:
                return -1
            operations += diff//x
        
        return operations
