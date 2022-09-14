'''
Given an integer array nums and two integers k and p, return the number of distinct subarrays which have at most k elements divisible by p.

Two arrays nums1 and nums2 are said to be distinct if:

They are of different lengths, or
There exists at least one index i where nums1[i] != nums2[i].
A subarray is defined as a non-empty contiguous sequence of elements in an array.
'''

Explanation

Loop twice
For each subarry, check if the number of elements divisble is less than or equal to 'k'.
If greated than given 'k' then break the inner loop. Else add the current substring to set().add(nums[i:j+1] )
Convert each subarray to string and add it to Set() to easily maintain/discard duplicates.
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        res = set()

        for i in range(n):
            k1 = 0
            for j in range(i, n):
                if nums[j] % p == 0:
                        k1 += 1
                if k1 <= k:
                    res.add(str(nums[i:j+1]))
                else:
                    break

        return len(res)
      
----------------------------------------------------------------------------
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        ans = []
        past = set()
        def dfs(path, ind):
            tmp = 0
            for s in path:
                if int(s)%p == 0:
                    tmp += 1
            if tmp <= k and tuple(path) not in past:
                ans.append(path)
            past.add(tuple(path))
            if ind+1 < len(nums):
                dfs(path + [nums[ind+1]], ind+1)
        for i in range(len(nums)):
                dfs([nums[i]], i)
        return len(ans)
