'''
You are given a 0-indexed string s consisting of only lowercase English letters. Return the number of substrings in s that begin and end with the same character.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: s = "abcba"
Output: 7
Explanation:
The substrings of length 1 that start and end with the same letter are: "a", "b", "c", "b", and "a".
The substring of length 3 that starts and ends with the same letter is: "bcb".
The substring of length 5 that starts and ends with the same letter is: "abcba".
Example 2:

Input: s = "abacad"
Output: 9
Explanation:
The substrings of length 1 that start and end with the same letter are: "a", "b", "a", "c", "a", and "d".
The substrings of length 3 that start and end with the same letter are: "aba" and "aca".
The substring of length 5 that starts and ends with the same letter is: "abaca".
Example 3:

Input: s = "a"
Output: 1
Explanation:
The substring of length 1 that starts and ends with the same letter is: "a".
'''


Explanation
Traverse from left to right, when visiting a character C, number of substring that begin and end with C in the prefix substring is the frequency of C (in this prefix substring) + 1
For example: abcba
a: found 1, a, total 1
ab: found 1, b, total 2
abc: found 1, c, total 3
abcb: found 2, bcb and b, total 5
abcba: found 2, abcba and a, total 7
Implementation
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        d = collections.defaultdict(int)
        for c in s:
            d[c] += 1
            ans += d[c]
        return ans
------------------------------------------------------------------------

For each character, suppose there are n of them, you can pick any 2 of them to generate a substring whose length is larger than 1. That gives you nC2 = n*(n-1) / 2 substrings. Then add n substrings whose length is 1.
So for each character, it contributes n*(n-1)/2 + n = n*(n+1)/2 substrings.

def numberOfSubstrings(s):
	return sum(n*(n+1)>>1 for n in collections.Counter(s).values())
-----------------------------------------------------

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = defaultdict(list)
        for i in range(len(s)):
            count[s[i]].append(i)
        res = 0 
        for k in count:
            v = len(count[k])
            res += v*(v+1)//2
        return res
---------------------------------------------------

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        return sum((v ** 2 + v) // 2 for v in Counter(s).values())
-----------------------------------------------------------
Dynamic programming approach:

f contains the number of substrings that have the same beginning and ending letter
g contains the number of strings that ending in a specific letter(a - z)
    def numberOfSubstrings(self, s: str) -> int:
        if s == None or len(s) == 0:
            return 0
        
        n = len(s)
        f = [0 for i in range(n + 1)]
        g = [0 for i in range(26)]
        
        for i in range(1, n + 1):
            diff = ord(s[i - 1]) - ord('a')
            g[diff] = g[diff] + 1
            f[i] = f[i - 1] + g[diff]
        
        return f[n]
      
      
