'''
There is a special keyboard with all keys in a single row.

Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25). 
Initially, your finger is at index 0. To type a character, you have to move your finger to the index of the desired character.
The time taken to move your finger from index i to index j is |i - j|.

You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.
'''


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        
        r = [i for i in range(0, 26)]
        abc = dict(zip(keyboard, r))
        
        total = 0
        prev = 0
        for ch in word:
            
            total += abs(  abc[ch] - prev   )
            
            prev = abc[ch]
            
        print(total)
        return total
