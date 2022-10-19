'''
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m non-empty substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        @cache
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            choose_s1, choose_s2 = False, False
            if i < len(s1) and s1[i] == s3[i + j]:
                choose_s1 = dfs(i + 1, j)
            if j < len(s2) and s2[j] == s3[i + j]:
                choose_s2 = dfs(i, j + 1)

            return choose_s1 or choose_s2

        return dfs(0, 0)
      
-------------------------------------------------------------------------------------------
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        d={}
        m=len(s1)
        n=len(s2)
        if m==0:
            return s2==s3
        if n==0:
            return s1==s3
        if m+n!=len(s3):return False
        def dfs(i,j):
            if (i,j) in d: return d[(i,j)]
            
            c1=c2=False 
            
            if i==m and j==n: return True
                
           
            if i<m and s1[i]==s3[i+j]:c1=dfs(i+1,j)
           
            if j<n and s2[j]==s3[i+j]:c2=dfs(i,j+1)  
            
            d[(i,j)]=c1 or c2
            return c1 or c2
        
        dfs(0,0)
        return d[(0,0)]
      
--------------------------------------------------------------------------------------------------------
# O(n) space
def isInterleave3(self, s1, s2, s3):
    r, c, l= len(s1), len(s2), len(s3)
    if r+c != l:
        return False
    dp = [True for _ in xrange(c+1)] 
    for j in xrange(1, c+1):
        dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
    for i in xrange(1, r+1):
        dp[0] = (dp[0] and s1[i-1] == s3[i-1])
        for j in xrange(1, c+1):
            dp[j] = (dp[j] and s1[i-1] == s3[i-1+j]) or (dp[j-1] and s2[j-1] == s3[i-1+j])
    return dp[-1]
    
# DFS 
def isInterleave4(self, s1, s2, s3):
    r, c, l= len(s1), len(s2), len(s3)
    if r+c != l:
        return False
    stack, visited = [(0, 0)], set((0, 0))
    while stack:
        x, y = stack.pop()
        if x+y == l:
            return True
        if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
            stack.append((x+1, y)); visited.add((x+1, y))
        if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
            stack.append((x, y+1)); visited.add((x, y+1))
    return False
            
# BFS 
def isInterleave(self, s1, s2, s3):
    r, c, l= len(s1), len(s2), len(s3)
    if r+c != l:
        return False
    queue, visited = [(0, 0)], set((0, 0))
    while queue:
        x, y = queue.pop(0)
        if x+y == l:
            return True
        if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
            queue.append((x+1, y)); visited.add((x+1, y))
        if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
            queue.append((x, y+1)); visited.add((x, y+1))
    return False
  
      
