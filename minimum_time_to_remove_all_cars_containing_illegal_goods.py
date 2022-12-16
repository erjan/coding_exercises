'''
You are given a 0-indexed binary string s which represents a sequence of train cars. s[i] = '0' denotes that the ith car does not contain illegal goods and s[i] = '1' denotes that the ith car does contain illegal goods.

As the train conductor, you would like to get rid of all the cars containing illegal goods. You can do any of the following three operations any number of times:

Remove a train car from the left end (i.e., remove s[0]) which takes 1 unit of time.
Remove a train car from the right end (i.e., remove s[s.length - 1]) which takes 1 unit of time.
Remove a train car from anywhere in the sequence which takes 2 units of time.
Return the minimum time to remove all the cars containing illegal goods.

Note that an empty sequence of cars is considered to have no cars containing illegal goods.
'''

 def minimumTime(self, s):
        n = len(s)
        dp = [0] * n
        left = right = 0
        for i, c in enumerate(s):
            left = min(left + (c == '1') * 2, i + 1)
            dp[i] = left
        for i in range(n - 1, -1 , -1):
            c = s[i]
            right = min(right + (c == '1') * 2, n - 1 - i + 1)
            if i:
                dp[i - 1] += right
        return min([n] + dp)
      
------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minimumTime(self, s: str) -> int:
        ans = inf 
        prefix = 0 
        for i, ch in enumerate(s): 
            if ch == '1': prefix = min(2 + prefix, i+1)
            ans = min(ans, prefix + len(s)-1-i)
        return ans 
