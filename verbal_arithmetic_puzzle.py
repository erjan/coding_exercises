'''
Given an equation, represented by words on the left side and the result on the right side.

You need to check if the equation is solvable under the following rules:

Each character is decoded as one digit (0 - 9).
No two characters can map to the same digit.
Each words[i] and result are decoded as one number without leading zeros.
Sum of numbers on the left side (words) will equal to the number on the right side (result).
Return true if the equation is solvable, otherwise return false.
'''



class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        if max(map(len, words)) > len(result): return False # edge case 
        
        words.append(result)
        digits = [0]*10 
        mp = {} # mapping from letter to digit 
        
        def fn(i, j, val): 
            """Find proper mapping for words[i][~j] and result[~j] via backtracking."""
            if j == len(result): return val == 0 # base condition 
            if i == len(words): return val % 10 == 0 and fn(0, j+1, val//10)
            
            if j >= len(words[i]): return fn(i+1, j, val)
            if words[i][~j] in mp: 
                if j and j+1 == len(words[i]) and mp[words[i][~j]] == 0: return # backtrack (no leading 0)
                if i+1 == len(words): return fn(i+1, j, val - mp[words[i][~j]])
                else: return fn(i+1, j, val + mp[words[i][~j]])
            else: 
                for k, x in enumerate(digits): 
                    if not x and (k or j == 0 or j+1 < len(words[i])): 
                        mp[words[i][~j]] = k
                        digits[k] = 1
                        if i+1 == len(words) and fn(i+1, j, val-k): return True 
                        if i+1 < len(words) and fn(i+1, j, val+k): return True 
                        digits[k] = 0
                        mp.pop(words[i][~j])
        
        return fn(0, 0, 0)
