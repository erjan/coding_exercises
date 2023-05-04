'''
You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.
'''

'''
Intuition
To minimize the maximum difference amongst all the pairs, we need to find a maximum difference that satisfies the given condition of having p pairs of indices of nums. Since we want to minimize the maximum difference, we can use binary search to find the smallest maximum difference that satisfies the given condition.

Approach
First, we sort the input list of integers. We define the minimum and maximum possible values for the maximum difference. The minimum value is 0 since the difference between any two elements is at least 0. The maximum value is the difference between the largest and smallest elements in the list since that is the maximum difference possible.

We perform binary search for the smallest maximum difference that satisfies the given condition. In each iteration, we calculate the mid-point of the possible range of maximum differences. We then count the number of pairs of adjacent integers with a difference less than or equal to the mid-point maximum difference. If the number of such pairs is greater than or equal to p, we decrease the maximum possible value of the maximum difference. Otherwise, we increase the minimum possible value of the maximum difference.

We continue this process until the minimum and maximum values converge to the same value, which is the smallest maximum difference that satisfies the given condition.
'''



class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # Sort the input list of integers
        nums.sort()
        n = len(nums)
        
        # Define the minimum and maximum possible values for the maximum difference
        min_max_diff = 0
        max_max_diff = nums[-1] - nums[0]
        
        # Binary search for the smallest maximum difference that satisfies the given condition
        while min_max_diff < max_max_diff:
            mid_max_diff = (min_max_diff + max_max_diff) // 2
            
            # Count the number of pairs of adjacent integers with a difference less than or equal to mid_max_diff
            pair_count = 0
            i = 1
            while i < n:
                if nums[i] - nums[i-1] <= mid_max_diff:
                    pair_count += 1
                    i += 1
                i += 1
            
            # If the number of such pairs is greater than or equal to p, decrease the maximum possible value of the maximum difference
            if pair_count >= p:
                max_max_diff = mid_max_diff
            # Otherwise, increase the minimum possible value of the maximum difference
            else:
                min_max_diff = mid_max_diff + 1
        
        # Return the smallest maximum difference that satisfies the given condition
        return min_max_diff
