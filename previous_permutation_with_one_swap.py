'''
Given an array of positive integers arr (not necessarily distinct), return 
the lexicographically largest permutation that is smaller than arr, that can be made with exactly
one swap (A swap exchanges the positions of two numbers arr[i] and arr[j]). If it cannot be done, then return the same array.
'''


class Solution:
	 def prevPermOpt1(self, nums: List[int]) -> List[int]:
		n = len(nums)-1
		left = n

    // find first non-decreasing number
    while left >= 0 and nums[left] >= nums[left-1]:
        left -= 1
        
	// if this hits, it means we have the smallest possible perm 
    if left <= 0:
        return nums
	
	// the while loop above lands us  at +1, so k is the actual value
    k = left - 1
    
    // find the largest number that's smaller than k 
    // while skipping duplicates
    right = n
    while right >= left:
        if nums[right] < nums[k] and nums[right] != nums[right-1]:
            nums[k], nums[right] = nums[right], nums[k]
            return nums
            
        right -= 1
   
    return nums
