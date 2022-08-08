'''
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.
'''

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        
        res = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[j] - nums[i] == diff and nums[k]-nums[j] == diff:
                        res+=1
        return res
                        
----------------------------------------------------------------------------------
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i] + diff in nums and nums[i] + 2 * diff in nums:
                ans += 1
        
        return ans

-----------------------------------------------------------
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i] + diff in nums and nums[i] + 2 * diff in nums:
                ans += 1
        
        return ans
        
-----------------------------------------------------------------------------------
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        t = len(nums)

        def binary_search(arr, low, high, x):
 
            if high >= low:

                mid = (high + low) // 2

                if arr[mid] == x:
                    return mid


                elif arr[mid] > x:
                    return binary_search(arr, low, mid - 1, x)

                else:
                    return binary_search(arr, mid + 1, high, x)

            else:
                return -1
 
        count = 0
        for i,n in enumerate(nums):
            if binary_search(nums, 0, i-1, n-diff) != -1  and binary_search(nums, i+1, t-1,n + diff) != -1:
                count+=1
        
        return count
