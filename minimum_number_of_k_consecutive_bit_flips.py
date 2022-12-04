'''
You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.
'''


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        ans = 0
        q = []
        for i in range(len(nums)):
            if len(q) % 2 == 0:
                if nums[i] == 0:
                    if i+k-1 <= len(nums)-1:
                        ans += 1
                        q.append(i+k-1)
                    else:
                        return -1
            else:
                if nums[i] == 1:
                    if i+k-1 <= len(nums)-1:
                        ans += 1
                        q.append(i+k-1)
                    else:
                        return -1
            if q:
                if q[0] == i:
                    q.pop(0)
        return ans
