
'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        temp =0
        for i in range(len(nums)-1):
            
            if nums[i+1] < nums[i]:
                temp = i+1
        return nums[temp]
        
-----------------------------------------------------------
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        first = 0
        last = len(nums)-1
        
        while first < last:
            mid = (first+last)//2
            
            if nums[mid] > nums[last]:
                
                first = mid+1
            else:
                last = mid
        return nums[first]
