'''
You are given a 0-indexed integer array nums of length n. You are initially standing at index 0. You can jump from index i 
to index j where i < j if:

nums[i] <= nums[j] and nums[k] < nums[i] for all indexes k in the range i < k < j, or
nums[i] > nums[j] and nums[k] >= nums[i] for all indexes k in the range i < k < j.
You are also given an integer array costs of length n where costs[i] denotes the cost of jumping to index i.

Return the minimum cost to jump to the index n - 1.
'''



The key point is that convert the complex jump rule stated in the question to find the next greater and equal element and next smaller element. And at each i, there are at most 2 possible places to go for next steps.

class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        # key point: jump rule is actually the next greater equal elem or next strict smaller elem.
        n = len(nums)
        minstack = []  # use min mono stack to find the next greater elem.
        nge = [n] * n  # next greater elem at index.
        
        maxstack = [] # use max mono stack to find the next smaller elem.
        nse = [n] * n
        
        # get next greater equal elem.
        for i in range(0, len(nums)):
            while minstack and nums[i] >= nums[minstack[-1]]:
                top = minstack.pop()
                nge[top] = i
            minstack.append(i)
            
        # get next smaller elem.
        for i in range(0, len(nums)):
            while maxstack and nums[i] < nums[maxstack[-1]]:
                top = maxstack.pop()
                nse[top] = i
            maxstack.append(i)
        print(nge, nse)
        
        inf = float("inf")
        dp = [inf for i in range(n)]
        dp[0] = 0
        for i in range(n):
            if nge[i] < n:
                dp[nge[i]] = min(dp[nge[i]], dp[i] + costs[nge[i]])
            if nse[i] < n:
                dp[nse[i]] = min(dp[nse[i]], dp[i] + costs[nse[i]])
        print(dp)
        return dp[-1]
