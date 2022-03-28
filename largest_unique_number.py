'''
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
'''


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
                
        d = dict()
        
        for i in range(len(nums)):
            
            if nums[i] not in d:
                d[ nums[i]] = 1
            else:
                d[nums[i]] +=1
        
        maxi = float('inf')
        
        res = list()
        
        maxi = -1
        for k,v in d.items():
            
            if v == 1:
                if k > maxi:
                    maxi = k
        return maxi
        
        
#another

class Solution(object):
	"""
	Count the frequency of all elements then get the maximum value with the frequency of 1
	Time: O(N)
	Space: O(N)
	"""
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cnt = Counter(A)
        result = -1
        for k,v in cnt.items():
            if v == 1:
                result = max(result, k)
        return result
                
                
        
        
