'''
Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.

Test cases are generated such that partitioning exists.

 
 '''


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        """
        Intuition(logic) is to find two maximums.
        One maximum is for left array and other maximum is for right array.
        
        But the condition is that, the right maximum should be such that, 
        no element after that right maximum should be less than the left maximum. 
        
        If there is any element after right maximum which is less than left maximum,
        that means there is another right maximum possible and therefore in that case assign
        left maximum to right maximum and keep searching the array for correct right
        maximum till the end.
        """
        #start with both left maximum and right maximum with first element.
        left_max = right_max = nums[0]
        # our current index
        partition_ind = 0
        # Iterate from 1 to end of the array
        for i in range(1,len(nums)):
            #update right_max always after comparing with each nums
            #in order to find our correct right maximum
            right_max = max(nums[i], right_max)
            """
			if current element is less than left maximum, that means this 
            element must belong to the left subarray. 
              * so our partition index will be updated to current index 
              * and left maximum will be updated to right maximum. 
             Why left maximum updated to right maximum ?
              Because when we find any element less than left_maximum, that 
              means the right maximum which we had till now is not valid and we have
              to find the valid right maximum again while iterating through the end of the loop.
			"""
            if nums[i] < left_max:
                left_max = right_max
                partition_ind = i
        
        return partition_ind+1
      
--------------------------------------------------------------------------
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        leftMax = nums[0]
        curMax = nums[0]
        ans = 1
        for i, num in enumerate(nums):
			# If current number is smaller than left maximum, the answer is no longer valid.
			# Now the current index is the last index of left and the maximum is now left maximum.
            if num < leftMax:
                ans = i+1  
                leftMax = curMax
			# Update the current maximum
            curMax = max(curMax, num)

        return ans
