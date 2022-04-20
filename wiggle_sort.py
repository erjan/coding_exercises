'''
Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

You may assume the input array always has a valid answer.

 

Example 1:

Input: nums = [3,5,2,1,6,4]
Output: [3,5,1,6,2,4]
Explanation: [1,6,2,5,3,4] is also accepted.
Example 2:

Input: nums = [6,6,5,6,3,8]
Output: [6,6,5,6,3,8]

'''

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        # Time: O(n), Space: O(1)
        swap=True
        for i in range(len(nums)-1):
            if (swap and nums[i]>nums[i+1]) or (not swap and nums[i]<nums[i+1]):
                nums[i],nums[i+1]=nums[i+1],nums[i]
            swap = not swap
    
    def wiggleSort1(self, nums: List[int]) -> None:
        # Time: O(nlogn), Space: O(1)
        nums.sort()
        for i in range(1,len(nums)-1,2):
            nums[i],nums[i+1]=nums[i+1],nums[i]
--------------------------------------------------------------------------

from collections import deque

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Init
        queue = deque(sorted(nums))
        nums.clear()
        flag = True
        
        # Wiggle sort
        while queue:
            nums.append(queue.popleft() if flag else queue.pop())
            flag = False if flag else True
        
        return
-------------------------------------------------------

Algorithm:
We go through nums one by one, as soon as we see a pair of numbers that don't satisfy the wiggle condition, we swap them greedily/immediately.

Why it works:
Suppose we have three numbers [a, b, c], optimal substructure guarantees that a and b are in their correct positions. If the wiggle condition requires that a > b < c but we have a > b > c, the wiggle condition is violated. Why does swapping b and c restores the wiggle condition? After swapping we have [a, c, b]. We know that a > b > c which implies that a > c. We also know that b > c. Therefore we have a > c < b.

Code:

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if i%2 == 0 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif i%2 == 1 and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
--------------------------------------------------------------------

ShamelessSelfPromotion: My other leetcode solutions to various questions can be found here

Algorithm:

Sort the Array in-place.
Swap the indexed starting from 2, till the end of the array and skip the indexes by two.
Time: O(NLogN)
Space: O(1)

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
		
        for i in range(2, len(nums), 2):
            nums[i], nums[i-1] = nums[i-1], nums[i]
---------------------------------------------------------------------------

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if i % 2 == 0 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            if i % 2 !=0 and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums
      
          
                
      
            
