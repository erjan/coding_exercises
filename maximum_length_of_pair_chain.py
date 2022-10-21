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

    
-----------------------------------------------------------------------------------
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        length = len(pairs)
        prev = None
        count = 0
        for i in range(0, len(pairs)):
            #Initial Case
            if not prev:
                count += 1
                prev = pairs[i]
            #Normal case explained in the question description
            elif prev[-1] < pairs[i][0]:
                prev = pairs[i]
                count += 1
            #if the current pair has smaller end than the previous then we take this
            #how do we know this is valid?
            #if we had something like this -> [[1,2],[3,10],[4,5],[6,10]]
            #we greedily replace 3,10 with 4,5 as it has smaller end which can let us
            #find more pairs, how do we know [4,5] makes valid chain with pairs before [3,10]
            #because we know that 4 > 3 and the reason why [3,10] formed pairs is that 3 was bigger
            #than numbers before it for eg: [3,10] and [1,2] --> 3 > 2 and so 4 is also bigger than 2
            elif prev[-1] > pairs[i][-1]:
                prev = pairs[i]
        return count
