'''
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.
'''


class Solution:
    def solve(self, nums, res, cnt, n):
        if cnt >= n:
            if cnt == n and res not in self.visit:
                return res
            return 0
        for val in nums:
            temp = self.solve(nums, res+val, cnt+1, n)
            if temp:
                return temp
            else:
                continue
    
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        self.visit = nums
        return self.solve(['0', '1'], '', 0, len(nums))
