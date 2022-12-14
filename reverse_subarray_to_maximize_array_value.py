'''
You are given an integer array nums. The value of this array is defined as the sum of |nums[i] - nums[i + 1]| for all 0 <= i < nums.length - 1.

You are allowed to select any subarray of the given array and reverse it. You can perform this operation only once.

Find maximum possible value of the final array.
'''

class Solution:
    # For nums = [x0, x1,..., a, [b,....,c],d,..., xn-1]
    # In we flip [b,....,c], we have these scenarios:
    # 1. [min[a,b], max[a,b]], [min[c,d],max[c,d]] intersect
    # 2. They do not
    # in the first case, we cannot increase the value (One really should draw the possible scenarios to convince yourself)
    # in the second case, there is a gain of 2*(min(a,b) - max(c,d)) (if positive, otherwise reverse sign)
    # Therefore we should iterate through the pairs and find max(min(a,b)) - min(max(a,b))
    # We should notice the edge should also be taken care of. This can done when handling the pairs
    
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        result, n, value, maxmin, minmax = 0, len(nums), 0, -100001, 100001
        for i in range(n-1):
            a, b = nums[i], nums[i+1]
            value += abs(a-b)
            result = max(result, abs(nums[0]-b) - abs(a-b))
            result = max(result, abs(nums[-1]-a) - abs(a-b))
            maxmin, minmax = max(maxmin, min(a,b)), min(minmax, max(a,b))
        return value + max(result, 2*(maxmin-minmax))
