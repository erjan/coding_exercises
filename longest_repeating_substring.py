
'''
Given a string s, return the length of the longest repeating substrings. If no repeating substring exists, return 0.


'''


class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        subStrDict = {}  
        # two pointers to count substring
        for i in range(len(s)):
            for j in range(i+1):
                subStrDict[s[j:i+1]] = subStrDict.get(s[j:i+1], 0) +1   
        # gather repeating substring and return the max len of key
        repeatStr = [key for (key,value) in subStrDict.items() if value > 1]    
        return len(max(repeatStr, key = len)) if len(repeatStr) > 0 else 0

      
-----------------------------------------------------------------------------------------
(1)
Find longest substrings using dp
Example for s = "abab"
image

(2)
In the dp table:
number of substrings of length 1 for column 1 is 2: {a:2}
number of substrings of length 1 for column 2 is 2: {b:2}
number of substrings of length 2 for column 2 is 2: {ab:2}
number of substrings of length 1 for column 3 is 2: {a:2}
number of substrings of length 2 for column 3 is 1: {ba:2}
number of substrings of length 3 for column 3 is 1: {aba:3}
so on...

if there are more than one occourances of highest length in a column, then second_highest = highest
else if there is only one occourance of the highest, the second highest is the answer for that column because the highest length substring contains the second highest length substring.

image

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        
        dp = [[0 if s[i] != s[j] else 1 for j in range(len(s))] for i in range(len(s))]
        
        for i in range(1, len(s)):
            for j in range(1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
        
        ret = 0
        for l in dp:
            highest = -math.inf
            secondHighest = -math.inf
            for m in l:
                if m > highest:
                    secondHighest = highest
                    highest = m
            ret = max(ret, secondHighest)
			
        return ret
      
------------------------------------------------------------------------
class Solution: 
    def search(self, S: str, length: int) -> bool:
        visited = set()
        for i in range(len(S)-length+1):
            substring = S[i:i+length]
            if substring in visited: return True
            visited.add(substring)    
        return False
        
    def longestRepeatingSubstring(self, S: str) -> str:
        left, right = 0, len(S)-1
        while left <= right:
            middle = left + (right-left+1)//2
            if self.search(S, middle): left = middle+1
            else: right = middle-1
        return left-1
      
---------------------------------------------------------------------------------------
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        MOD = 1_000_000_007
        
        fac = [1]
        prefix = [0]
        for ch in s: 
            fac.append((fac[-1] * 26 % MOD))
            prefix.append((prefix[-1]*26 + ord(ch) - 97) % MOD)
            
        def fn(k): 
            """Return True if a repeating substring of length k is found."""
            seen = set()
            for i in range(len(s)-k+1): 
                val = (prefix[i+k] - prefix[i]*fac[k]) % MOD 
                if val in seen: return True # rolling hash (ver. Monte Carlo)
                seen.add(val)
            return False 
        
        # last-true binary search 
        lo, hi = -1, len(s)-1
        while lo < hi:
            mid = lo + hi + 1 >> 1
            if fn(mid): lo = mid
            else: hi = mid - 1
        return lo
      
      
      
