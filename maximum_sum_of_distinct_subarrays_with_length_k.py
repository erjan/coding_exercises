'''
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.
'''


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        leftpointer = 0
        d = Counter()
        cur = 0
        res = -math.inf
        for rightpointer in range(len(nums)):
            d[nums[rightpointer]] +=1
            cur += nums[rightpointer]

            while d[nums[rightpointer]] >1 or(rightpointer-leftpointer+1) >k:
                cur = cur - nums[leftpointer]
                d[nums[leftpointer]]-=1
                leftpointer+=1
            
            if (rightpointer - leftpointer+1) == k:
                res = max(res,cur)
        
        return res if res != -math.inf else 0

---------------------------------------------------------------------------------------------------------------
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left, right = 0,0
        max_sum = 0
        n = len(nums)
        seen = {}
        current_sum = 0
        while right<n:
            seen[nums[right]] = seen.get(nums[right], 0)+1
            current_sum += nums[right]
            if right-left+1 == k:
                if len(seen) == k:
                    max_sum = max(max_sum, current_sum)
                if seen[nums[left]]>1:
                    seen[nums[left]]-=1
                else:
                    del seen[nums[left]]
                current_sum-=nums[left]
                left+=1
            right+=1
        
        return max_sum
