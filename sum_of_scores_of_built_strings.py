'''
You are building a string s of length n one character at a time, prepending each new character to the front of the string. The strings are labeled from 1 to n, where the string with length i is labeled si.

For example, for s = "abaca", s1 == "a", s2 == "ca", s3 == "aca", etc.
The score of si is the length of the longest common prefix between si and sn (Note that s == sn).

Given the final string s, return the sum of the score of every si.
'''

class Solution:
    def sumScores(self, s: str) -> int:
        def z_function(s):
            left, right = 0, 0
            length = len(s)
            z = [0] * length
            
            for i in range(1, length):
                
                if i <= right:
                    z[i] = min(z[i - left], right - i + 1)
                
                while (i + z[i] < length and s[z[i]] == s[i + z[i]]):
                    z[i] += 1
                
                if i + z[i] - 1 > right:
                    left = i
                    right = i + z[i] - 1
                    
            return z
        
        return sum(z_function(s)) + len(s)
