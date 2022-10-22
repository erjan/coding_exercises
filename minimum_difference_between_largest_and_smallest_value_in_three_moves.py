'''
You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.
'''


If the size <= 4, then just delete all the elements and either no or one element would be left giving the answer 0.
else sort the array
there are 4 possibilities now:-

delete 3 elements from left and none from right
delete 2 elements from left and one from right
and so on.. now just print the minima.

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 4: return 0
        nums.sort()
        return min(nums[-1] - nums[3], nums[-2] - nums[2], nums[-3] - nums[1], nums[-4] - nums[0])
      
---------------------------------------------------------------------------------------------------------------
class Solution:
    
    def minDifference(self, nums: List[int]) -> int:
        
        n = len(nums)
        # If nums are less than 3 all can be replace,
        # so min diff will be 0, which is default condition
        if n > 3:
            
            # Init min difference
            min_diff = float("inf")
            
            # sort the array
            nums = sorted(nums)
            
            # Get the window size, this indicates, if we
            # remove 3 element in an array how many element
            # are left, consider 0 as the index, window
            # size should be (n-3), but for array starting
            # with 0 it should be ((n-1)-3)
            window = (n-1)-3
            
            # Run through the entire array slinding the
            # window and calculating minimum difference
            # between the first and the last element of
            # that window
            for i in range(n):
                if i+window >= n:
                    break
                else:
                    min_diff = min(nums[i+window]-nums[i], min_diff)
                    
            # return calculated minimum difference
            return min_diff
        
        return 0 # default condition
