'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
'''

Usually sliding window has 3 steps:

Put current element into the window
When some conditions can not be satisfied, make the left element out
compute the res for every eligible window
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        if not nums:
            return 0
        
        # find the longest subseq that has at most k zeroes
        res = 0
        left = 0
        
        count = 0
        
        for i in range(len(nums)):
            
            cur = nums[i]
            
            # 1. in
            if cur == 0:
                count += 1
            
            # 2. out
            while count > k:
                
                if nums[left] == 0:
                    count -= 1
                
                left += 1
            
            # 3. compute
            res = max(res, i - left + 1)
        
        return res
      
---------------------------------------------------
def longestOnes(self, nums: List[int], k: int) -> int:
	n, ans, l = len(nums), 0, 0
	for r in range(n):
		if nums[r] == 0:                       # try to pick current 0
			if k == 0:                         # if window already picked k zeros, pop 1 from left and pick this
				while nums[l] != 0 : l += 1
				l += 1
			else : k-= 1                       # otherwise pick it and decrement k
		ans = max(ans, r - l + 1)              # update ans as max window size till now
	return ans

---------------------------------------------------------------------------------------------------------------------
This is a very typical problem that can be solved using the sliding window approach with a hashmap.

The intuition is that we want at most to have k 0's in our subarray, so we'll keep track of how many 0's and 1's we have up until now and if the number of 0's exceeds k, then we slide the left side of the window over until we have k 0's again.

Time complexity is O(n) because we only have to iterate over the array once and space complexity is O(1) because our hashmap stays constant regardless of the input.

If you have trouble understanding what's going on in the while loop, just remember that when we move our left pointer to the right (i.e., we shrink the window size) we no longer are keeping track of the leftmost element. Therefore, we decrement its count from the hashmap.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        answer = 0
        counts = {0: 0, 1: 0}
        
        for right, num in enumerate(nums):
            counts[num] += 1
            
            while counts[0] > k:
                counts[nums[left]] -= 1
                left += 1
                
            curr_window_size = right - left + 1
            answer = max(answer, curr_window_size)
            
        return answer
