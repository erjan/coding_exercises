'''
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.
'''

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = [0]
        far = 0
        while q:
            ind = q.pop(0)
            if ind == len(s)-1:
                return True
            low = max(far+1, ind+minJump)
            high = min(len(s)-1, ind+maxJump)
            for jump in range(low, high+1):
                if s[jump] == '0':
                    q.append(jump)
            far = ind+maxJump
        return False
