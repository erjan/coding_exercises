'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

In addition to the mapping above, an encoded message may contain the '*' character, which can represent any digit from '1' to '9' ('0' is excluded). For example, the encoded message "1*" may represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.

Given a string s consisting of digits and '*' characters, return the number of ways to decode it.

Since the answer may be very large, return it modulo 109 + 7.
'''


class Solution:
    mod =  1000000007
    def solve(self,dp,s,i):
        if i==len(s):
            return 1
        if i> len(s):
            return 0
        if dp[i] != -1:
            return dp[i]
        if s[i] == "0":
            dp[i] =0
            return dp[i]
        one = 0
        if s[i] == '*':
            one += (9*self.solve(dp,s,i+1))% self.mod
        else:
            one += self.solve(dp,s,i+1)
        
        two = 0
        if  i+1 < len(s):
            if s[i+1]=='*':
                if s[i]=='*':
                    two += (15*self.solve(dp,s,i+2))% self.mod
                elif s[i] <'2':
                    two += (9*self.solve(dp,s,i+2))% self.mod
                elif s[i] == '2':
                    two += (6*self.solve(dp,s,i+2))% self.mod
            else:
                if s[i] == "*" and s[i+1]<'7':
                    two += (2*self.solve(dp,s,i+2))% self.mod
                elif s[i] <'2' or (s[i] == '2' and s[i+1] <'7'):
                    two += self.solve(dp,s,i+2)
        dp[i] = ((one % self.mod + two % self.mod)%self.mod)
        return dp[i]
                
        
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1]*(n+1)
        return self.solve(dp,s,0)
