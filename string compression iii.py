'''
Given a string word, compress it using the following algorithm:

Begin with an empty string comp. While word is not empty, use the following operation:
Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
Append the length of the prefix followed by c to comp.
Return the string comp.
'''

class Solution:
    def compressedString(self, word: str) -> str:
        comp = ''

        cnt = 1
        n = len(word)
        ch = word[0]

        for i in range(1,n):
            if word[i] == ch and cnt<9:
                cnt+=1
            else:
                
                comp += str(cnt)+ch
                ch = word[i]
                cnt = 1

       
        
        comp += str(cnt) + ch
        return comp

        
