'''
Given an integer array nums sorted in non-decreasing order and an integer target, return true if target is a majority element, or false otherwise.

A majority element in an array nums is an element that appears more than nums.length / 2 times in the array.
'''

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        l = len(nums)
        
        t_count = nums.count(target)
        
        if t_count > l/2:
            return True
        return False
      
      
      
#another O log n

def isMajorityElement(self, nums, target):

        def search(a, x):
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) // 2
                if a[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
            
        N = len(nums)
        if nums[N // 2] != target:
            return False
        lo = search(nums, target)
        hi = search(nums, target + 1)
        return hi - lo > N // 2

    
    
#-----------------------------
During an interview, we would think a bit more. Letting x be our majority element, a sorted array containing a majority element would look like one of the following:

[ x x x x x x x . . . . . . ]        # majority at the beginning
[ . . . x x x x x x x . . . ]        # majority at the middle
[ . . . . . . x x x x x x x ]        # majority at the ending
If there is a majority element then when we examine the middle index of the array, we are guaranteed to find the majority element. So we can binary search for the beginning and end of the streak:

def isMajorityElement(self, nums, target):
    N = len(nums)
    if nums[N // 2] != target:
        return False
    lo = bisect.bisect_left(nums, target)
    hi = bisect.bisect_right(nums, target)
    return hi - lo > N // 2
