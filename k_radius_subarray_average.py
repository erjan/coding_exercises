'''
You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.
'''



class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1]*n
        if k*2 >= n:
            return result
        
        prefix_sum = [0]
        for v in nums:
            prefix_sum.append(prefix_sum[-1] + v)
        
        for i in range(k, n - k):
            # Since we have +1 indexes on prefix_sum we need to access the indexes one to the right
            result[i] = (prefix_sum[i+k+1] - prefix_sum[i-k]) // (k*2+1)
        return result
        
-----------------------------------------------------------------------------------------------------------
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * n
        running_sum = 0
        
        # We need n to be at least k*2+1 since k must be on both left and right sides
        if k*2 >= n:
            return result
        
        # run only on the range that we know contains k for both sides
        for i in range(k, n - k):
            # the first iteration we calculate the sliding window sum
            if i == k:
                running_sum = sum(nums[:i+k+1])
                result[i] = running_sum//(k*2+1)
                continue
            
            # on other iterations we remove the element that went out and insert the element that went in
            running_sum -= nums[i-k-1]
            running_sum += nums[i+k]
            result[i] = running_sum//(k*2+1)
        
        return result
