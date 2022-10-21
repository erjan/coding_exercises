'''
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.
'''

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        rt = 1
        l = pairs[0]
        for r in range(1,len(pairs)):
            if l[1] < pairs[r][0]:
                rt += 1 
                l = pairs[r]
            elif pairs[r][1]<l[1]:
                l = pairs[r]
        return rt 
      
-------------------------------------------------------------------
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp=[1 for i in range(len(pairs))]
        dp[0]=1
        for i in range(1,len(pairs)):
            for j in range(i-1,-1,-1):
                if pairs[i][0]>pairs[j][1]:
                    dp[i]=max(dp[i],dp[j]+1)
        return dp[len(pairs)-1]
