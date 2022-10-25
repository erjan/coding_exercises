'''
Given an array of digit strings nums 
and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the 
concatenation of nums[i] + nums[j] equals target.
'''

class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        #sol2 using Counter and iterative check
        counter,ans=Counter(nums),0
        for i in range(1,len(target)):
            a,b=target[:i],target[i:]
            if a not in counter or b not in counter:continue
            ans=ans+counter[a]*counter[b] if a!=b else ans+counter[a]*(counter[a]-1)
        return ans
-------------------------------------------------------------------------------------------------------------
class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        #sol1:brute force check
        ans=0
        for i in range(len(nums)):
            fst=nums[i]
            for j in range(len(nums)):
                if i==j:continue
                if fst+nums[j]==target:ans=ans+1
        return ans
