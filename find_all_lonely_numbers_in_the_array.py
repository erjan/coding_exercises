'''
You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.

Return all lonely numbers in nums. You may return the answer in any order.

 
 '''

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        
        d = dict(Counter(nums))
        
        res = list()
        for k,v in d.items():
            
            if k-1 not in d.keys() and k+1 not in d.keys() and v== 1:
                
                res.append(k)
                
        return res
