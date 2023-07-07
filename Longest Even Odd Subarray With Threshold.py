
'''
You are given a 0-indexed integer array nums and an integer threshold.

Find the length of the longest subarray of nums starting at index l and ending at index r (0 <= l <= r < nums.length) that satisfies the following conditions:

nums[l] % 2 == 0
For all indices i in the range [l, r - 1], nums[i] % 2 != nums[i + 1] % 2
For all indices i in the range [l, r], nums[i] <= threshold
Return an integer denoting the length of the longest such subarray.

Note: A subarray is a contiguous non-empty sequence of elements within an array.
'''



class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        

        res = 0

        for i in range(len(nums)):

            cnt = 0

            if nums[i]%2 == 0 and nums[i]<=threshold:
                cnt = 1

                for j in range(i+1, len(nums)):

                    if nums[j]%2 != nums[j-1]%2 and nums[j]<=threshold:
                        cnt+=1
                    else:
                        break
            res = max(res,cnt)
        return res
