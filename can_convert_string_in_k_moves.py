'''
Given two strings s and t, your goal is to convert s into t in k moves or less.

During the ith (1 <= i <= k) move you can:

Choose any index j (1-indexed) from s, such that 1 <= j <= s.length and j has not been chosen in any previous move, and shift the character at that index i times.
Do nothing.
Shifting a character means replacing it by the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Shifting a character by i means applying the shift operations i times.

Remember that any index j can be picked at most once.

Return true if it's possible to convert s into t in no more than k moves, otherwise return false
'''

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        # We calculate the differences
        diff = defaultdict(int)
        for sc, tc in zip(s, t):
            d = (ord(tc) - ord(sc)) % 26
            if d == 0: continue
            if d > k: return False
            diff[d] += 1
            if ((diff[d] - 1) * 26) + d > k:
                return False
        
        return True
      
---------------------------------------------------------------------------
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        
        # Check uneven lengths 
        if len(s) != len(t):
            return False 
        
		# Track used shifts
        shifts = [0 for x in range(1,27)]
      
        for i in range(len(s)):
            
			# No shift required
            if t[i] == s[i]:
                continue
			
			# Number of shifts calculation
            diff = (ord(t[i]) - ord(s[i])) % 26
			
			# Check if number of shift is permitted 
            if ((shifts[diff]) *26 + diff) > k:
                return False
            shifts[diff] += 1

        return True
