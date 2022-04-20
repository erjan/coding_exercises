'''
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there is not one, return 0 instead.

 

Example 1:

Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
'''

A lot of solutions here either put i+1 to history (sum) hashmap or start it with {0: -1}, which makes the code just less maintainable, and to be honest the reason of doing so isn't very obvious. I just couldn't get my head around that. Following solution solves the same problem without going through that indexing mess.

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen_sum = {0:0}
        total_sum, largest_len = 0, 0
        for i in range(len(nums)):
            total_sum += nums[i]
            if total_sum == k:
                largest_len = i + 1
            else: 
                required = total_sum - k
                if required in seen_sum:
                    largest_len = max(largest_len, i - seen_sum[required])
            if total_sum not in seen_sum:
                seen_sum[total_sum] = i
        return largest_len
      
--------------------------------------------

Thought process
store the leftmost index for cumulated sum
iterate through nums, when curr_sum - k is in sum_indexes, try to update max_length with i (current index) - sum_indexes[curr_sum - k)
O(n) time | O(n) space
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_indexes = {0: -1}
        curr_sum = 0
        res = 0
        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum - k in sum_indexes:
                res = max(res, i - sum_indexes[curr_sum - k])
            if curr_sum not in sum_indexes:
                sum_indexes[curr_sum] = i
        return res
-----------------------------------------------------------
                                                                                                                         
                                                                                                                         Algo
Compute prefix sum and check if prefix - k has been seen before. If so, update ans if the length is longer.

Implementation

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        seen = {0: -1}
        ans = prefix = 0
        for i, x in enumerate(nums): 
            prefix += x
            if prefix-k in seen: 
                ans = max(ans, i - seen[prefix-k])
            seen.setdefault(prefix, i)
        return ans 
Analysis
Time complexity O(N)
Space complexity O(N)
-------------------------------------------------------
                                                                                                                         
   class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
		#Basically the same as two sum: if I've seen sum-k before, I know I can get a valid subarray solution.
        d={}
        s=0
        M=0
        for i,v in enumerate(nums):
            s+=v
            if s-k in d:
                if i-d[s-k]>M:
                    M=i-d[s-k]
            if s==k:
                if i+1>M:
                    M=i+1
            if s not in d:
                d[s]=i
        return M
                                                                                                                         
---------------------------------------------                                                                                                                         
                                                    
                                                                                                                         
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum_map = {0:-1}  # mapping of sum_up_to_index_i : i 
        cur_sum , max_len = 0, 0
        for i in range(n):
            cur_sum += nums[i]     # cur_sum upto index i
            remain = cur_sum - k    
            if remain in sum_map: # if cur_sum - k, means  some_sum + k  == cur_sum , was there in past
                max_len = max(max_len , i-sum_map[remain])  # from that index to i , sum is k
            if cur_sum not in sum_map:
                sum_map[cur_sum] = i   # store the current sum for future check
            
        return max_len```
                                                                                                                         
