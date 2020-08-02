'''
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.
'''


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = 0
        bal = 0
        for i in range(len(s)):
            if s[i] == 'R':
                bal+=1
            if s[i] == 'L':
                bal-=1
            if bal==0:
                counter+=1
        print('counter %d' % counter)
        return counter
