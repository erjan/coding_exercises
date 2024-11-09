'''
You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of nums is x.

Return the minimum possible value of nums[n - 1].
'''

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x

        rem = n-1
        position = 1

        while rem:
            if not (x&position):
                res |= (rem&1)*position
                rem>>=1
            position <<=1
        return res
