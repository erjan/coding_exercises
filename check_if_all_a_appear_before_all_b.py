'''
Given a string s consisting of only the characters
'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

'''

class Solution:
    def checkString(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        last_a = s.rfind('a')
        print(last_a)

        first_b = s.find('b')
        print(first_b)
        
        if first_b == -1 or last_a == -1:
            return True
        
        if first_b < last_a:
            return False
        return True
