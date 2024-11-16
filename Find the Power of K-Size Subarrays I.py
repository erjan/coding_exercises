'''
You are given an array of integers nums of length n and a positive integer k.

The power of an array is defined as:

Its maximum element if all of its elements are consecutive and sorted in ascending order.
-1 otherwise.
You need to find the power of all 
subarrays
 of nums of size k.

Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].
'''


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)

        l = 0
        consec = 1

        for r  in range(n):
            if r>0 and nums[r-1] +1 == nums[r]:
                consec+=1
            if r-l+1>k:
                if nums[l]+1 == nums[l+1]:
                    consec-=1
                l+=1
            if r-l+1 ==k:
                res.append(nums[r] if consec == k else -1)
        return res
        


