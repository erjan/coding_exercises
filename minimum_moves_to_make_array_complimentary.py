'''
You are given an integer array nums of even length n and an integer limit. In one move, you can replace any integer from nums with another integer between 1 and limit, inclusive.

The array nums is complementary if for all indices i (0-indexed), nums[i] + nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.

Return the minimum number of moves required to make nums complementary.
'''


the logic is that we try to calculate the interval for each pair if we make one move
the interval is [min(nums[i],nums[n-i-1])+1, max(nums[i],nums[n-i-1])+limit]
we only record the interval boundaries and calculate the number of overlapped invervals in one-pass

from collections import defaultdict

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
                
        sum_count = defaultdict(int)
        m = len(nums)//2
        interval = [0]*(2*limit+2)
        for i in range(m): # calculate the interval boundaries
            s = nums[i]+nums[len(nums)-1-i]
            sum_count[s]+=1
            interval[min(nums[i],nums[len(nums)-1-i])+1]+=1
            interval[max(nums[i],nums[len(nums)-1-i])+limit+1]-=1
        ans = float("inf")
        for i in range(1,len(interval)): 
            interval[i]+=interval[i-1]
            ans = min(ans, 2*(m-interval[i])+interval[i]-sum_count[i])
        return ans        
