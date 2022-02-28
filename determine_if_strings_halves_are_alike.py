'''
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). 
Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        mid = len(s)//2

        first = s[:mid]
        second = s[mid:]
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        first_count = 0
        for i in range(len(first)):
            if first[i] in vowels:
                first_count += 1
        second_count = 0
        for i in range(len(second)):
            if second[i] in vowels:
                second_count += 1

        return (first_count == second_count)
