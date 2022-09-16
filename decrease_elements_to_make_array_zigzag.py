'''
Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.

An array A is a zigzag array if either:

Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
Return the minimum number of moves to transform the given array nums into a zigzag array.
'''

class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        zig, zag = 0, 0
        prev_zig, prev_zag = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            if i % 2 == 0:
                zig += max(0, prev_zig - nums[i] + 1)
                prev_zig = nums[i] 
                zag += max(0, nums[i] - prev_zag + 1)
                prev_zag = nums[i] - max(0, nums[i] - prev_zag + 1)
            else:
                zag += max(0, prev_zag - nums[i] + 1)
                prev_zag = nums[i]
                zig += max(0, nums[i] - prev_zig + 1)
                prev_zig = nums[i] - max(0, nums[i] - prev_zig + 1)
        
        return min(zig, zag)
      
---------------------------------------------------------------------------------

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def greedy(nums, small_first=True):
            if n <= 1: return 0
            ans = 0
            for i in range(n-1):
                if small_first and nums[i] >= nums[i+1]:
                    ans += nums[i] - (nums[i+1]-1)
                    nums[i] = nums[i+1] - 1
                elif not small_first and nums[i] <= nums[i+1]:
                    ans += nums[i+1] - (nums[i]-1)
                    nums[i+1] = nums[i] - 1
                small_first = not small_first
            return ans    
        n = len(nums)
        return min(greedy(nums[:], True), greedy(nums[:], False))
