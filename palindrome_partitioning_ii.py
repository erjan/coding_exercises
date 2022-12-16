'''
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
.

Return the minimum cuts needed for a palindrome partitioning of s.
'''

# python code

class Solution(object):
    def minCut(self, s):
        """
        s="abcgcbafj"
        :type s: str
        :rtype: int
        """
      
        if s == s[::-1]:
            return 0
        
        for i in range(len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        
        l=len(s)
      
        #d=[[0 for i  in range(l)] for j in range(l)]
        x=[[0 for i  in range(l)] for j in range(l)]
        for i in range(l):
          for j in range(i,l):
            st=s[i:j+1]
            #d[i][j]=st
            x[i][j]= (st==st[::-1])
                      
            
        p=[0 for c in range(l)]
        for i in range(1,l):
          if x[0][i]:
            p[i]=0
          else:
            m=float("inf")
            for j in range(i,0,-1):
              if x[j][i]: 
                m=min(m,p[j-1])
            p[i]=m+1
        return p[-1]
  
       
