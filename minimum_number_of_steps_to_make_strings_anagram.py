'''
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 
 '''

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        count = 0

        s_d = dict(Counter(s))
        t_d = dict(Counter(t))

        res = list(set(s+t))

        for i in range(len(res)):
            key = res[i]

            if key in s_d and key in t_d:
                count += abs(s_d[key] - t_d[key])
            elif key in s_d and key not in t_d:
                count += s_d[key]
            elif key in t_d and key not in s_d:
                count += t_d[key]
        return count//2
