'''
Given an array nums of distinct positive integers, return 
the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.
'''

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:	
        temp = []
		
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                temp.append(nums[i] * nums[j])
        
        temp = collections.Counter(temp)
        ans = 0
        
        for i, j in temp.items():
            if j >= 2:
                ans += j * (j-1) // 2
        
        return ans * 8
