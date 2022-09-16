'''
Given two integers a and b, return any string s such that:

s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
The substring 'aaa' does not occur in s, and
The substring 'bbb' does not occur in s.
'''

class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        output = ""
        a = 0  # length of last sequence of 'a'
        b = 0  # length of last sequence of 'b'
        i = 0
        size = A + B
        
        while i < size:
            if (a < 2 and A > B) or b==2:
                output += 'a'
                b = 0
                a += 1
                A -= 1
            else: 
                output += 'b'
                b += 1
                a = 0
                B -= 1
            i += 1
            
        return output    
