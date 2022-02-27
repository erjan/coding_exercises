'''
You are given two strings s and t. In one step, you can append any character to either s or t.

Return the minimum number of steps to make s and t anagrams of each other.

An anagram of a string is a string that contains the same characters with a different (or the same) ordering.
'''

#my own solution!

from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        count = 0
        hash_s = dict(Counter(s))
        hash_t = dict(Counter(t))
        
        res = ''.join(set(s+t))

        for i in range(len(res)):

            if res[i] not in hash_s.keys():
                count += hash_t[res[i]]

            elif res[i] not in hash_t.keys():
                count += hash_s[res[i]]
            else:
                count += abs(hash_s[res[i]] - hash_t[res[i]])
        print(count)
        return count
