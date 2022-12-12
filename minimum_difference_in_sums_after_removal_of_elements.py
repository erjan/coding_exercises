'''
You are given a 0-indexed integer array nums consisting of 3 * n elements.

You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:

The first n elements belonging to the first part and their sum is sumfirst.
The next n elements belonging to the second part and their sum is sumsecond.
The difference in sums of the two parts is denoted as sumfirst - sumsecond.

For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
Return the minimum difference possible between the sums of the two parts after the removal of n elements.
'''


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//3
        pq0 = [-x for x in nums[:n]]
        pq1 = nums[-n:]
        
        heapify(pq0)
        heapify(pq1)
        
        ans = -sum(pq0) - sum(pq1)
        prefix = [0]
        for i in range(n, 2*n): 
            prefix.append(prefix[-1])
            if nums[i] < -pq0[0]: 
                prefix[-1] += nums[i] + pq0[0]
                heapreplace(pq0, -nums[i])
        extra = prefix[-1]
        suffix = 0 
        for i in reversed(range(n, 2*n)): 
            if nums[i] > pq1[0]: 
                suffix += pq1[0] - nums[i]
                heapreplace(pq1, nums[i])
            extra = min(extra, prefix[i-n] + suffix)
        return ans + extra
