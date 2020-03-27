class Solution:
    def missingNumber(self, nums):
        largest = len(nums)
        s1 = 0
        s2 = 0
        for item in range(largest + 1):
            s1 ^= item
        for num in nums:
            s2 ^= num
        return s1 ^ s2
        
#bitwise trick - dont understand it
