'''
A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.
'''


class Solution:
    def isValid(self, word: str) -> bool:
        vowels = 'aeiou'

        word = word.lower()
        cond1 = any(ch in vowels for ch in word)
        cond2 = any(ch not in vowels and ch.isalpha() for ch in word)

        cond4 = len(word)>=3

        cond5 = all(ch.isdigit() or ch.isalpha() for ch in word)

        return cond1 and cond2 and cond4 and cond5

----------------------------------
#regex

class Solution:
    def isValid(self, w: str) -> bool:
        return match('^(?=.*[aeiou])(?=.*[^0-9aeiou])[a-z0-9]{3,}$',w,I)

------------------------------------------------------------------------------------



class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowelcount = 0
        consonantcount = 0
        validcharacterscount = 0
        vowels = "aeiou"
        
        for char in word:
            if char.isalpha():
                if char.lower() in vowels:
                    vowelcount += 1
                else:
                    consonantcount += 1
                validcharacterscount += 1
            elif char.isdigit():
                validcharacterscount += 1
            else:
                return False
        
        # Check if it meets all criteria
        return validcharacterscount >= 3 and vowelcount >= 1 and consonantcount >= 1
