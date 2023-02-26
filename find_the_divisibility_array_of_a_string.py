'''
You are given a 0-indexed string word of length n consisting of digits, and a positive integer m.

The divisibility array div of word is an integer array of length n such that:

div[i] = 1 if the numeric value of word[0,...,i] is divisible by m, or
div[i] = 0 otherwise.
Return the divisibility array of word.
'''


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        x=0
        a=[]
        for i in word:
            x=x*10+int(i)
            if(x%m==0):
                a+=[1]
            else:
                a+=[0]
            x%=m
        return a
----------------------------------------------------------------------------------------------------------------------------
Using the mathematical property that
ab (mod m) ≡ ((a (mod m) * 10) + (b (mod m))) mod m
We can compute and store the mod of current digit and use it for the next digit. No TLE due to small modulo operations.

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        mod = 0
        div = []

        for i in range(0, len(word)):
            mod = (mod * 10 + int(word[i])) % m
            div.append(1 if mod % m == 0 else 0)
        return div
