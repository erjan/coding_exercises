'''
A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

 
 '''

First, by appending nums to nums, you can ignore the effect of split case.
Then, you look at the window whose width is width. Here, width = the number of 1's in the original nums. This is because you have to gather all 1's in this window at the end of some swap operations. Therefore, the number of swap operation is the number of 0's in this window.
The final answer should be the minimum value of this.

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        width = sum(num == 1 for num in nums) #width of the window
        nums += nums
        res = width
        curr_zeros = sum(num == 0 for num in nums[:width]) #the first window is nums[:width]
        
        for i in range(width, len(nums)):
            curr_zeros -= (nums[i - width] == 0) #remove the leftmost 0 if exists
            curr_zeros += (nums[i] == 0) #add the rightmost 0 if exists
            res = min(res, curr_zeros) #update if needed
        
        return res
