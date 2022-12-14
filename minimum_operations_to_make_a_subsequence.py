'''
You are given an array target that consists of distinct integers and another integer array arr that can have duplicates.

In one operation, you can insert any integer at any position in arr. For example, if arr = [1,4,1,2], you can add 3 in the middle and make it [1,4,3,1,2]. Note that you can insert the integer at the very beginning or end of the array.

Return the minimum number of operations needed to make target a subsequence of arr.

A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.
'''

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        loc = {x: i for i, x in enumerate(target)}
        stack = []
        for x in arr: 
            if x in loc: 
                i = bisect_left(stack, loc[x])
                if i < len(stack): stack[i] = loc[x]
                else: stack.append(loc[x])
        return len(target) - len(stack)
      
-------------------------------------------------------------------------------
class Solution(object):
    def minOperations(self, target, arr):
        d = {num: idx for idx, num in enumerate(target)}
        arr = [d.get(num, -1) for num in arr]
        res = []
        for num in arr:
            if num == -1: continue
            else:
                pos = bisect.bisect_left(res, num)
                if pos == len(res):
                    res.append(num)
                else:
                    res[pos] = min(res[pos], num)
        return len(target) - len(res)
      
-------------------------------------------------------------------------------------------
class Solution:
    def minOperations(self, target, arr):
        n, nums = len(target), []
        D = {target[i]: i for i in range(n)}
        res = [D[i] for i in arr if i in D.keys()]
        for i in res:
            j = bisect.bisect_left(nums, i)
            if j == len(nums): nums.append(i)
            else: nums[j] = i
        return n - len(nums)
