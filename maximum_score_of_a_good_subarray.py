'''
You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.

 
 '''
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        ans = mn = nums[k]
        lo = hi = k
        while 0 <= lo-1 or hi+1 < len(nums): 
            if lo == 0 or hi+1 < len(nums) and nums[lo-1] < nums[hi+1]: 
                hi += 1
                mn = min(mn, nums[hi])
            else: 
                lo -= 1
                mn = min(mn, nums[lo])
            ans = max(ans, mn * (hi-lo+1))
        return ans 
---------------------------------------------------------------------------------------------
def maximumScore(self, nums: List[int], k: int) -> int:
	n = len(nums)
	left, right = [1 for _ in range(n)], [1 for _ in range(n)]
	stack = []
	for i in range(n):
		ele = nums[i]
		while(stack and stack[-1][0] >= ele):
			stack.pop()
		left[i] = i-(stack[-1][1] if(stack) else -1)
		stack.append([ele, i])
	stack = []
	for i in range(n-1, -1, -1):
		ele = nums[i]
		while(stack and stack[-1][0] >= ele):
			stack.pop()
		if(stack):
			right[i] = stack[-1][1] - i
		else:
			right[i] = n-i
		stack.append([ele, i])
	ans = 0
	# print(left, right)
	for i in range(n):
		if(i-left[i] < k and i + right[i] > k):
			ans = max(ans, nums[i] * (left[i]+right[i]-1))
	return ans
