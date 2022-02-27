'''
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.
'''


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count= 0
        
        for i in range(len(words)):
            
            word = words[i]
            
            len_pref = len(pref)
            possible_pref = word[:len_pref]
            
            if possible_pref == pref:
                count+=1
        return count
