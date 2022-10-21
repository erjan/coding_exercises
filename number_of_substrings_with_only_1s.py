'''
Given a binary string s, return the number of substrings 
with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.
'''

def numSub(self, s: str) -> int:
    ans = cum = 0
    for x in s:
        if x == "1":
            cum+=1
            ans+=cum
        else:
            cum = 0
    return ans%(10**9+7)
  
-----------------------------------------------------------------------------------------------
class Solution:
    def numSub(self, s: str) -> int:
        cnt, ans = 0, 0
        for i in range(len(s)):
            if s[i] == '0':
                cnt = 0
            else:
                cnt += 1
                ans += cnt
        return ans % ((10**9)+7)
      
--------------------------------------------------------------

The example would be self explanatoy:
"0110111" can be evaluated to -->
0120123
Now if we sum up all these digits:
1+2+1+2+3 = 9 is the result!

class Solution(object):
    def numSub(self, s):
        res, currsum = 0,0
        for digit in s:
            if digit == '0':
                currsum = 0
            else:
                currsum += 1 
                res+=currsum 
        return res % (10**9+7)
      
