'''
Given a sorted (in ascending order) integer array nums of n 
elements and a target value, write a function to search target 
in nums. If target exists, then return its index, otherwise return -1.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <=high:
            mid = (low + high)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid+1
            else:
                high = mid-1
        return -1
