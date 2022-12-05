'''
You are given an integer array nums and an integer k.

Find the longest subsequence of nums that meets the following requirements:

The subsequence is strictly increasing and
The difference between adjacent elements in the subsequence is at most k.
Return the length of the longest subsequence that meets the requirements.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
'''




# Iterative Segment Tree
class SegmentTree:
    def __init__(self, n, fn):
        self.n = n
        self.fn = fn
        self.tree = [0] * (2 * n)
       
    def query(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l < r:
            if l & 1:
                res = self.fn(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.fn(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = self.fn(self.tree[i * 2], self.tree[i * 2 + 1])
class Solution:
    # Inspired from the solution of Bakerston
    # Basically we make an array to store nums in increasing order and find what is the size of the LIS ending there
	# Our array is 0 to max element from the given nums
    # We need to find the elements smaller than n till the limit k which are in nums before this num
    # so simply all the elements previous to our current num are smaller(till k smaller)
    # now how to find LIS's size?
    # Since we are updating elements left to right in our array we know the LIS's size of elements smaller
    # than our current num
    # we just need to find the largest LIS size in range (num - k, num) from our array
    # This is a range query and can be efficiently answered using Segment Trees.
    
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = max(nums)
        res = 1
        tree = SegmentTree(n, max)
        for num in nums:
            num -= 1
            mm = tree.query(max(0, num - k), num)
            tree.update(num, mm + 1)
            res = max(res, mm + 1)
        return res
      
----------------------------------------------------------------------------------------------------------------------
class SegTree: 

    def __init__(self, arr: List[int]): 
        self.n = len(arr)
        self.tree = [0] * (2*self.n)
        # for i in range(2*self.n-1, 0, -1): 
        #     if i >= self.n: self.tree[i] = arr[i - self.n]
        #     else: self.tree[i] = max(self.tree[i<<1], self.tree[i<<1|1])

    def query(self, lo: int, hi: int) -> int: 
        ans = 0 
        lo += self.n 
        hi += self.n
        while lo < hi: 
            if lo & 1: 
                ans = max(ans, self.tree[lo])
                lo += 1
            if hi & 1: 
                hi -= 1
                ans = max(ans, self.tree[hi])
            lo >>= 1
            hi >>= 1
        return ans 

    def update(self, i: int, val: int) -> None: 
        i += self.n 
        self.tree[i] = val
        while i > 1: 
            self.tree[i>>1] = max(self.tree[i], self.tree[i^1])
            i >>= 1

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        m = max(nums)
        ans = 0 
        tree = SegTree([0] * (m+1))
        for x in nums: 
            val = tree.query(max(0, x-k), x) + 1
            ans = max(ans, val)
            tree.update(x, val)
        return ans 
