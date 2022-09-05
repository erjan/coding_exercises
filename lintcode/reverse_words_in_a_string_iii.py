'''
Given a string, you need to 
reverse the order of characters in each word 
within a sentence while still preserving whitespace and initial word order.
'''


class Solution:

    def reverse_words(self, s: str) -> str:
        # Write your code here

        s = s.split()

        for i in range(len(s)):
            s[i] = s[i][::-1]
        
        s = " ".join(s)
        return s
