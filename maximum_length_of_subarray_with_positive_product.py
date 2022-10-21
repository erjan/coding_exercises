'''
Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.




We can simplify the problem:

subarry is continuous, so we can transfer the problem to: For each index i n nums , what is the max length of subarray (ending with index i) With positive product. Then we can iterate every answer for all indexes to get the result for original question.
We know that: positive_number * positive_number is positive, positive_number * negative_number is negative, negative_number * negative_number is positive.
Let's define:
dp[i][0] : max length of subarray ending with index i With positive product
dp[i][1] : max length of subarray ending with index i With negative product

In order to get the answer for current index, we need dp[i - 1][0] and dp[i - 1][1] to form a new subarray.

Implementation:

define a 2D array with length n

Base case would be: when index is 0, only one number can be used

Loop through the array, for the new number we have:

if current number is positive, we know we can definitely form a positive subarry, the length is at least 1:
[previous positive subarray] + [current number positive]
if current number is positive, we know we can form a negative subarray if for previous index, negative subarray exists. Otherwise we can't form a negetive subarray ending with current number
[previous negative subarray] + [current number positive]
if current number is negative, we know we can definitely form a negative subarry, the length is at least 1:
[previous positive subarray] + [current number negative]
if current number is negative, we know we can form a positive subarray if for previous index, negative subarray exists. Otherwise we can't form a positive subarray ending with current number
[previous negative subarray] + [current number negative]

'''

    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]   
        # dp[i][0] : max length of subarray ending with index i With positive product   
		# dp[i][1] : max length of subarray ending with index i With negative product 
		
        # Base case: when index is 0, only one number can be used
        if nums[0] > 0:
            dp[0][0] = 1
        
        if nums[0] < 0:
            dp[0][1] = 1
            
        res = dp[0][0]
        
        for i in range(1, n):
            cur = nums[i]
            
            if cur > 0:
                dp[i][0] = dp[i - 1][0] + 1
                if dp[i - 1][1] > 0: # if previous negative subarray exists
                    dp[i][1] = max(dp[i][1], dp[i - 1][1] + 1)
            if cur < 0:
                dp[i][1] = dp[i - 1][0] + 1
                if dp[i - 1][1] > 0: # if previous negative subarray exists
                    dp[i][0] = max(dp[i][0], dp[i - 1][1] + 1)
                    
            res = max(res, dp[i][0])
            
        return res
    
-------------------------------------------------------------------------------------------------------------------------------    
class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        pos = [0] * n # (1)
        neg = [0] * n # (2)
        
        pos[0] = 1 if nums[0] > 0 else 0
        neg[0] = 1 if nums[0] < 0 else 0
        
        for i in range(1, n):
            if nums[i] < 0:
                pos[i] = 1 + neg[i - 1] if neg[i - 1] else 0
                neg[i] = 1 + pos[i - 1] if pos[i - 1] else 1
            elif nums[i] > 0:
                pos[i] = 1 + pos[i - 1] if pos[i - 1] else 1
                neg[i] = 1 + neg[i - 1] if neg[i - 1] else 0
                    
        return max(pos)
    
    # The idea is to keep track of the maximum length of subarray with negative product and maximum length of subarray with positive product, because depending on the sign of each number we encounter, we want to use each length to inform the other.
    # (1) pos[i] = maximum subarray length with positive product including nums[i] so far
    # (2) neg[i] = maximum subarray length with negative product including nums[i] so far
    # Here are the different possible cases:
    #   - If the number is negative:
    
    #       - If there is a non-empty subarray with negative product to the immediate left of this number:
    #           - Add this number to the subarray with positive product, since negative times negative equals positive.
    #       - Otherwise:
    #           - No subarray with positive product at this point.
    
    #       - If there is a non-empty subarray with positive product to the immediate left of this number:
    #           - Add this number to subarray with negative product, since positive times negative equals negative.
    #       - Otherwise:
    #           - Begin a new subarray with negative product, since a single negative value has a negative product.
    
    #   - If the number is positive:
    
    #       - If there is a non-empty subarray with positive product to the immediate left of this number:
    #           - Add this number to the subarray with positive product, since positive times positive equals positive.
    #       - Otherwise:
    #           - Begin a new subarray with positive product, since a single positive value has a positive product.
    
    #       - If there is a non-empty subarray with negative product to the immediate left of this number:
    #           - Add this number to subarray with negative product, since negative times positive equals negative.
    #       - Otherwise:
    #           - No array with negative product at this point.
