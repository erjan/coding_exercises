'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.
'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        self.dfs(s,[],res)
        return res
    
    
    def dfs(self,s,path,res):
        if not s:
            res.append(path)
            return
        
        for i in range(1,len(s)+1):
            if self.isP(s[:i]):
                self.dfs(s[i:], path + [s[:i]],res)
    
    def isP(self,s):
        return s == s[::-1]
            
        
