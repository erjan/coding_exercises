'''
During the NBA playoffs, we always set the rather strong team to play with the rather weak team, like make the rank 1 team play with the rank nth team, which is a good strategy to make the contest more interesting.

Given n teams, return their final contest matches in the form of a string.

The n teams are labeled from 1 to n, which represents their initial rank (i.e., Rank 1 is the strongest team and Rank n is the weakest team).

We will use parentheses '(', and ')' and commas ',' to represent the contest team pairing. We use the parentheses for pairing and the commas for partition. During the pairing process in each round, you always need to follow the strategy of making the rather strong one pair with the rather weak one.
'''


For each round R consisting of a list of match results, pair the new round by matching player i with len(R)-1-i.

def findContestMatch(self, n):
    R = tuple(range(1, n+1))
    while len(R) > 2:
        R = tuple((R[i],R[~i]) for i in xrange(len(R)/2))
    return str(R).replace(' ','')
  
------------------------------------------------------------------

class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = map(str, range(1, n+1))
        while n > 1:
            res = ["(" + res[i] + "," + res[n-1-i] + ")" for i in range(n >> 1)]
            n >>= 1
        return res[0]
      
-----------------------------------------------------------------------------

class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        def helper(array):
            if len(array) == 1:return array[0]
            res = []
            for i in range(len(array)/2):
                res.append('('+array[i]+','+array[len(array)-1-i]+')')
            return helper(res)
        a = map(str,range(1,n+1))
        return helper(a)
