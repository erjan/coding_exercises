'''
You are given a string s, an integer k, a letter letter, and an integer repetition.

Return the lexicographically smallest subsequence of s of length k that has the letter letter appear at least repetition times. The test cases are generated so that the letter appears in s at least repetition times.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

A string a is lexicographically smaller than a string b if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
'''


class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        s = list(s)
        stack = []
        countAll = s.count(letter)
        count = 0
        for ind, i in enumerate(s):
            while stack and stack[-1] > i:
                if stack[-1] == letter and i != letter:
                    if countAll+count-1 < repetition:
                        break
                if len(stack)+len(s)-ind-1 < k:
                    break
                if stack[-1] == letter:
                    count-=1
                stack.pop()
            stack.append(i)
            if i == letter:
                count+=1
                countAll-=1
        temp = 0
        while len(stack)+temp > k:
            if stack[-1] == letter and count <= repetition:
                temp+=1
            if stack[-1] == letter:
                count-=1
            stack.pop()
        return "".join(stack)+temp*letter
      
-------------------------------------------------------------------------------------------------------------
class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        rest = sum(x == letter for x in s)
        stack = []
        for i, x in enumerate(s): 
            while stack and stack[-1] > x and len(stack) + len(s) - i > k and (stack[-1] != letter or repetition < rest): 
                if stack.pop() == letter: repetition += 1
            if len(stack) < k and (x == letter or len(stack) + repetition < k): 
                stack.append(x)
                if x == letter: repetition -= 1
            if x == letter: rest -= 1
        return "".join(stack)
