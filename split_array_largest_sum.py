'''
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.
'''

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def condition(pivot):
            index = 0
            remaining_sub_arrays = k
            cur_sub_array_sum = 0
            while index < len(nums) and remaining_sub_arrays > 0:
                if cur_sub_array_sum + nums[index] > pivot:
                    remaining_sub_arrays -= 1
                    cur_sub_array_sum = nums[index]
                else:
                    cur_sub_array_sum += nums[index]
                index += 1
            return remaining_sub_arrays != 0
        
        start, end = max(nums), sum(nums)
        while start < end:
            pivot = start + (end-start)//2
            if condition(pivot):
                end = pivot
            else:
                start = pivot + 1
        return start
      
----------------------------------------------------------------------------------------------------------------------------
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n<k:return -1
        
        
        def binarySearch(mid):
            arrSum = 0
            count = 1
            
            for i in range(n):
                if arrSum+nums[i]<=mid:
                    arrSum += nums[i]
                    
                else:
                    count+=1
                    if count>k or nums[i]>mid:
                        return False
                    arrSum = nums[i]
            return True
        
        begin = max(nums)
        end = sum(nums)
        res = -1
        
        while begin<=end :
            mid = (begin+end)//2
            
            if binarySearch(mid):
                res = mid 
                end = mid-1
            
            else:
                begin = mid+1
        return res
		
-----------------------------------------------------------------------------------------------
