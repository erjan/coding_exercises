'''
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s,wordDict,{})
    
    def helper(self, s,wordDict,memo):
        
        if s in memo:
            return memo[s]
        if not s:
            return []
        
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            
            if len(word) == len(s):
                res.append(word)
            else:
                resultofrest = self.helper(s[len(word):], wordDict,memo)
                for item in resultofrest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res
