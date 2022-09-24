'''
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
'''


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count, N = 0, len(nums)
        memo = {}
    
        def dfs(i, currentSum):
            if (i, currentSum) in memo: return memo[(i, currentSum)]
            if i == N:
                if currentSum == target: return 1
                return 0
            result = dfs(i + 1, currentSum + nums[i]) + dfs( i + 1, currentSum - nums[i])
            memo[(i , currentSum)] = result
            return result
        return  dfs(0, 0)
