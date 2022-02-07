'''
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. 
It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.
'''

# my own solution!

import string
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = paragraph            
        
        p = p.lower()
    
        for character in string.punctuation:
            p = p.replace(character, ' ')

        p = p.split(' ')

        p = list(filter(lambda word: word not in banned and word != '',p))
        p = Counter(p).most_common(1)[0][0]
        print(p)
        return p

