'''
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
'''

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:

        output = [0 for i in range(len(s))]
        pos = -len(s)

        for i in range(len(s)):
            if s[i] == c:
                pos = i

            output[i] = i - pos

        #s = s[::-1]
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                pos = i
            output[i] = min(output[i], abs(i - pos))
        print(output)
        return output
