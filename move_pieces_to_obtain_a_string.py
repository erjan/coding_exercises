'''
You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.
'''

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        lcnt, rcnt = 0, 0
        for c1, c2 in zip(start, target):
            if c1 == 'L': lcnt += 1
            if c2 == 'L': lcnt -= 1
            if c1 == 'R': rcnt += 1
            if c2 == 'R': rcnt -= 1
        if lcnt or rcnt: return False
        
        s_ptr = 0
        for t_ptr in range(len(target)):
            if target[t_ptr] == '_':
                continue
            else:
                while s_ptr < len(start) and start[s_ptr] == '_':
                    s_ptr += 1
                if (target[t_ptr] != start[s_ptr] or
                    target[t_ptr] == 'L' and s_ptr < t_ptr or
                    target[t_ptr] == 'R' and s_ptr > t_ptr):
                    return False
                s_ptr += 1
        return True
      
------------------------------------------------------------------------------------------------

class Solution:
                    # Criteria for a valid transormation:

                    #   1) The # of Ls, # of Rs , and # of _s must be equal between the two strings
                    #
                    #   2) The ordering of Ls and Rs in the two strings must be the same.
                    #
                    #   3) Ls can only move left and Rs can only move right, so each L in start 
                    #      cannot be to the left of its corresponding L in target, and each R cannot
                    #      be to the right of its corresponding R in target.

    def canChange(self, start: str, target: str) -> bool:
                                                          
        if (len(start) != len(target) or 
            start.count('_') != target.count('_')): return False   #  <-- Criterion 1

        s = [(ch,i) for i, ch in enumerate(start ) if ch != '_']
        t = [(ch,i) for i, ch in enumerate(target) if ch != '_']

        for i in range(len(s)):
            (sc, si), (tc,ti) = s[i], t[i]
            if sc != tc: return False                              # <-- Criteria 1 & 2
            if sc == 'L' and si < ti: return False                 # <-- Criterion 3
            if sc == 'R' and si > ti: return False                 # <--/

        return True                                                # <-- It's a winner!
      
-------------------------------------------------------------------------------------------------------------------------------------
Just keep track of two numbers:

The requested 'Ls' that have been encountered in target, which will have to be supplied by start.
The 'Rs' in start which will have to be absorbed by target
As soon as you realize the 'L's and 'R's will have to cross one another you terminate the loop.

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if len(start) != len(target):
            return False
        pendingLs = 0
        pendingRs = 0
        for i in range(len(start)):
            s, t = start[i], target[i]
            if t == 'L':
                if pendingRs:
                    return False
                pendingLs += 1
            if s == 'L':
                if not pendingLs:
                    return False
                pendingLs -= 1
            if s == 'R':
                if pendingLs:
                    return False
                pendingRs += 1
            if t == 'R':
                if not pendingRs:
                    return False
                pendingRs -= 1
        return pendingLs == 0 and pendingRs == 0
