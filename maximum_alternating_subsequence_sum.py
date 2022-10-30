'''
The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of the elements at odd indices.

For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
Given an array nums, return the maximum alternating sum of any subsequence of nums (after reindexing the elements of the subsequence).

A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.
'''





'''
Intuition
We can use DP (dynamic programming) to loop through nums and find the biggest alternating subsequence num.

Algorithm
We first initialize a n by 2 matrix where n = len(nums). In a supposed index of dp[i][j], i stands for the index of dp based on the such index of nums given from the input, while j stands for whether we add or subtract a number for the last value. If j == 0, then we add, if j==1, then we subtract. This means dp[i][0] means that we have a plus for the last value, while dp[i][1] means we have a minus for the last value. Before we start the iteration, we need to pre-define dp[0][0] as nums[0] as the index is both 0. We also need to pre-define dp[0][1] as 0 since we have to start by adding given the question, thus we put 0.

Next, we iterate through nums in a range for loop from index 1 to n, we start on index 1 instead of 0 because index 0 is already pre-defined. Each iteration, we try either to choose (meaning we choose to go or continue to add/subtract) or not choose (meaning we continue iterating through the array without making an alternating subsequence) for when the last value is plus (dp[i][0]) and when the last value is minus. (dp[i][1]) We take the max of whether to choose or not choose for both when the last value is plus and when the last value is minus.

After we finish iterating, max of dp[-1] is the result, meaning we find the maximum number between when the last value is plus and when the last value is minus.
'''

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)   
        dp = [[0,0] for _ in range(n)] # initialize dp
        dp[0][0] = nums[0] # pre-define
        dp[0][1] = 0 # pre-define

        for i in range(1, n): # iterate through nums starting from index 1
            dp[i][0] = max(nums[i] + dp[i-1][1], dp[i-1][0]) # find which value is higher between choosing or not choosing when the last value is plus.
            dp[i][1] = max(-nums[i] + dp[i-1][0], dp[i-1][1]) # find which value is higher between choosing or not choosing when the last value is minus.
        
        return max(dp[-1]) # find the maximum of the last array of dp of whether the last value is plus or minus, this will be our answer.
