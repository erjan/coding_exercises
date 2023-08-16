'''
You are given a 0-indexed integer array nums. You have to find the maximum sum of a pair of numbers from nums such that the maximum digit in both numbers are equal.

Return the maximum sum or -1 if no such pair exists.
'''


class Solution:

    def getmaxdigit(self, n):      
        curmaxd = list(str(n))
        curmaxd = max([int(x) for x in curmaxd])
        return curmaxd
    def maxSum(self, nums: List[int]) -> int:



        res = -1

        for i in range(len(nums)):
            
            curmaxd = self.getmaxdigit(nums[i])
            
            for j in range(i+1, len(nums)):

                curm2 = self.getmaxdigit(nums[j])

                if curm2 == curmaxd:
                    res = max(res, nums[i]+nums[j])
        
        if res == -1:
            return -1
        return res

---------------------------------------------------------------------------------------------
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        d, ans = defaultdict(list), -1
        
        for num in nums: d[max(str(num))].append(num)   # <-- 1)
            
        for ch in d:
            if len(d[ch]) < 2: continue

            ans = max(ans, sum(sorted(d[ch])[-2:]))     # <-- 2)

        return  ans                                     # <-- 3)
