'''
Given a string s consisting of lowercase English letters, return the first letter to appear twice.
'''

#my own solution

from collections import Counter

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        d = dict(Counter(s))
        n = []
        for k, v in d.items():
            if v >= 2:
                n.append([k, v])

        mini = float('inf')
        letter = ''
        for k, v in n:
            check = k
            counter = 0
            for i in range(len(s)):
                if s[i] == check:
                    counter += 1
                    if counter == 2:
                        if i < mini:
                            mini = i
                            letter = check
                        #mini.append([check, i])
        #print(mini, letter)
        return letter
        
-----------------------------------------------------
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        occurences = defaultdict(int)
        for char in s:
            occurences[char] += 1
            if occurences[char] == 2:
                return char

