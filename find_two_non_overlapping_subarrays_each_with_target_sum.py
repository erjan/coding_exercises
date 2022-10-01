'''
You are given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.
'''


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        l, windowSum, res = 0, 0, float('inf')
        min_till = [float('inf')] * len(arr) # records smallest lenth of subarry with target sum up till index i.
        for r, num in enumerate(arr): # r:right pointer and index of num in arr
            windowSum += num
            while windowSum > target: 
			# when the sum of current window is larger then target, shrink the left end of the window one by one until windowSum <= target
                windowSum -= arr[l]
                l += 1
			# the case when we found a new target sub-array, i.e. current window
            if windowSum == target:
			   # length of current window
                curLen = r - l + 1
				# min_till[l - 1]: the subarray with min len up till the previous position of left end of the current window: 
				# avoid overlap with cur window
				# new_sum_of_two_subarray = length of current window + the previous min length of target subarray without overlapping
				# , if < res, update res.
                res = min(res, curLen + min_till[l - 1])
				# Everytime we found a target window, update the min_till of current right end of the window, 
				# for future use when sum up to new length of sum_of_two_subarray and update the res.
                min_till[r] = min(curLen, min_till[r - 1])
            else:
			# If windowSum < target: window with current arr[r] as right end does not have any target subarry, 
			# the min_till[r] doesn't get any new minimum update, i.e it equals to previous min_till at index r - 1. 
                min_till[r] = min_till[r - 1]
        return res if res < float('inf') else -1
      
-------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        ## RC ##
        ## APPROACH : DP ##        
		## Similar to Leetcode: 123 Best Time To Buy And Sell Stock III ##
        ## LOGIC ##
        ## 1. Like typical subarray sum problem, calculate the valid subarray lengths at that particular index using running/prefix sum
        ## 2. dp will have the minimum subarray length with sum = target found till that index.
        ## 3. now reverse the array and compute the same. (we now have both dp_left and dp_right)
        ## 4. As there should not be any overlaps, we consider minimum found till index - 1 in left side and minimum found from this current index till end on right side. Compute the sum and store in ans.
		
		## INTUITION ## (How did I get to know that I have to use dp_left and dp_ right ?)
		## As we are finding only 2 best cases, if we consider any particular index, one best case can be to its left side , othe best case can be to its right side ##
        
		## TIME COMPLEXICITY : O(3xN) ##
		## SPACE COMPLEXICITY : O(N) ##
        
        def get_sub_arrays( arr ):
            lookup = collections.defaultdict(int)
            running_sum = 0
            dp = [float('inf')] * len(arr)
            
            for i, num in enumerate(arr):
                running_sum += num
                if running_sum == target:
                    dp[i] = i - 0 + 1
                elif running_sum - target in lookup:
                    dp[i] = i - lookup[running_sum - target] + 1
                lookup[running_sum] = i+1
                dp[i] = min( dp[i-1], dp[i] )
            return dp
        
        dp_left = get_sub_arrays( arr )                     # from front
        dp_right = get_sub_arrays( arr[::-1] )[::-1]        # from backwards
        
        ans = float('inf')
        for i in range( 1, len(arr) ):
            ans = min( ans, dp_left[i-1] + dp_right[i] )
        return ans if( ans != float('inf') ) else -1
