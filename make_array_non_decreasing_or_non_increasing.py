'''
You are given a 0-indexed integer array nums. In one operation, you can:

Choose an index i in the range 0 <= i < nums.length
Set nums[i] to nums[i] + 1 or nums[i] - 1
Return the minimum number of operations to make nums non-decreasing or non-increasing.
'''


    def convertArray(self, nums: List[int]) -> int:
        def helper(nums):
            que = [] # stores negative number, to make max heap.
            res = 0
            for num in nums:
                if que and num<(-que[0]):
                    res += abs(num-(-heapq.heappop(que)))
                    heapq.heappush(que,-num) # reduce max to num, then push back
                heapq.heappush(que,-num)
            return res
        return min(helper(nums),helper(nums[::-1]))
      
------------------------------------------------------------------------------------------------

'''
DP O(n^2):
We only need to look at ”increasing“ case, decreasing is same as increasing with reversed nums.
dp(i, level) means the minimum operations needed to make nums increasing until nums[i], with nums[i] <= level.
dp(i, level) = min(dp(i-1, level0) + abs(nums[i]-level0)) for all "level0<=level".

Here "dp(i-1, level) + abs(nums[i] - level)" means minimum operations needed to make nums increasing until nums[i], with nums[i] == level. This is the result for nums[i] == level, but not nums[i]<= level as defined by DP. So we calculate same way for all levels that <= "level", the minimum result will be dp(i, level).

For python, the key not getting TLE is to NOT checking every single level, instead checking only those levels that exists in nums.
Both ways have same time complexity, but one get passed, one get TLE. That's why I think this quesiton is too strict for python.
'''


    def convertArray(self, nums: List[int]) -> int:
        levels = sorted(set(nums))
        def helper(nums):
            dp = defaultdict(int)
            for num in nums:
                cur_res = math.inf
                for cur_level in levels:
                    cur_res = min(cur_res,dp[cur_level]+abs(num-cur_level))
                    dp[cur_level] = cur_res
            return dp[levels[-1]]
        return min(helper(nums),helper(nums[::-1]))




