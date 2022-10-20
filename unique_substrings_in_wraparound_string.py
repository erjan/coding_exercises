'''
We define the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this:

"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
Given a string p, return the number of unique non-empty substrings of p are present in s.
'''

---------------------------------------------------------------------------------------------------------------------

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        
        dp = [0 for _ in range(len(p))]
        dp[0] = 1

        for i in range(1,len(p)):
            if ord(p[i]) - ord(p[i-1])==1 or p[i]=='a'and p[i-1]=='z':
                dp[i] = dp[i-1]+1
            else:
                dp[i] = 1

        dic = {}
        for i in range(len(p)):
            if p[i] in dic:
                dic[p[i]] = max(dic[p[i]],dp[i])
            else:
                dic[p[i]] = dp[i]

        res = 0
        for k,v in dic.items():
            res += v

        return res
