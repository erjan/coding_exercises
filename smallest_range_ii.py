'''
You are given an integer array nums and an integer k.

For each index i where 0 <= i < nums.length, change nums[i] to be either nums[i] + k or nums[i] - k.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after changing the values at each index.
'''

class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        mini = A[0]
        maxi = A[-1]
        res = maxi - mini
        for i in range(len(A)-1):
            res = min(res, max(maxi-K, A[i]+K) - min(mini+K, A[i+1]-K))
        return res
      
---------------------------------------------------------------------------------------------------------------------
#heap

	class Solution:
		def smallestRangeII(self, nums: List[int], k: int) -> int:
			newNums = [(x - k, True) for x in nums]
			largest = max(newNums, key=lambda a: a[0])[0]
			heapq.heapify(newNums)
			result = abs(newNums[0][0]-largest)
			while newNums[0][1]:
				result = min(result, abs(newNums[0][0]-largest))
				popped = heapq.heappop(newNums)
				heapq.heappush(newNums, (popped[0] + 2*k, False))
				largest = max(largest, popped[0] + 2*k)
			result = min(result, abs(newNums[0][0]-largest))
			return result
        
-------------------------------------------------------------------------------------------------------------------
# Approach 1: 
# Time complexity:  O(n)
# Space complexity: O(1)
# ----------------
# The idea is to minimize the difference between max and min:
    # Max value tends to become smaller
    # Min value tends to become larger
# Cause A[i] < A[i + 1], to minimize the difference:
    # make smaller larger: A[i] + K, A[0] + K
    # make larger smaller: A[i + 1] - K, A[-1] - K
# Update the Max and Min:
    # max: max(A[-1] - K, A[i] + K)
    # min: min(A[0] + K, A[i + 1] - K)
# Update the result:
    # res = max - min
# We know, A - B = (A + K) - (B + K),
    # res = max - min = max(A[-1] - K, A[i] + K) - min(A[0] + K, A[i + 1] - K)
    # res = max - min = max(A[-1], A[i] + 2 * K) - min(A[0] + 2 * K, A[i + 1])
# ----------------

def smallestRangeII(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums.sort()
    mn, mx = nums[0], nums[-1]
    res = mx - mn
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            mx = max(nums[-1] - k, nums[i]   + k)
            mn = min(nums[0]  + k, nums[i+1] - k)
            res = min(res, mx - mn)

    return res
        
