'''
You are given an integer array nums. The adjacent integers in nums will perform the float division.

For example, for nums = [2,3,4], we will evaluate the expression "2/3/4".
However, you can add any number of parenthesis at any position to change the priority of operations. You want to add these parentheses such the value of the expression after the evaluation is maximum.

Return the corresponding expression that has the maximum value in string format.

Note: your expression should not contain redundant parenthesis.
'''

def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums)<3:
            result=''.join([str(num)+'/' for num in nums])
            return result[:-1]
        result=[]
        result.append(str(nums[0])+'/(')
        for i in range(1,len(nums)):
            result.append(str(nums[i]))
            result.append('/')
        result=result[:-1]
        result.append(')')
        return ''.join(result)
      
----------------------------------------------------
class Solution(object):
    def optimalDivision(self, nums):

        A = list(map(str, nums))
        
        
        if len(A) <= 2:
            
            return '/'.join(A)
        
        
        return A[0] + '/(' + '/'.join(A[1:]) + ')'
