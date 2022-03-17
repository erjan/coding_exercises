'''
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
'''

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        res = dict(collections.Counter(s))

        values = list(res.values())
        if len(set(values) ) > 1:
            return False
        return True
