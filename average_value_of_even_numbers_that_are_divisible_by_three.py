'''
Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

'''


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        def getsum(n):
            q = str(n)
            res = 0
            for s in q:
                res += int(s)
                
            if res %3 == 0:
                return True
            return False
           
            
            
        even = []
        for n in nums:
            if n %2 == 0:
                even.append(n)
        
        x = []
        for n in even:
            
            if getsum(n) == True:
                x.append(n)
        
        if len(x) == 0:
            return 0
        return sum(x)//len(x)
      
-----------------------------------------------------------
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        nums = [n for n in nums if not n%6]
        
        return sum(nums)//len(nums) if nums else 0
-------------------------------
        l=[]
        for i in nums:
            if i%6==0:
                l.append(i)
        return sum(l)/len(l) if l else 0
