'''
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.
'''

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def find(w):
            
            l = []
            
            d = defaultdict(int)
            i = 0
            
            for char in w:
                
                if char in d:
                    l.append(d[char])
                    
                else:
                    i+=1
                    d[char] = i
                    l.append(d[char])
            return l                
        res = []
        patternword_pattern = find(pattern)
        
        for word in words:
            word_pattern = find(word)
            if word_pattern == patternword_pattern:
                res.append(word)
                
        return res
                
