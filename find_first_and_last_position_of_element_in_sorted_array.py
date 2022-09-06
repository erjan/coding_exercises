'''
Given an array of integers nums sorted in non-decreasing order, find the 
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''


#wrong solution
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def bs(nums, n):

            l = 0
            r = len(nums)-1
            mid = 0

            while l <= r:

                mid = (l + r)//2

                if nums[mid] < n:
                    l = mid+1

                elif nums[mid] > n:
                    r = mid-1

                else:
                    return mid
            return -1
    
        if len(nums) == 2 and nums[0] == nums[1] == target:
            return [0,1]
        
        if len(nums) == 0:
            return [-1, -1]
        
        if nums.count(target) == 0:
            return [-1, -1]

        if nums.count(target) == 1:
            index = bs(nums, target)
            return [index, index]

        else:
            index = bs(nums,target)
            if nums[index-1] == target:
                return [index-1,index]
            elif nums[index+1] == target:
                return [index, index+1]
              
------------------------------------------------------------------------------------
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        left = self.bs(nums,target, True)
        right = self.bs(nums,target,False)
        return [left,right]
    
    def bs(self,nums, target, leftBias):

        l = 0
        r = len(nums)-1
        index = -1

        while l <= r:

            mid = (l + r)//2

            if target > nums[mid]:
                l = mid+1

            elif target < nums[mid]:
                r = mid-1

            else:
                index = mid
                if leftBias:
                    r = mid-1
                else:
                    l = mid+1
        return index

-----------------------------------------------------------------------------------------------
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        low, high = 0, len(nums)-1
        first = self.findFirstIndex(nums, low, high, target)

        second = self.findLastIndex(nums, low, high, target)
        
        return [first, second]
    def findFirstIndex(self, nums, low, high, target):
        res = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                res = mid
                high = mid-1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid + 1
        return res
    
    def findLastIndex(self, nums, low, high, target):
        res = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                res = mid
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid + 1
        return res
