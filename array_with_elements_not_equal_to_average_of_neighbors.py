'''
You are given a 0-indexed array nums of distinct integers. You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.

More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

Return any rearrangement of nums that meets the requirements.
'''

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0,len(nums)-1,2):
            nums[i],nums[i+1]=nums[i+1],nums[i]
        return nums
      
--------------------------------------------------------------
'''
First sort the list, for num on odd indices, switch it with the next one element.
By doing this way, we have a_i > a_(i-1), a_i > a_(i+1), therefore a_i > (a_(i-1) + a_(i+1))/2 for all odd indices and a_i < (a_(i-1) + a_(i+1))/2 for all even indices.
'''

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        for i in range(1, len(nums), 2):
            if i != len(nums)-1:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            
        return nums
      
      
