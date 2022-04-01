
'''
Given an array nums 
of integers and integer k, return the 
maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If 
no i, j exist satisfying this equation, return -1.
'''



#brute force

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
                
        answer = -1
        a = nums
        
        for i in range(len(a)):
            
            for j in range(i):
                
                if a[i] + a[j] < k:
                    answer = max(answer, a[i]+ a[j])
                    
        return answer

    
#another    
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        res = -1        
        nums.sort()        
        i = 0
        j = len(nums)-1        
        while i < j:
            
            potential_sum = nums[i] + nums[j]
            
            if potential_sum < k:
                res = max(res, potential_sum)
                i+=1
            else:
                j = j - 1
        
        return res
                
                
