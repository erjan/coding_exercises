'''
You are given a string text. You should split it to k substrings (subtext1, subtext2, ..., subtextk) such that:

subtexti is a non-empty string.
The concatenation of all the substrings is equal to text (i.e., subtext1 + subtext2 + ... + subtextk == text).
subtexti == subtextk - i + 1 for all valid values of i (i.e., 1 <= i <= k).
Return the largest possible value of k.
'''

class Solution:
    def longestDecomposition(self, text: str) -> int:
        begin, end = 0, len(text) - 1
        count = 0
        
        left, right = [], []
        
        for i in range(len(text)):
            left.append(text[i])
            right.append(text[len(text) - i - 1])
            
            if left == list(reversed(right)):
                count += 1
                left, right = [], []
        
        return count
      
-------------------------------------------------------------------------------------------
def longestDecomposition(self, text: str) -> int:
    n = len(text)
    mod = 2**63-1
    power = 31
    chVal = {ch:ord(ch)-ord("a")+1 for ch in text}
    hash1,hash2,hashLen = 0 , 0, 0
    
    res = 0
    l ,r = 0 , n-1
    for i in range(n) :
        hash1 = ( hash1 + chVal[text[l]]*(power**hashLen) ) % mod     # forward rolling hash
        hash2 = ( hash2*power + chVal[text[r]] ) % mod                 # reverse rolling hash 
        if hash1 == hash2 :
            res += 1
            hash1 , hash2 ,hashLen = 0 , 0 , 0
        else:
            hashLen += 1
        l += 1
        r -=1
    return res
  
---------------------------------------------------------------------------------------------------------------  


class Solution:
    def longestDecomposition(self, text: str) -> int:
        n=len(text)-1
        dp=[[-1 for i in range(n+1)] for j in range(n+1)]
        def dfs(start,end):
            if start>end:
                return 0
            if dp[start][end]!=-1:
                return dp[start][end]
            best=1
            l,r=start,end
            mid=(r+l)//2
            while r>mid:
                chunk=end-r+1
                if text[l:l+chunk]==text[r:end+1]:
                    val=dfs(l+chunk,r-1)+2
                    best=max(best,val)
                r-=1
            dp[start][end]=best
            return dp[start][end]
        return dfs(0,n)
                    
