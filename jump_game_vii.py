'''
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.
'''

min_i and max_i are the range 
of positions that we can reach for the
next step. If at some point we find the last index in this range, that
means the last index is reachable. If my current index i is greater than max_i, we can't reach this position 
and won't be able to continue jumping. We ignore
those 'invalid' position (s[i] == 1 or i < min_i) because we can't jump from these positions.

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        n = len(s)
        min_i = max_i = 0
        for i in range(n-1):
            if s[i] == '1' or i < min_i:
                continue
            if i > max_i:
                return False
            min_i = i + minJump
            max_i = min(i + maxJump, n-1)
            if min_i <= n-1 <= max_i:
                return True
        return False
