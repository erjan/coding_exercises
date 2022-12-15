'''
Given two strings s and t, transform string s into string t using the following operation any number of times:

Choose a non-empty substring in s and sort it in place so the characters are in ascending order.
For example, applying the operation on the underlined substring in "14234" results in "12344".
Return true if it is possible to transform s into t. Otherwise, return false.

A substring is a contiguous sequence of characters within a string.
'''


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        if sorted(s) != sorted(t): return False # edge case 
        
        pos = [deque() for _ in range(10)]
        for i, ss in enumerate(s): pos[int(ss)].append(i)
            
        for tt in t: 
            i = pos[int(tt)].popleft()
            for ii in range(int(tt)): 
                if pos[ii] and pos[ii][0] < i: return False # cannot swap 
        return True 
      
-----------------------------------------------------------------------------------------------------------------------------
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        if s == t:
            return True
        big_table = [deque() for _ in range(10)]
        for i, c in enumerate(s):
            big_table[int(c)].append(i)
        
        for c in t:
            if not big_table[int(c)]: return False
            i = big_table[int(c)].popleft()
            for j in range(int(c)):
                if big_table[j] and big_table[j][0] < i:
                    return False
        return True

