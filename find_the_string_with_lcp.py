'''
We define the lcp matrix of any 0-indexed string word of n lowercase English letters as an n x n grid such that:

lcp[i][j] is equal to the length of the longest common prefix between the substrings word[i,n-1] and word[j,n-1].
Given an n x n matrix lcp, return the alphabetically smallest string word that corresponds to lcp. If there is no such string, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position 
where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding 
letter in b. For example, "aabd" is lexicographically smaller than "aaca" because the first position they differ is at the third letter, and 'b' comes before 'c'.
'''

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        ans = []
        for i in range(n): 
            tabu = set()
            for j in range(i): 
                if lcp[i][j]: 
                    ans.append(ans[j])
                    break
                else: tabu.add(ans[j])
            else: 
                for ch in ascii_lowercase: 
                    if ch not in tabu: 
                        ans.append(ch)
                        break
                else: return ""
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1): 
            for j in range(n-1, -1, -1): 
                if ans[i] == ans[j]: 
                    if i == n-1 or j == n-1: dp[i][j] = 1
                    else: dp[i][j] = 1 + dp[i+1][j+1]
                if dp[i][j] != lcp[i][j]: return ""
        return "".join(ans)
      
--------------------------------------------------------------------------------------------------------------
First we build s from left to right. For position i, we will fill it with current smallest char if it is empty. Next we will check lcp with all other substrings starting with i+1, i+2, ..., n-1. If lcp[i][j] > 0, it means s[j] == s[i].
Repeat this process we will always get a string. Then we use z-function to check the lcp matrix. The detail of z-function please refer to https://cp-algorithms.com/string/z-function.html.

Notice:

The lcp matrix is symmetric. The diagonal element is same as the substring length.
Make sure the chars we used are not exceed 26.
Code
class Solution:
    def z_function(self, s):
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i <= r and z[i - l] < r - i + 1:z[i] = z[i - l]
            else:
                z[i] = max(0, r - i + 1)
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:z[i] += 1
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
        z[0] = len(s)
        return z

    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        s, idx = [''] * n, 0
        for i in range(n):
            if i + lcp[i][i] != n: return ''
            if s[i] == '':
                if idx > 25: return ''
                s[i] = chr(ord('a') + idx)
                idx += 1
            for j in range(i + 1, n):
                if lcp[i][j] != lcp[j][i]: return ''
                if lcp[i][j]:
                    if s[j] != '' and s[j] != s[i]: return ''
                    s[j] = s[i]
        s = ''.join(s)
        return '' if any(self.z_function(s[i:]) != lcp[i][i:] for i in range(n)) else s
