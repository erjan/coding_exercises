'''
Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.
'''

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        s1 = Counter(words1)
        s2 = Counter(words2)

        s1 = dict(s1.items())
        s2 = dict(s2.items())
  
        count = 0
        for k, v in s1.items():
            if v == 1 and k in s2.keys():
                if s2[k] == 1:
                    count += 1
        return count
        
