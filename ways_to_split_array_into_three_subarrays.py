'''
A split of an integer array is good if:

The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.

 '''

from bisect import *

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        mod = 10**9+7
        
        pre_sum = [0]
        for num in nums: 
            pre_sum.append(pre_sum[-1]+num)
        
        res = 0
        
        for i in range(1, len(nums)): 
            l = bisect_left(pre_sum, 2*pre_sum[i])
            r = bisect_right(pre_sum, (pre_sum[i]+pre_sum[-1])//2)
            res += max(0, min(len(nums), r)-max(i+1, l))
            
        return res%mod
      
------------------------------------------------------------------------------
Calculate prefix sum and store at pre_sum
Iterate each index i and consider it as the ending index of the 1st segment
Do binary search on the 2nd segment ending index. This is doable because pre_sum is a non-decreasing array
[i+1, j] is the shortest possible segment of the 2nd segment (bisect_left)
Condition to find: pre_sum[i] * 2 <= pre_sum[j]
Meaning the 2nd segment sum will not be less than the 1st segment sum
[i+1, k-1] is the longest possible segment of the 2nd segment (bisect_right)
Condition to find: pre_sum[k-1] - pre_sum[i] <= pre_sum[-1] - pre_sum[k-1]
Meaning the 3rd segment sum will not be less than the 2dn segment sum
For example, all combinations below will be acceptable
		# [0, i], [i+1, j], [j+1, n-1]
		# [0, i], [i+1, j+1], [j+2, n-1]
		# [0, i], [i+1, ...], [..., n-1]
		# [0, i], [i+1, k-2], [k-1, n-1]
		# [0, i], [i+1, k-1], [k, n-1]
Don't forget to handle the edge case when k == n
Time: O(NlogN)
Space: O(N)
Implementation
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        mod, pre_sum = int(1e9+7), [nums[0]]
        for num in nums[1:]:                               # create prefix sum array
            pre_sum.append(pre_sum[-1] + num)
        ans, n = 0, len(nums)
        for i in range(n):                                 # pre_sum[i] is the sum of the 1st segment
            prev = pre_sum[i]                              # i+1 is the starting index of the 2nd segment
            if prev * 3 > pre_sum[-1]: break               # break loop if first segment is larger than the sum of 2 & 3 segments
                
            j = bisect.bisect_left(pre_sum, prev * 2, i+1) # j is the first possible ending index of 2nd segment
                
            middle = (prev + pre_sum[-1]) // 2             # last possible ending value of 2nd segment
            k = bisect.bisect_right(pre_sum, middle, j+1)  # k-1 is the last possible ending index of 2nd segment
            if k-1 >= n or pre_sum[k-1] > middle: continue # make sure the value satisfy the condition since we are using bisect_right here
            ans = (ans + min(k, n - 1) - j) % mod          # count & handle edge case
        return ans
