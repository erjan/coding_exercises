'''
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.
'''


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0 
        while j < len(abbr) and i < len(word): 
            if abbr[j].isalpha(): 
                if abbr[j] != word[i]: 
                    return False 
                i += 1 
                j += 1 
            else: 
                if abbr[j] == '0':  # to handle edge cases such as "01", which are invalid
                    return False 
                temp = 0 
                while j < len(abbr) and abbr[j].isdigit(): 
                    temp = temp * 10 + int(abbr[j]) 
                    j += 1 
                i += temp  
        
        return j == len(abbr) and i == len(word)
