'''
You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
Return the lexicographically smallest string that can be written on the pape
'''


class Solution:
    def robotWithString(self, s: str) -> str:
        result = []
        t = []
        while s:

            # Work out the minimum character in s, and the indexes of this character
            indexes = [0]
            minChar = s[0]
            for i in range(1, len(s)):
                thisChar = s[i]
                if thisChar < minChar:
                    minChar = thisChar
                    indexes = [i]
                elif thisChar == minChar:
                    indexes.append(i)

            # Are there smaller characters at the end of t? 
            # Use them!
            while t and t[-1] <= minChar:
                result.append(t.pop())

            # Now take all the minimum characters
            # (Pushing their predecessors onto t)
            prev = 0
            for i in indexes:
                t.extend(s[prev:i])
                result.append(minChar)
                prev = i + 1
            s = s[indexes[-1]+1:]

        #  Nothing left on s
        # Just take everything off t and we're done!
        result.extend(t[::-1])

       # Finally, convert the list into a string
        return "".join(result)
      
-----------------------------------------------------------------------
"""
Algorithm:
step1: keep a counter of s
        -> everytime we pop from s, we should decrease the element by 1
        -> if the element cnt is 0, remove from the counter
step2: start an iteration, in each iteration, we need to decide wheter we should pop from t and print it
       as a result, here is the rules:
        -> if there is still one element smaller than t[-1], then we cannot pop
        -> if there is not elements smaller than t[-1], then we pop until the condition does not meet
step3: check the conor case, if the s is completely reversed, t will never pop,
       at that time, just return the t[::-1]
"""
class Solution:
    def robotWithString(self, s: str) -> str:
        s_counter = Counter(s)
        t = []
        res = []
        for char in s:
            t.append(char)
            s_counter[char] -= 1
            # delete it, because this character does not exist anymore
            if s_counter[char] == 0:
                del s_counter[char]
            # start the printing process
            while t and s_counter and t[-1] <= min(s_counter):
                res.append(t.pop())
        # base case when s is empty and t is full, ex.[cba], t will be [a,b,c], never have a chance to pop
        res += t[::-1]
        return "".join(res)
      
----------------------------------------------------------------------------------------------------------------------
class Solution:
    def robotWithString(self, s: str) -> str:
        
        d = {}
        for x in s:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1

        t = []
        ans = []
        for x in s:
            t.append(x)
            if d[x] == 1:
                d.pop(x)
            else:
                d[x] -= 1
            while d and t and min(d) >= t[-1]:
                ans += t.pop()

        return "".join(ans + t[::-1])
